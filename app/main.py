import time
import uvicorn
from typing import Union
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.modules.recommendations import get_random_beer_recommendations_with_budget
from app.modules.utils import get_or_create_beers_dataframe, get_rounded_float

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
def get_recommendations(amount: int, budget: Union[str, None] = None):
    start_time = time.time()
    beer_df = get_or_create_beers_dataframe()
    if beer_df is not None:
        budget = int(budget) if budget else 20
        tastings = get_random_beer_recommendations_with_budget(
            beer_df, amount, budget)
        end_time = time.time()
        elapsed = get_rounded_float(end_time - start_time)
        print('Got beers in %s ms' % elapsed)

        return tastings

    print('No Excel data to work with')
    return {"message": "All out of beer"}


if __name__ == "__main__":
    uvicorn.run(app, "127.0.0.1", 8000)
