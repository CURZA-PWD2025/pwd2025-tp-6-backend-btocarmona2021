from .proveedores_model import ProveedorModel


class ProveedorController:
    @staticmethod
    def obtener_proveedores():
        proveedores = ProveedorModel.obtener_proveedores()
        return proveedores

    @staticmethod
    def obtener_proveedor(id):
        proveedor = ProveedorModel(id=id).obtener_proveedor()
        return proveedor

    @staticmethod
    def crear_proveedor(data: dict):
        proveedor = ProveedorModel(
            nombre=data["nombre"],
            telefono=data["telefono"],
            direccion=data["direccion"],
            email=data["email"],
        )
        result = proveedor.crear_proveedor()
        return result

    @staticmethod
    def modificar_proveedor(data: dict):
        proveedor = ProveedorModel(
            id=data["id"],
            nombre=data["nombre"],
            telefono=data["telefono"],
            direccion=data["direccion"],
            email=data["email"],
        )
        result = proveedor.modificar_proveedor()
        return result

    @staticmethod
    def eliminar_proveedor(id):
        proveedor = ProveedorModel(id=id)
        result = proveedor.eliminar_proveedor()
        return result
