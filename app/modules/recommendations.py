import pandas as pd
from .utils import get_rounded_float


def get_random_beer_recommendations(beers: pd.DataFrame, amount: int):
    return beers.sample(amount)


def get_random_beer_recommendations_with_budget(beers: pd.DataFrame, amount: int, budget: float):
    # Randomly select beers that fall within the budget
    # Does not take into account left amount after selecting a product
    max_price = budget/amount
    mask = beers['Hinta'] <= max_price
    selected = beers[mask].sample(amount).reset_index()
    spent_money = selected["Hinta"].sum()
    print(selected)
    return {
        # TODO: parse into proper dictionaries
        "beers": selected['Nimi'].to_json(),
        "spare_change": get_rounded_float(budget - spent_money)
    }
