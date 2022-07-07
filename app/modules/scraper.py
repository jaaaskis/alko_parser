from bs4 import BeautifulSoup
from requests import get

from app.modules.constants import ALKO_STORES_URL


def scrape_alko_stores():
    result = get(ALKO_STORES_URL).content
    soup = BeautifulSoup(result, "html.parser")

    blocks = soup.find_all(
        class_="store-list-item row text-left relative padding-1 outletType_myymalat"
    )

    address_list = []

    for block in blocks:
        name = block.find(class_="name").text
        address = ""
        address_strings = block.find_all(class_="address-data")
        for string in address_strings:
            address = address + string.text
        address = address.replace("\n", "")
        address_list.append([name, address])

    return address_list
