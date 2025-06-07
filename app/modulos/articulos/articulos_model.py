from ...database.conecDB import conectarDB
from ..marcas.marcas_model import MarcaModel as Marca
from ..proveedores.proveedores_model import ProveedorModel as Proveedor
from ..categorias.categorias_model import CategoriaModel as Categoria


class ArticuloModel:
    def __init__(
        self,
        id: int = 0,
        descripcion: str = "",
        precio: float = 0.0,
        stock: int = 0,
        marca: Marca = None,
        proveedor: Proveedor = None,
        categorias: list[Categoria] = None,
    ):
        self.id = id
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.marca = marca
        self.proveedor = proveedor
        self.categorias = categorias

    def serializar(self):
        return {
            "id": self.id,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "stock": self.stock,
            "marca": self.marca.serializar(),
            "proveedor": self.proveedor.serializar(),
            "categorias": self.categorias,
        }

    @staticmethod
    def deserializar(data: dict):
        return ArticuloModel(
            id=data["id"],
            descripcion=data["descripcion"],
            precio=data["precio"],
            stock=data["stock"],
            marca=data["marca"],
            proveedor=data["proveedor"],
            categorias=data["categorias"],
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
                        cursor.execute(
                            "SELECT categoria_id FROM ARTICULOS_CATEGORIAS WHERE articulo_id = %s",
                            (articulo["id"],),
                        )
                        # Obtengo todas las categorias
                        categorias = cursor.fetchall()
                        # Obtengo la Marca
                        marca = Marca(articulo["marca_id"]).obtener_marca()
                        # Obtengo el proveedor
                        proveedor = Proveedor(
                            articulo["proveedor_id"]
                        ).obtener_proveedor()
                        # Agrego la Marca al articulo

                        articulo["marca"] = marca
                        # Agrego el Proveedor al articulo
                        articulo["proveedor"] = proveedor
                        del articulo["marca_id"]
                        del articulo["proveedor_id"]

                        for cat in categorias:
                            categoria = Categoria(
                                cat["categoria_id"]
                            ).obtener_categoria()
                            articulo["categorias"] = categoria
                        articulos.append(articulo)
                    return articulos
                return False
        except Exception as ex:
            return {"message": f"Ha ocurrido un error {ex}"}
        finally:
            conn.close()

    def obtener_articulo(self):
        conn = conectarDB.conectar()
        print(self.id)
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM ARTICULOS WHERE id=%s", (self.id,))
                articulo = cursor.fetchone()
                cursor.execute(
                    "SELECT * FROM ARTICULOS_CATEGORIAS WHERE articulo_id=%s",(self.id,)
                )
                indices_categorias = cursor.fetchall()
                categorias = []
                for categoria in indices_categorias:
                    categoria = Categoria(id=categoria["categoria_id"]).obtener_categoria()
                    categorias.append(categoria)
                marca = Marca(articulo["marca_id"]).obtener_marca()
                proveedor = Proveedor(articulo["proveedor_id"]).obtener_proveedor()
                del articulo["marca_id"]
                del articulo["proveedor_id"]
                articulo["marca"]=marca
                articulo["proveedor"]=proveedor
                articulo["categorias"] = categorias
                if articulo:
                    return articulo

        except Exception as ex:
            return {"message": f"Ha ocurrido un error {ex}"}
        finally:
            conn.close()

    def crear_articulo(self):
        conn = conectarDB.conectar()
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(
                    "INSERT INTO ARTICULOS (descripcion, precio, stock, marca_id, proveedor_id) VALUES (%s, %s, %s, %s, %s)",
                    (
                        self.descripcion,
                        self.precio,
                        self.stock,
                        self.marca.id,
                        self.proveedor.id,
                    ),
                )
                conn.commit()
                articulo_id = cursor.lastrowid

                for categoria in self.categorias:
                    cursor.execute(
                        "INSERT INTO ARTICULOS_CATEGORIAS (articulo_id, categoria_id) VALUES (%s, %s)",
                        (articulo_id, categoria),
                    )

                conn.commit()
                cursor.execute("SELECT * FROM ARTICULOS WHERE id=%s", (articulo_id,))
                articulo_creado = cursor.fetchone()
                if articulo_creado:
                    return articulo_creado
                else:
                    return False
        except Exception as ex:
            return {"message": f"Ha ocurrido un error: {ex}"}
        finally:
            conn.close()

    def modificar_articulo(self):
        conn = conectarDB.conectar()
        try:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(
                    "   UPDATE ARTICULOS SET descripcion=%s, precio=%s, stock=%s, marca_id=%s, proveedor_id=%s WHERE id=%s",
                    (
                        self.descripcion,
                        self.precio,
                        self.stock,
                        self.marca.id,
                        self.proveedor.id,
                        self.id,
                    ),
                )
                conn.commit()
                for categoria in self.categorias:
                    cursor.execute(
                        "UPDATE ARTICULOS_CATEGORIAS SET categoria_id=%s WHERE categoria_id= %s",
                        (
                            categoria,
                            self.id,
                        ),
                    )

                conn.commit()
                cursor.execute("SELECT * FROM ARTICULOS WHERE id=%s", (self.id,))
                articulo_creado = cursor.fetchone()
                if articulo_creado:
                    return articulo_creado
                else:
                    return False
        except Exception as ex:
            return {"message": f"Ha ocurrido un error: {ex}"}
        finally:
            conn.close()
