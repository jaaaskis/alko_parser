from typing import Union
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.modules.recommendations import get_random_beer_recommendations_with_budget
from app.modules.constants import path_to_file
from app.modules.utils import get_beers_from_alko_xlsx

app = FastAPI()
favicon_path = "static/favicon.ico"

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/favicon.ico")
def favicon():
    return FileResponse(favicon_path)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/beers/{amount}")
def get_recommendations(amount: int, q: Union[str, None] = None):
    beer_df = get_beers_from_alko_xlsx(path_to_file)
    budget = int(q["budget"]) if q else 20
    tastings = get_random_beer_recommendations_with_budget(
        beer_df, amount, budget)
    return tastings
