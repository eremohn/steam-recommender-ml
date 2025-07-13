"""
main.py  –  Steam Recommender API
"""

from pathlib import Path
import os
import pandas as pd
from fastapi import FastAPI, HTTPException
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer

# ───────────────────────── CONFIG ──────────────────────────
BASE_DIR     = Path(__file__).resolve().parent
PARQUET_DIR  = Path(os.getenv("PARQUET_DIR", BASE_DIR / "data" / "processed" / "parquet"))

USER_REVIEWS_FP   = PARQUET_DIR / "user_reviews.parquet"
GAMES_FP          = PARQUET_DIR / "output_steam_games.parquet"
USERS_ITEMS_FP    = PARQUET_DIR / "australian_users_items.parquet"

# ───────────────────────── DATA ────────────────────────────
user_reviews           = pd.read_parquet(USER_REVIEWS_FP)
output_steam_games     = pd.read_parquet(GAMES_FP)
australian_users_items = pd.read_parquet(USERS_ITEMS_FP)

# Modelo KNN basado en contenido
def _to_str(x):
    if isinstance(x, list):
        return " ".join(map(str, x))
    if x is None or (isinstance(x, float) and pd.isna(x)):
        return ""
    return str(x)

output_steam_games["combined_features"] = (
    output_steam_games["genres"].apply(_to_str) + " " + output_steam_games["tags"].apply(_to_str)
)

vectorizer      = TfidfVectorizer()
X_features      = vectorizer.fit_transform(output_steam_games["combined_features"])
knn_model       = NearestNeighbors(metric="cosine", algorithm="brute").fit(X_features)

def get_recommendations(item_id: int, k: int = 5):
    idx_list = output_steam_games.index[output_steam_games["item_id"] == item_id].tolist()
    if not idx_list:
        return []
    idx = idx_list[0]
    _, indices = knn_model.kneighbors(X_features[idx], n_neighbors=k + 1)
    return indices.flatten()[1:].tolist()  # sin el propio juego

# ───────────────────────── API ─────────────────────────────
app = FastAPI(title="Steam Recommender API")

@app.get("/")
def root():
    return {
        "message": "Bienvenido. Visita /docs para la API interactiva."
    }

# ---------- developer ----------
@app.get("/developer")
def developer(desarrollador: str):
    if desarrollador not in output_steam_games["developer"].unique():
        return {"error": "Desarrollador no encontrado"}

    df = output_steam_games[output_steam_games["developer"] == desarrollador].copy()
    df["release_date"] = pd.to_datetime(df["release_date"])
    df["year"] = df["release_date"].dt.year
    df["free"] = df["tags"].apply(_to_str).str.contains("Free", case=False)

    res = (
        df.groupby(["year", "developer"])
          .agg(cantidad_de_items=("item_id", "count"),
               contenido_free=("free", "mean"))
          .reset_index()
    )
    res["contenido_free"] = (res["contenido_free"] * 100).round(2).astype(str) + "%"
    return res.to_dict(orient="records")

# ---------- userdata ----------
@app.get("/userdata")
def userdata(user_id: str):
    user_items = australian_users_items[australian_users_items["user_id"] == user_id]
    if user_items.empty:
        raise HTTPException(404, detail="Usuario no encontrado")

    merged = user_items.merge(output_steam_games[["item_id", "price"]],
                              on="item_id", how="left")
    money_spent = merged["price"].sum()
    rec_pct = user_reviews[user_reviews["user_id"] == user_id]["recommend"].mean() * 100
    items_count = len(user_items)

    return {
        "Usuario": user_id,
        "Dinero gastado": float(round(money_spent, 2)),
        "% de recomendación": round(rec_pct, 2),
        "Cantidad de items": items_count
    }

