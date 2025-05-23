from ..articulos.articulos_model import ArticuloModel
from ..marcas.marcas_model import MarcaModel as Marca
from ..proveedores.proveedores_model import ProveedorModel as Proveedor 
from ..categorias.categorias_model import CategoriaModel as Categoria


class ArticuloController:

    @staticmethod
    def obtener_articulos():
        articulos = ArticuloModel.obtener_articulos()
        return articulos

    @staticmethod
    def obtener_articulo(id):
        articulo = ArticuloModel(id=id).obtener_articulo()
        return articulo

    @staticmethod
    def crear_articulo(data:dict):
        mark = Marca(id=data["marca_id"]).obtener_marca()
        prov = Proveedor(id=data["proveedor_id"]).obtener_proveedor()
        marca = Marca.deserializar(mark)
        proveedor = Proveedor.deserializar(prov)
        # cat =  Categoria(id=data["categoria_id"]).obtener_categoria()
        # categoria = Categoria.deserializar(cat)

        articulo = ArticuloModel(descripcion=data["descripcion"],precio=data["precio"],stock=data["stock"],marca=marca,proveedor=proveedor)
        articulo["categoria_id"]= data["categoria_id"]
        print(articulo)
        result = articulo.crear_articulo()
        return result