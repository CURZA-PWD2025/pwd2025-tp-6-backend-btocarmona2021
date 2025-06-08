import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()
database_name = os.getenv("DB_NAME")

database_config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "port": os.getenv("DB_PORT"),
    "raise_on_warnings": True,
    "database": database_name,
}

DROPPED_TB = {}

DROPPED_TB["ARTICULOS_CATEGORIAS"] = "DROP TABLE IF EXISTS ARTICULOS_CATEGORIAS;"
DROPPED_TB["ARTICULOS"] = "DROP TABLE IF EXISTS ARTICULOS;"
DROPPED_TB["PROVEEDORES"] = "DROP TABLE IF EXISTS PROVEEDORES;"
DROPPED_TB["MARCAS"] = "DROP TABLE IF EXISTS MARCAS;"
DROPPED_TB["CATEGORIAS"] = "DROP TABLE IF EXISTS CATEGORIAS;"


def rollback_db():
    cxn = mysql.connector.connect(**database_config)
    cursor = cxn.cursor()
    for table in DROPPED_TB:
        print(f"Dropped table: {table}", end=" ")
        try:
            cursor.execute(DROPPED_TB[table])
            print("ok")
            cxn.commit()
        except Error as e:
            print(f"{e}")

    cursor.close()
    cxn.close()


rollback_db()
