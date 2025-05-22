from ...database.conecDB import conectarDB


class ProveedorModel:

    def __init__(self, id:int=0, nombre:str="", telefono:int=0, direccion:str="", email:str=""):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.email = email

    def serializar(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "email": self.email,
        }

    @staticmethod
    def deserializar(data: dict):
        return ProveedorModel(
            id=data["id"],
            nombre=data["nombre"],
            telefono=data["telefono"],
            direccion=data["direccion"],
            email=data["email"],
        )

    def obtener_proveedores():
        conn = conectarDB.conectar()
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM PROVEEDORES")
                proveedores = []
                provees = cursor.fetchall()
                if len(provees) > 0:
                    for proveedor in provees:
                        proveedores.append(proveedor)
                    return proveedores
                return False
        except Exception as ex:
            return {"message": f"No se encontraron marcas {ex}"}
        finally:
            conn.close()

    def obtener_proveedor(self):
        print(self.id)
        conn = conectarDB.conectar()
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM PROVEEDORES WHERE id=%s", (self.id,))
                proveedor = cursor.fetchone()
                if proveedor:
                    print(proveedor)
                    return proveedor
                return False
        except Exception as ex:
            return {"message": f"Ha ocurrido un error {ex}"}
        finally:
            conn.close()

    def crear_proveedor(self):
        conn = conectarDB.conectar()
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(
                    "INSERT INTO PROVEEDORES (nombre,telefono,direccion,email) values(%s,%s,%s,%s)",
                    (self.nombre, self.telefono, self.direccion, self.email),
                )
                conn.commit()
                id = cursor.lastrowid
                cursor.execute("SELECT * FROM PROVEEDORES WHERE id=%s", (id,))
                proveedor = cursor.fetchone()
                if proveedor:
                    return proveedor
                return False
        except Exception as ex:
            return {"message": f"Ha ocurrido un error {ex}"}
        finally:
            conn.close()

    def modificar_proveedor(self):
        conn = conectarDB.conectar()
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(
                    "UPDATE PROVEEDORES SET nombre=%s,telefono=%s,direccion=%s,email=%s WHERE id=%s",
                    (self.nombre, self.telefono, self.direccion, self.email, self.id),
                )
                conn.commit()
                cursor.execute("SELECT * FROM PROVEEDORES WHERE id=%s", (self.id,))
                proveedor = cursor.fetchone()
                if proveedor:
                    return proveedor
                return False
        except Exception as ex:
            return {"message": f"Ha ocurrido un error {ex}"}
        finally:
            conn.close()

    def eliminar_proveedor(self):
        conn = conectarDB.conectar()
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM PROVEEDORES WHERE id=%s", (self.id,))
                proveedor = cursor.fetchone()
                cursor.execute("DELETE FROM PROVEEDORES WHERE id=%s", (self.id,))
                conn.commit()
                if proveedor:
                    return {
                        "message": f"proveedor eliminado correctamente: {proveedor}"
                    }
                return False
        except Exception as ex:
            return {"message": f"Ha ocurrido un error {ex}"}
        finally:
            conn.close()
