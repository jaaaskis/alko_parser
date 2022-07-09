import psycopg2

from app.modules.database.queries import (
    get_all_manufacturers_query,
    get_all_products_query,
    get_all_stores_query,
    get_all_test_query,
)
from app.modules.database.utils import get_query_by_type

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


def get_record_by_id_and_type(id: int, type: str):
    try:
        # Connect to an existing database
        connection = psycopg2.connect(DATABASE_CONNECTION, sslmode="require")
        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Defining the query
        query = get_query_by_type(id, type)
        # Executing a SQL query
        cursor.execute(query)
        # Fetch result
        record = cursor.fetchone()
        return record
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()


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
        return record
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()


def get_all_manufacturers():
    try:
        # Connect to an existing database
        connection = psycopg2.connect(DATABASE_CONNECTION, sslmode="require")
        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Defining the query
        query = get_all_manufacturers_query()
        # Executing a SQL query
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


def get_all_stores():
    try:
        # Connect to an existing database
        connection = psycopg2.connect(DATABASE_CONNECTION, sslmode="require")
        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Defining the query
        query = get_all_stores_query()
        # Executing a SQL query
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
