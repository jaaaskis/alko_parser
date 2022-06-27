from math import ceil
import os
import pandas as pd
from .constants import alko_store_inventory_url_fi, alko_store_product_url_fi, path_to_beers, path_to_whole_inventory, alko_store_products_fi


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


def trim_alko_inventory_head(df: pd.DataFrame):
    # Drop first two rows of the Excel since they're not relevant
    df = df.drop([0, 1])
    # Assign the new first row as the column names
    df.columns = df.iloc[0]
    # Pick only beers from the list
    df = df[df['Tyyppi'] == 'oluet']
    # Reset DataFrame index
    df = df.reset_index()
    # Convert price column to numbers
    df = df.astype({"Hinta": float})
    return df


def get_or_create_beers_dataframe():
    # Check if filtered excel exists
    beer_df = os.path.isfile(path_to_beers)
    if(beer_df):
        df = pd.read_excel(path_to_beers, engine="openpyxl")
        return df

    # If no filtered excel check if inventory excel exists
    inventory_df = os.path.isfile(path_to_whole_inventory)
    if(inventory_df):
        df = pd.read_excel(path_to_whole_inventory, engine="openpyxl")
        df = trim_alko_inventory_head(df)
        # Write excel to file
        print('Writing beers.xlsx ...')
        df.to_excel(path_to_beers)
        return df

    # If no excel fetch the latest from Alko
    try:
        df = pd.read_excel(alko_store_products_fi, engine="openpyxl")
        # Write whole inventory
        print('Writing whole inventory .xlsx ...')
        df.to_excel(path_to_whole_inventory)

        beers = trim_alko_inventory_head(df)
        # Write beers.xlsx
        print('Writing beers.xlsx ...')
        beers.to_excel(path_to_beers)

        return beers
    except:
        print('Something went wrong!')
