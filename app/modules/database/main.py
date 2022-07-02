import psycopg2

from app.modules.database.queries import get_all_test
from .constants import database_name, database_user


def test_connection():
    # Connect to an existing database
    connection = psycopg2.connect(f"dbname={database_name} user={database_user}")

    # Open a cursor to perform database operations
    cursor = connection.cursor()

    # Execute query
    query = get_all_test()
    print(query)
    cursor.execute(query)
    result = cursor.fetchone()
    print("result", result)

    # Close communication with the database
    cursor.close()
    connection.close()
