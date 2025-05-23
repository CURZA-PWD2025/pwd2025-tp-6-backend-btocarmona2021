from ..articulos.articulos_controller import ArticuloController
from flask import request, Blueprint, jsonify

articulo_bp = Blueprint("articulo", __name__)


@articulo_bp.route("/articulos")
def obtener_articulos():
    articulos = ArticuloController.obtener_articulos()
    return jsonify(articulos)


@articulo_bp.route("/articulo/<int:id>")
def obtener_articulo(id):
    articulos = ArticuloController.obtener_articulo(id)
    return jsonify(articulos)


@articulo_bp.route("/articulo", methods=["POST"])
def crear_articulo():
    data = request.get_json()
    articulo = ArticuloController.crear_articulo(data)
    return jsonify(articulo)
