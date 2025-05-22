from .categorias_model import CategoriaModel


class CategoriaController:
    @staticmethod
    def obtener_categorias():
        categorias = CategoriaModel.obtener_categorias()
        return categorias

    @staticmethod
    def obtener_categoria(id):
        categoria = CategoriaModel(id=id).obtener_categoria()
        p
        return categoria

    @staticmethod
    def crear_categoria(data: dict):
        categoria = CategoriaModel(nombre=data["nombre"])
        result = categoria.crear_categoria()
        return result

    @staticmethod
    def modificar_categoria(data: dict):
        categoria = CategoriaModel(id=data["id"], nombre=data["nombre"])
        result = categoria.modificar_categoria()
        return result

    @staticmethod
    def eliminar_categoria(id):
        categoria = CategoriaModel(id=id)
        result = categoria.eliminar_categoria()
        return result
