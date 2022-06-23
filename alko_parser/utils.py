from math import ceil
import pandas as pd
from constants import alko_store_inventory_url_fi, alko_store_product_url_fi


def get_inventory_url(sku: str):
    return alko_store_inventory_url_fi + str(sku)


def get_product_url(sku: str):
    return alko_store_product_url_fi + str(sku)


def get_rounded_float(n: float):
    return ceil((n)*100)/100


def get_alko_urls(df: pd.DataFrame):
    urls = []
    for idx in df.index:
        url = get_product_url(df['Numero'][idx])
        urls.append(url)
    return urls


def get_beers_from_alko_xlsx(path: str):
    """Return a DataFrame of beers from an Alko .xlsx file"""
    # Read excel file into a DataFrame
    df = pd.read_excel(path, engine="openpyxl")
    # Drop first two rows of the Excel since they're not relevant
    df = df.drop([0, 1])
    # Assign the new first row as the column names
    df.columns = df.iloc[0]
    # Pick only beers from the list
    df = df[df['Tyyppi'] == 'oluet']
    # Reset DataFrame index
    df = df.reset_index()
    return df
