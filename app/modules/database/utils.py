from app.modules.database.queries import (
    get_manufacturer_by_id_query,
    get_product_by_id_query,
    get_store_by_id_query,
)


def get_query_by_type(id: int, type: str):
    if type == "product":
        return get_product_by_id_query(id)
    if type == "manufacturer":
        return get_manufacturer_by_id_query(id)
    if type == "store":
        return get_store_by_id_query(id)
    raise Exception("Unknown type", type)
