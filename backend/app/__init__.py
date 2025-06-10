from flask import Flask
from .modulos.categorias.categorias_routes import categoria_bp
from .modulos.marcas.marcas_routes import marca_bp
from .modulos.proveedores.proveedores_routes import proveedor_bp
from .modulos.articulos.articulos_routes import articulo_bp
from flask_cors import CORS
def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(categoria_bp, url_prefix="/api/v1")
    app.register_blueprint(marca_bp, url_prefix="/api/v1")
    app.register_blueprint(proveedor_bp, url_prefix="/api/v1")
    app.register_blueprint(articulo_bp, url_prefix="/api/v1")
    @app.route("/")
    def home():
        return "<h1>Home</h1><h3>Todas las rutas estan bajo /api/v1/</h3>"

    return app
