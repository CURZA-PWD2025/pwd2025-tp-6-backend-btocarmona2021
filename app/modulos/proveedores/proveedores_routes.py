from .proveedores_controller import ProveedorController
from flask import Blueprint, jsonify, request

proveedor_bp = Blueprint("proveedor", __name__)


@proveedor_bp.route("/proveedores")
def obtener_proveedores():
    try:
        proveedores = ProveedorController.obtener_proveedores()
        if len(proveedores) > 0:
            return jsonify(proveedores), 200
        else:
            return jsonify({"message": "No se encontraron proveedores"})
    except Exception as ex:
        return jsonify({"message": f"Ha ocurrido un error {ex}"})


@proveedor_bp.route("/proveedor/<int:id>")
def obtener_proveedor(id):
    try:
        proveedor = ProveedorController.obtener_proveedor(id)

        if proveedor:
            return jsonify(proveedor), 200
        else:
            return jsonify({"message": "No se encontro el proveedor"}),404
    except Exception as ex:
        return jsonify({"message": f"Ha ocurrido un error {ex}"})


@proveedor_bp.route("/proveedor", methods=["POST"])
def crear_proveedor():
    try:
        data = request.get_json()
        result = ProveedorController.crear_proveedor(data)
        if result:
            return jsonify(result), 201
    except Exception as ex:
        return jsonify({"message": f"Ha ocurrido un error {ex}"}), 500


@proveedor_bp.route("/proveedor/<int:id>", methods=["PUT"])
def modificar_proveedor(id):
    try:
        data = request.get_json()
        data["id"] = id
        result = ProveedorController.modificar_proveedor(data)
        if result != False:
            return jsonify(result), 200
        else:
            return {"message": f"No se encontro el proveedor con el id: {id}"}, 404
    except Exception as ex:
        return jsonify({"message": f"Ha ocurrido un error {ex}"}), 500


@proveedor_bp.route("/proveedor/<int:id>", methods=["DELETE"])
def eliminar_proveedor(id):
    try:
        result = ProveedorController.eliminar_proveedor(id)
        if result != False:
            return jsonify(result), 201
        else:
            return {"message": f"No se encontro la proveedor con el id: {id}"}, 404
    except Exception as ex:
        return jsonify({"message": f"Ha ocurrido un error {ex}"}), 500
