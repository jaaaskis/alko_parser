import pandas as pd
from .utils import get_rounded_float


def get_random_beer_recommendations(beers: pd.DataFrame, amount: int):
    return beers.sample(amount)


def get_random_beer_recommendations_with_budget(
    beers: pd.DataFrame, amount: int, budget: float
):
    # Randomly select beers that fall within the budget
    # Does not take into account left amount after selecting a product
    max_price = budget / amount
    mask = beers["Hinta"] <= max_price
    selected = beers[mask].sample(amount).reset_index()
    spent_money = selected["Hinta"].sum()
    print(selected.columns)
    return {
        # TODO: parse into proper dictionaries
        "beers": selected["Nimi"],
        "prices": selected["Hinta"],
        "beer_type": selected["Oluttyyppi"],
        "abv": selected["Alkoholi-%"],
        "total": get_rounded_float(spent_money),
        "spare_change": get_rounded_float(budget - spent_money),
    }
