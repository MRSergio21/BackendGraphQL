# main.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from ariadne import graphql_sync
from ariadne.explorer import ExplorerGraphiQL
from app.schema import schema

app = Flask(__name__)
CORS(app)  # Permitir solicitudes desde frontend (CORS)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    # Explorar y probar consultas en navegador
    return ExplorerGraphiQL().html(None), 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    # Recibir y procesar consultas GraphQL
    data = request.get_json()
    success, result = graphql_sync(schema, data, context_value=request, debug=True)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
