import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()


class conectarDB:
    def conectar():
        try:
            conn = mysql.connector.connect(
                database=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT"),
            )
            print("Conectado correctamente a la base de datos")
            return conn

        except Exception as ex:
            print(f"Error al conectar con la base de datos {ex}")
