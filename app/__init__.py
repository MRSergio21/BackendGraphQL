from flask import Flask, request, jsonify
from flask_cors import CORS
from graphene import ObjectType, String, Schema

class Query(ObjectType):
    hello = String(name=String(default_value="stranger"))

    def resolve_hello(root, info, name):
        return f'Hello {name}!'

schema = Schema(query=Query)

def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route("/graphql", methods=["POST"])
    def graphql_server():
        data = request.get_json()
        result = schema.execute(
            data.get("query"),
            variables=data.get("variables")
        )
        response = {}
        if result.errors:
            response["errors"] = [str(e) for e in result.errors]
        if result.data:
            response["data"] = result.data
        return jsonify(response)

    return app