import mysql.connector
from dotenv import load_dotenv, find_dotenv
import os

dotenv_path = find_dotenv()
print("Cargando .env desde:", dotenv_path)
load_dotenv(dotenv_path, override=True)

class conectarDB:
    @staticmethod
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

    @staticmethod
    def obtener(sql: str, params: tuple = ()):
        cxn = conectarDB.conectar()
        try:
            with cxn.cursor(dictionary=True) as cursor:
                print(params)
                cursor.execute(sql, params)
                result = cursor.fetchall()

                return result if result else False
        except Exception as exc:
            print(f"error {str(exc)}")
        finally:
            cxn.close()

    @staticmethod
    def registrar(sql: str, params=None):
        cxn = conectarDB.conectar()
        try:
            with cxn.cursor(dictionary=True) as cursor:
                print(params)
                cursor.execute(sql, params or ())
                cxn.commit()
                if cursor.lastrowid:
                    result = cursor.lastrowid
                else:
                    result = cursor.rowcount
            return result
        except Exception as exc:
            print(f"error {str(exc)}")
        finally:
            cxn.close()
