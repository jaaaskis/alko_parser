from difflib import get_close_matches
from math import ceil
import os
import pandas as pd

from app.modules.database.queries import add_manufacturer_query

from .constants import (
    ALKO_STORE_INVENTORY_URL_FI,
    ALKO_STORE_PRODUCT_URL_FI,
    PATH_TO_BEERS,
    PATH_TO_WHOLE_INVENTORY,
    ALKO_STORE_PRODUCTS_FI,
)


def get_inventory_url(sku: str):
    return ALKO_STORE_INVENTORY_URL_FI + str(sku)


def get_product_url(sku: str):
    return ALKO_STORE_PRODUCT_URL_FI + str(sku)


def get_rounded_float(n: float):
    return ceil((n) * 100) / 100


def get_alko_urls(df: pd.DataFrame):
    urls = []
    for idx in df.index:
        url = get_product_url(df["Numero"][idx])
        urls.append(url)
    return urls


def trim_alko_inventory_head(df: pd.DataFrame):
    # Drop first two rows of the Excel since they're not relevant
    df = df.drop([0, 1])
    # Assign the new first row as the column names
    df.columns = df.iloc[0]
    # Pick only beers from the list
    df = df[df["Tyyppi"] == "oluet"]
    # Reset DataFrame index
    df = df.reset_index()
    # Convert price column to numbers
    df = df.astype({"Hinta": float})
    return df


def get_or_create_beers_dataframe():
    # Check if filtered excel exists
    beer_df = os.path.isfile(PATH_TO_BEERS)
    if beer_df:
        df = pd.read_excel(PATH_TO_BEERS, engine="openpyxl")
        return df

    # If no filtered excel check if inventory excel exists
    inventory_df = os.path.isfile(PATH_TO_WHOLE_INVENTORY)
    if inventory_df:
        df = pd.read_excel(PATH_TO_WHOLE_INVENTORY, engine="openpyxl")
        df = trim_alko_inventory_head(df)
        # Write excel to file
        print("Writing beers.xlsx ...")
        df.to_excel(PATH_TO_BEERS)
        return df

    # If no excel fetch the latest from Alko
    try:
        df = pd.read_excel(ALKO_STORE_PRODUCTS_FI, engine="openpyxl")
        # Check that ./data folder exists and if not create it
        if not os.path.exists("./data"):
            print("Making ./data directory...")
            os.mkdir("./data")

        # Write whole inventory
        print("Writing whole inventory .xlsx ...")
        df.to_excel(PATH_TO_WHOLE_INVENTORY)

        beers = trim_alko_inventory_head(df)
        # Write beers.xlsx
        print("Writing beers.xlsx ...")
        beers.to_excel(PATH_TO_BEERS)

        return beers
    except:
        print("Something went wrong!")


def parse_product(data: tuple):
    return {
        "name": data[0],
        "type": data[1],
        "subtype": data[2],
        "brewery": data[3],
        "abv": data[4],
    }
