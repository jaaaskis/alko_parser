def get_manufacturer_by_id_query(id: int):
    return 'SELECT * FROM "Manufacturers" WHERE id = {id}'.format(id=id)


def get_product_by_id_query(id: int):
    fields = "p.name as name, pt.type as type, pt.sub_type as sub_type, m.name as Manufacturer, m.country as Country, p.abv as ABV"
    tables = '"Products" p LEFT JOIN "Manufacturers" AS m ON p.manufacturer_id = m.id LEFT JOIN "ProductTypes" AS pt ON p.type_id = pt.id'
    query = f"SELECT {fields} " f"FROM {tables} " f"WHERE p.id = {id}"
    return query


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
