from flask import Blueprint, redirect, request, jsonify
from backend.models import States
from backend.instances import db
from backend.schema import multiple, single

estados = Blueprint('estados', __name__)

@estados.route('/api/estados', methods=['GET'])
def all_states():
    """
    Obtener listado de estados

    En este endpoint puedes obtener el listado de todos los estados de la República Mexicana 
    ---
    tags:
      - Estados
    produces:
      - application/json

    responses:
      200:
        description: Obtener lista de estados
    """
    estados = States.query.all()
    esquema = multiple.dump(estados)
    return jsonify(esquema)


@estados.route('/api/estado/<int:id>', methods=['GET'])
def one_state(id):
    """
    Obtener estado por id

    En este endpoint puedes obtener información de algún estado de la República Mexicana 
    ---
    tags:
      - Estados
    produces:
      - application/json
    parameters:
      - in: path
        name: id
        type: string
        description: id para mostrar estado
        required: true

    responses:
      200:
        description: Obtener estado por id
    """
    estado = States.query.get(id)
    esquema = single.dump(estado)
    return jsonify(esquema)

@estados.route('/', methods=['GET'])
def index():
    return jsonify({'msg':'ve a /docs para ver la documentación en swagger'})