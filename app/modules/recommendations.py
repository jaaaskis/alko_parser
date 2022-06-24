import pandas as pd
from .utils import get_rounded_float


def get_random_beer_recommendations(beers: pd.DataFrame, amount: int):
    return beers.sample(amount)


def get_random_beer_recommendations_with_budget(beers: pd.DataFrame, amount: int, budget: float):
    spent_money = 0
    ids = []
    for idx in beers.sample(frac=1.0).index:
        # We have the wanted amount of beers
        if(len(ids) == amount):
            break
        id = beers['Numero'][idx]
        # Parse the price into a float for arithmetics
        price = float(beers['Hinta'][idx])

        # Have a max price for beers to return the wanted amount of beers
        if(price > budget/amount):
            continue

        currently_within_budget = spent_money <= budget
        does_not_go_over_budget = ((spent_money + price) <= budget)

        if(currently_within_budget & does_not_go_over_budget):
            spent_money = spent_money + price
            ids.append(id)
        else:
            continue

    return {
        "beers": beers[beers['Numero'].isin(ids)].to_json(),
        "spare_change": get_rounded_float(budget - spent_money)
    }


# beer_df = get_beers_from_alko_xlsx(path_to_file)
# tastings = get_random_beer_recommendations_with_budget(beer_df, 6, 50)
# urls = get_alko_urls(tastings["beers"])
# print('try these beers')
# for url in urls:
#     print(url)
