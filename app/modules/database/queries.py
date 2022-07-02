def get_manufacturer_by_id(id: int):
    return 'SELECT * FROM "Manufacturers" WHERE id = {id}'.format(id=id)


def get_all_test():
    return 'SELECT * FROM "Manufacturers" LIMIT 10'
