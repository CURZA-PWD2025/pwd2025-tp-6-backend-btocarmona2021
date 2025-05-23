from .marcas_controller import MarcaController
from flask import Blueprint, jsonify, request

marca_bp = Blueprint("marca", __name__)


@marca_bp.route("/marcas")
def obtener_marcas():
    try:
        marcas = MarcaController.obtener_marcas()
        if len(marcas) > 0:
            return jsonify(marcas), 200
        else:
            return jsonify({"message": "No se encontraron marcas"})
    except Exception as ex:
        return jsonify({"mnessage": "Ha ocurrido un error {ex}"})


@marca_bp.route("/marca/<int:id>")
def obtener_marca(id):
    try:
        marca = MarcaController.obtener_marca(id)
        if marca:
            return jsonify(marca), 200
        else:
            return jsonify({"message": "No se encontro la marca"})
    except Exception as ex:
        return jsonify({"mnessage": f"Ha ocurrido un error {ex}"})


@marca_bp.route("/marca", methods=["POST"])
def crear_marca():
    try:
        data = request.get_json()
        result = MarcaController.crear_marca(data)
        if result:
            return jsonify(result), 201
    except Exception as ex:
        print(type(ex).__name__)
        return jsonify({"message": f"Ha ocurrido un error {ex}"}), 500


@marca_bp.route("/marca/<int:id>", methods=["PUT"])
def modificar_marca(id):
    try:
        data = request.get_json()
        data["id"] = id
        result = MarcaController.modificar_marca(data)
        if result != False:
            return jsonify(result), 201
        else:
            return {"message": f"No se encontro la marca con el id: {id}"}, 404
    except Exception as ex:
        return jsonify({"message": f"Ha ocurrido un error {ex}"}), 500


@marca_bp.route("/marca/<int:id>", methods=["DELETE"])
def eliminar_marca(id):
    try:
        result = MarcaController.eliminar_marca(id)
        if result != False:
            return jsonify(result), 200
        else:
            return {"message": f"No se encontro la marca con el id: {id}"}, 404
    except Exception as ex:
        return jsonify({"message": f"Ha ocurrido un error {ex}"}), 500
