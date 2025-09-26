from .marcas_model import MarcaModel


class MarcaController:
    @staticmethod
    def obtener_marcas():
        marcas = MarcaModel.obtener_marcas()
        return marcas

    @staticmethod
    def obtener_marca(id):
        marca = MarcaModel(id=id).obtener_marca()
        return marca

    @staticmethod
    def crear_marca(data: dict):
        marca = MarcaModel(nombre=data["nombre"])
        result = marca.crear_marca()
        return result

    @staticmethod
    def modificar_marca(data: dict):
        marca = MarcaModel(id=data["id"], nombre=data["nombre"])
        result = marca.modificar_marca()
        return result

    @staticmethod
    def eliminar_marca(id):
        marca = MarcaModel(id=id)
        result = marca.eliminar_marca()
        return result
