import time
import datetime
import uvicorn
from typing import Union
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.modules.database.main import (
    get_all_manufacturers,
    get_all_stores,
    get_manufacturer_by_id,
    get_product_by_id,
    get_store_by_id,
    insert_store,
    test_connection,
    get_all_products,
)
from app.modules.recommendations import get_random_beer_recommendations_with_budget
from app.modules.scraper import scrape_alko_stores
from app.modules.utils import (
    get_or_create_beers_dataframe,
    get_rounded_float,
    parse_product,
)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/favicon.ico")
def favicon():
    now = datetime.datetime.now()
    hour = now.hour
    if hour < 20 and hour > 8:
        favicon_day = "static/favicon.ico"
        return FileResponse(favicon_day)
    else:
        favicon_night = "static/favicon_empty.ico"
        return FileResponse(favicon_night)


@app.get("/")
def read_root():
    result = test_connection()
    return result


@app.get("/manufacturers")
def get_manufacturers():
    start_time = time.time()
    results = get_all_manufacturers()
    end_time = time.time() - start_time
    return {
        "count": len(results),
        "elapsed": get_rounded_float(end_time),
        "result": results,
    }


@app.get("/manufacturer/{id}")
def get_manufacturer(id: int):
    result = get_manufacturer_by_id(id)
    return result


@app.get("/products")
def get_products():
    start_time = time.time()
    results = get_all_products()
    end_time = time.time() - start_time
    return {
        "count": len(results),
        "elapsed": get_rounded_float(end_time),
        "result": results,
    }


@app.get("/product/{id}")
def get_product(id: int):
    result = get_product_by_id(id)
    result = parse_product(result)
    return result


@app.get("/stores")
def get_products():
    start_time = time.time()
    results = get_all_stores()
    end_time = time.time() - start_time
    return {
        "count": len(results),
        "elapsed": get_rounded_float(end_time),
        "results": results,
    }


@app.get("/store/{id}")
def get_products(id: int):
    result = get_store_by_id(id)
    return result


@app.get("/scraper/stores")
def scrape_stores(insert: bool = False):
    """Temporary endpoint to insert Alko stores into DB"""
    start_time = time.time()
    res = scrape_alko_stores()
    if insert:
        for addr in res:
            insert_store(addr[0], addr[1])
    end_time = time.time() - start_time
    return {"message": "OK", "elapsed": get_rounded_float(end_time), "stores": res}


@app.get("/random/{amount}")
def get_recommendations(amount: int, budget: Union[str, None] = None):
    start_time = time.time()
    beer_df = get_or_create_beers_dataframe()
    if beer_df is not None:
        budget = int(budget) if budget else 20
        tastings = get_random_beer_recommendations_with_budget(beer_df, amount, budget)
        end_time = time.time()
        elapsed = get_rounded_float(end_time - start_time)
        print("Got beers in %s ms" % elapsed)

        return tastings

    print("No Excel data to work with")
    return {"message": "All out of beer"}


if __name__ == "__main__":
    uvicorn.run(app, "127.0.0.1", 8000)
