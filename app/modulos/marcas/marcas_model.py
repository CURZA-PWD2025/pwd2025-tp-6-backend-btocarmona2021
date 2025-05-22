from ...database.conecDB import conectarDB


class MarcaModel:
    def __init__(self, id: int = 0, nombre: str = ""):
        self.id = id
        self.nombre = nombre

    def serializar(self):
        return {"id": self.id, "nombre": self.nombre}

    @staticmethod
    def deserializar(data: dict):
        return MarcaModel(id=data["id"], nombre=data["nombre"])

    @staticmethod
    def obtener_marcas():
        conn = conectarDB.conectar()
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM MARCAS")
                marcas = []
                markas = cursor.fetchall()
                if len(markas) > 0:
                    for marca in markas:
                        marcas.append(marca)
                    return marcas
                return False
        except Exception as ex:
            return {"message": f"No se encontraron marcas {ex}"}
        finally:
            conn.close()

    def obtener_marca(self):
        conn = conectarDB.conectar()
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM MARCAS WHERE id=%s", (self.id,))
                marca = cursor.fetchone()
                if marca:
                    return marca
                return False

        except Exception as ex:
            return {"message": f"No se encontro la marca {ex}"}
        finally:
            conn.close()

    def crear_marca(self):
        conn = conectarDB.conectar()
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(
                    "INSERT INTO MARCAS (nombre) values (%s)", (self.nombre,)
                )
                conn.commit()
                id = cursor.lastrowid
                cursor.execute("SELECT * FROM MARCAS WHERE id=%s", (id,))
                marca = cursor.fetchone()
                if marca:
                    return marca
                return False
        except Exception as ex:
            return {"message": f"No se creo la marca {ex}"}
        finally:
            conn.close()

    def modificar_marca(self):
        conn = conectarDB.conectar()
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(
                    "UPDATE MARCAS SET nombre=%s WHERE id=%s",
                    (self.nombre, self.id),
                )
                conn.commit()
                cursor.execute("SELECT * FROM MARCAS WHERE id=%s", (self.id,))
                marca = cursor.fetchone()
                if marca:
                    return marca
                return False
        except Exception as ex:
            return {"message": f"No se encontro la marca {ex}"}
        finally:
            conn.close()

    def eliminar_marca(self):
        conn = conectarDB.conectar()
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM MARCAS WHERE id=%s", (self.id,))
                marca = cursor.fetchone()
                cursor.execute("DELETE FROM MARCAS WHERE id=%s", (self.id,))
                conn.commit()
                if marca:
                    return {
                        "message": f"marca eliminada correctamente: {marca}"
                    }
                return False
        except Exception as ex:
            return {"message": f"Ha ocurrido un error {ex}"}
        finally:
            conn.close()
