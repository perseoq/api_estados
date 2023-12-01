from flask import Flask, request, jsonify, redirect, url_for
from flask_migrate import Migrate
from backend.instances import db, mw
from backend.settings import Settings
from flask_cors import CORS
from backend.views import estados
from flasgger import Swagger, Flasgger, APISpec


app = Flask(__name__)
app.config.from_object(Settings)

app.config['SWAGGER'] = {
    'title': 'Estados de la República Mexicana',
    "version": "1.0",
    'uiversion': 3,  # optional, choose 3 for the latest Swagger UI version
    'description': 'Nombre del estado, su capital y su población',
    'specs_route': '/docs/'
}

swagger = Swagger(app)




db.init_app(app)
mw.init_app(app)
cors = CORS(app)
migrate = Migrate(app, db)

# Blueprint

app.register_blueprint(estados)

with app.app_context():
    db.create_all()