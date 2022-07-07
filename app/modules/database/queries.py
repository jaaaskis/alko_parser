def get_manufacturer_by_id_query(id: int):
    return 'SELECT * FROM "Manufacturers" WHERE id = {id}'.format(id=id)


def get_product_by_id_query(id: int):
    return 'SELECT name, abv FROM "Products" WHERE id = {id}'.format(id=id)


def get_store_by_id_query(id: int):
    return 'SELECT name, address FROM "Stores" WHERE id = {id}'.format(id=id)


def get_all_test_query():
    return 'SELECT * FROM "Manufacturers" LIMIT 10'


def get_all_products_query():
    return 'SELECT * FROM "Products"'


def get_all_manufacturers_query():
    return 'SELECT * FROM "Manufacturers"'


def get_all_stores_query():
    return 'SELECT * FROM "Stores"'


def add_manufacturer_query(name: str, country: str):
    return "INSERT INTO \"Manufacturers\" (name, country) VALUES ('{name}', '{country}')".format(
        name=name, country=country
    )


def add_store_query(name: str, address: str):
    return (
        "INSERT INTO \"Stores\" (name, address) VALUES ('{name}', '{address}')".format(
            name=name, address=address
        )
    )
