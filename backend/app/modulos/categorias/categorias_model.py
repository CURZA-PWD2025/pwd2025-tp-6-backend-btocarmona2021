from ...database.conecDB import conectarDB


class CategoriaModel:
    def __init__(self, id: int = 0, nombre: str = ""):
        self.id = id
        self.nombre = nombre

    def serializar(self):
        return {"id": self.id, "nombre": self.nombre}

    @staticmethod
    def deserializar(data: dict):
        return CategoriaModel(id=data["id"], nombre=data["nombre"])

    @staticmethod
    def obtener_categorias():
        conn = conectarDB.conectar()
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM CATEGORIAS")
                categorias = []
                cats = cursor.fetchall()
                if len(cats) > 0:
                    for categoria in cats:
                        categorias.append(categoria)
                    return categorias
                return False
        except Exception as ex:
            return {"message": f"No se encontraron categorias {ex}"}
        finally:
            conn.close()

    def obtener_categoria(self):
        conn = conectarDB.conectar()
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM CATEGORIAS WHERE id=%s", (self.id,))
                cat = cursor.fetchone()
                if cat:
                    return (cat)
                return (False)

        except Exception as ex:
            return {"message": f"No se encontro la categoria {str(ex)}"}
        finally:
            conn.close()

    def crear_categoria(self):
        conn = conectarDB.conectar()
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(
                    "INSERT INTO CATEGORIAS (nombre) values (%s)", (self.nombre,)
                )

                conn.commit()
                id = cursor.lastrowid
                cursor.execute("SELECT * FROM CATEGORIAS WHERE id=%s", (id,))
                categoria = cursor.fetchone()
                if categoria:
                    return categoria
                return False
        except Exception as ex:
            return {"message": f"No se creo la categoria {str(ex)}"}
        finally:
            conn.close()

    def modificar_categoria(self):
        conn = conectarDB.conectar()
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(
                    "UPDATE CATEGORIAS SET nombre=%s WHERE id=%s",
                    (self.nombre, self.id),
                )
                conn.commit()
                cursor.execute("SELECT * FROM CATEGORIAS WHERE id=%s", (self.id,))
                categoria = cursor.fetchone()
                if categoria:
                    return categoria
                return False
        except Exception as ex:
            return {"message": f"No se encontro la categoria {ex}"}
        finally:
            conn.close()

    def eliminar_categoria(self):
        conn = conectarDB.conectar()
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM CATEGORIAS WHERE id=%s", (self.id,))
                categoria = cursor.fetchone()
                cursor.execute("DELETE FROM CATEGORIAS WHERE id=%s", (self.id,))
                conn.commit()
                if categoria:
                    return {"message":f"categoria eliminada correctamente: {categoria}"}
                return False
        except Exception as ex:
            return {"message": f"Ha ocurrido un error {ex}"}
        finally:
            conn.