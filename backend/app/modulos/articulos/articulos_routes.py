from ..articulos.articulos_controller import ArticuloController
from flask import request, Blueprint, jsonify

articulo_bp = Blueprint("articulo", __name__)


@articulo_bp.route("/articulos")
def obtener_articulos():
    try:
        articulos = ArticuloController.obtener_articulos()
        return jsonify(articulos),200
    except Exception as ex:
        return jsonify({"mnessage": f"Ha ocurrido un error {ex}"}),500


@articulo_bp.route("/articulo/<int:id>")
def obtener_articulo(id):
    try:
        articulos = ArticuloController.obtener_articulo(id)
        return jsonify(articulos),200
    except Exception as ex:
        return jsonify({"mnessage": f"Ha ocurrido un error {ex}"}),500


@articulo_bp.route("/articulo", methods=["POST"])
def crear_articulo():
    try:
        data = request.get_json()
        articulo = ArticuloController.crear_articulo(data)
        return jsonify(articulo),201
    except Exception as ex:
        return jsonify({"mnessage": f"Ha ocurrido un error {ex}"}),500


@articulo_bp.route("/articulo/<int:id>", methods=["PUT"])
def modificar_articulo(id):
    try:
        data = request.get_json()
        data["id"]=id
        articulo = ArticuloController.modificar_articulo(data=data)
        return jsonify(articulo),200
    except Exception as ex:
        return jsonify({"mnessage": f"Ha ocurrido un error {ex}"}),500


@articulo_bp.route("/articulo/<int:id>", methods=["DELETE"])
def eliminar_articulo(id):
    try:
        articulo = ArticuloController.eliminar_articulo(id)
        return jsonify(articulo),200
    except Exception as ex:
        return jsonify({"mnessage": f"Ha ocurrido un error {ex}"}),500
