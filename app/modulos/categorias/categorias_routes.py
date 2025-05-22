from .categorias_controller import CategoriaController
from flask import Blueprint, jsonify, request

categoria_bp = Blueprint("categoria", __name__)


@categoria_bp.route("/categorias")
def obtener_categorias():
    try:
        categorias = CategoriaController.obtener_categorias()
        if len(categorias) > 0:
            return jsonify(categorias), 200
        else:
            return jsonify({"message": "No se encontraron categorias"})
    except Exception as ex:
        return jsonify({"mnessage": "Ha ocurrido un error {ex}"})


@categoria_bp.route("/categoria/<int:id>")
def obtener_categoria(id):
    try:
        categoria = CategoriaController.obtener_categoria(id)
        if categoria_bp:
            return jsonify(categoria), 200
        else:
            return jsonify({"message": "No se encontro la categoria"})
    except Exception as ex:
        return jsonify({"mnessage": f"Ha ocurrido un error {ex}"})


@categoria_bp.route("/categoria", methods=["POST"])
def crear_categoria():
    try:
        data = request.get_json()
        result = CategoriaController.crear_categoria(data)
        if result:
            return jsonify(result), 201
    except Exception as ex:
        return jsonify({"message": f"Ha ocurrido un error {ex}"}), 500


@categoria_bp.route("/categoria/<int:id>", methods=["PUT"])
def modifica_categoria(id):
    try:
        data = request.get_json()
        data["id"] = id
        result = CategoriaController.modificar_categoria(data)
        if result != False:
            return jsonify(result), 201
        else:
            return {"message": f"No se encontro la categoria con el id: {id}"}, 404
    except Exception as ex:
        return jsonify({"message": f"Ha ocurrido un error {ex}"}), 500


@categoria_bp.route("/categoria/<int:id>", methods=["DELETE"])
def eliminar_categoria(id):
    try:
        result = CategoriaController.eliminar_categoria(id)
        if result != False:
            return jsonify(result), 201
        else:
            return {"message": f"No se encontro la categoria con el id: {id}"}, 404
    except Exception as ex:
        return jsonify({"message": f"Ha ocurrido un error {ex}"}), 500