# ---------- UserForGenre ----------
@app.get("/UserForGenre")
def user_for_genre(genero: str):
    mask = australian_users_items["item_name"].str.contains(genero, case=False, na=False)
    user_items_genre = australian_users_items[mask]

    if user_items_genre.empty:
        raise HTTPException(404, detail="Género sin datos")

    user_playtime = (
        user_items_genre.groupby("user_id")["playtime_forever"]
        .sum().reset_index()
    )
    top_user = user_playtime.loc[user_playtime["playtime_forever"].idxmax()]
    top_user_id = top_user["user_id"]

    games_user = australian_users_items[
        (australian_users_items["user_id"] == top_user_id) & mask
    ].merge(output_steam_games[["item_id", "release_date"]], on="item_id", how="left")

    games_user["release_date"] = pd.to_datetime(games_user["release_date"])
    playtime_year = (
        games_user.groupby(games_user["release_date"].dt.year)["playtime_forever"]
        .sum().reset_index(names=["Año", "Horas"])
        .astype({"Año": int})
        .to_dict(orient="records")
    )

    return {f"Usuario con más horas {genero}": top_user_id, "Horas jugadas": playtime_year}

# ---------- best_developer_year ----------
@app.get("/best_developer_year")
def best_developer_year(año: int):
    games_year = output_steam_games[pd.to_datetime(output_steam_games["release_date"]).dt.year == año]
    if games_year.empty:
        raise HTTPException(404, detail="Año sin datos")

    desarrolladores = {}
    for _, row in games_year.iterrows():
        dev = row["developer"]
        recs = user_reviews[
            (user_reviews["item_id"] == row["item_id"]) &
            (user_reviews["recommend"]) &
            (user_reviews["sentiment_analysis"] > 0)
        ]
        desarrolladores[dev] = desarrolladores.get(dev, 0) + len(recs)

    top3 = sorted(desarrolladores.items(), key=lambda x: x[1], reverse=True)[:3]
    return [{f"Puesto {i+1}: {dev}": cant} for i, (dev, cant) in enumerate(top3)]

# ---------- developer_reviews_analysis ----------
@app.get("/developer_reviews_analysis")
def developer_reviews_analysis(desarrolladora: str):
    ids = output_steam_games.loc[
        output_steam_games["developer"] == desarrolladora, "item_id"
    ]
    revs = user_reviews[user_reviews["item_id"].isin(ids)]

    neg = len(revs[revs["sentiment_analysis"] == 0])
    pos = len(revs[revs["sentiment_analysis"] == 2])
    if neg == pos == 0:
        raise HTTPException(404, detail="Desarrollador sin datos")

    return {desarrolladora: {"Negative": neg, "Positive": pos}}

# ───────── utilitario de búsqueda por nombre ─────────
def find_game_id_by_name(name: str) -> int | None:
    """Devuelve el item_id cuyo app_name coincide (case-insensitive)."""
    mask = output_steam_games["app_name"].str.lower() == name.lower()
    ids  = output_steam_games.loc[mask, "item_id"].tolist()
    return ids[0] if ids else None

# ───────── nuevo endpoint por nombre ─────────
@app.get("/recomendacion")
def recomendacion_por_nombre(name: str, k: int = 5):
    """
    Devuelve recomendaciones basadas en el nombre de un juego (app_name).
    Ejemplo:  /recomendacion?name=Portal
    Opcional: k (cantidad de recomendaciones, default=5)
    """
    game_id = find_game_id_by_name(name)
    if game_id is None:
        raise HTTPException(404, detail="Juego no encontrado")

    rec_idxs = get_recommendations(game_id, k)
    if not rec_idxs:
        raise HTTPException(404, detail="No se hallaron juegos similares")

    titles = output_steam_games.loc[rec_idxs, "app_name"].dropna().tolist()
    return {"juego_consultado": name, "recomendaciones": titles}

# ───────── endpoint original por ID (opcional) ─────────
@app.get("/recomendacion_juego/{juego_id}")
def recomendacion_juego(juego_id: int, k: int = 5):
    rec_idxs = get_recommendations(juego_id, k)
    if not rec_idxs:
        raise HTTPException(404, detail="Juego no encontrado o sin similares")

    titles = output_steam_games.loc[rec_idxs, "app_name"].dropna().tolist()
    return {"juego_id": juego_id, "recomendaciones": titles}

# ────────────────────── Runner local ───────────────────────
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(os.getenv("PORT", 8000)),
        reload=True,
    )
