from flask import Flask
from .modulos.categorias.categorias_routes import categoria_bp
from .modulos.marcas.marcas_routes import marca_bp
from .modulos.proveedores.proveedores_routes import proveedor_bp
from .modulos.articulos.articulos_routes import articulo_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(categoria_bp)
    app.register_blueprint(marca_bp)
    app.register_blueprint(proveedor_bp)
    app.register_blueprint(articulo_bp)
    @app.route("/")
    def home():
        return "<h1>Home</h1>"

    return app
