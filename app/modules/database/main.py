import psycopg2

from app.modules.database.queries import (
    add_store_query,
    get_all_products_query,
    get_all_test_query,
    get_manufacturer_by_id_query,
    get_product_by_id_query,
)
from .constants import DATABASE_CONNECTION


def test_connection():
    try:
        # Connect to an existing database
        connection = psycopg2.connect(DATABASE_CONNECTION, sslmode="require")
        # Open a cursor to perform database operations
        cursor = connection.cursor()
        # Defining the query
        query = get_all_test_query()
        # Execute query
        cursor.execute(query)
        # Fetch result
        record = cursor.fetchall()
        return record
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def get_manufacturer_by_id(id: int):
    try:
        # Connect to an existing database
        connection = psycopg2.connect(DATABASE_CONNECTION, sslmode="require")
        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Defining the query
        query = get_manufacturer_by_id_query(id)
        # Executing a SQL query
        cursor.execute(query)
        # Fetch result
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")
        return record
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def get_product_by_id(id: int):
    try:
        # Connect to an existing database
        connection = psycopg2.connect(DATABASE_CONNECTION, sslmode="require")
        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Defining the query
        query = get_product_by_id_query(id)
        # Executing a SQL query
        cursor.execute(query)
        # Fetch result
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")
        return record
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def get_all_products():
    try:
        # Connect to an existing database
        connection = psycopg2.connect(DATABASE_CONNECTION, sslmode="require")
        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Defining the query
        query = get_all_products_query()
        # Executing a SQL query
        cursor.execute(query)
        # Fetch result
        record = cursor.fetchall()
        print("You are connected to - ", record, "\n")
        return record
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def insert_store(name: str, address: str):
    try:
        # Connect to an existing database
        connection = psycopg2.connect(DATABASE_CONNECTION, sslmode="require")
        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Defining the query
        query = add_store_query(name, address)
        # Executing a SQL query
        cursor.execute(query)
        # Commit changes
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
