from ...database.conecDB import conectarDB
from ..marcas.marcas_model import MarcaModel as Marca
from ..proveedores.proveedores_model import ProveedorModel as Proveedor


class ArticuloModel:
    def __init__(
        self,
        id: int = 0,
        descripcion: str = "",
        precio: float = 0.0,
        stock: int = 0,
        marca: Marca = None,
        proveedor: Proveedor = None,
    ):
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.marca = marca
        self.proveedor = proveedor

    def serializar(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "stock": self.stock,
            "marca": self.marca.serializar(),
            "proveedor": self.proveedor.serializar(),
        }

    def deserializar(data: dict):
        return ArticuloModel(
            id=data["id"],
            descripcion=data["descripcion"],
            precio=data["precio"],
            stock=data["stock"],
            marca=data['marca'],
            proveedor=data["proveedor"],
        )

    def obtener_articulos():
        conn = conectarDB.conectar()
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM ARTICULOS")
                articulos = []
                arts = cursor.fetchall()
                if len(arts) > 0:
                    for articulo in arts:
                        articulos.append(articulo)
                    return articulos
                return False
        except Exception as ex:
            return {"message": f"Ha ocurrido un error {ex}"}
        finally:
            conn.close()

    def obtener_articulo(self):
        conn = conectarDB.conectar()
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM ARTICULOS WHERE id=%s", (self.id,))
                articulo = cursor.fetchone()
                if articulo:
                    return articulo
                return False
        except Exception as ex:
            return {"message": f"Ha ocurrido un error {ex}"}
        finally:
            conn.close()

    def crear_articulo(self):
        conn = conectarDB.conectar()
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(
                    "INSERT INTO ARTICULOS (descripcion,precio,stock,marca_id,proveedor_id) VALUES (%s,%s,%s,%s,%s)",
                    (
                        self.descripcion,
                        self.precio,
                        self.stock,
                        self.marca.id,
                        self.proveedor.id,
                    ),
                )
                conn.commit()
                cursor.execute("INSERT INTO ARTICULOS_CATEGORIAS (articulo_id,categoria_id) values (%s,%s)",(self.id,se))
                id = cursor.lastrowid
                cursor.execute("SELECT * FROM ARTICULOS WHERE id=%s", (id,))
                articulo_creado = cursor.fetchone()
                if articulo_creado:
                    return articulo_creado
                else:
                    return False
        except Exception as ex:
            return {"message": f"Ha ocurrido un error {ex}"}
        finally:
            conn.close()
