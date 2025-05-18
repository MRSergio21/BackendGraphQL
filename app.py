from flask import Flask, request, jsonify
from ariadne import QueryType, make_executable_schema, graphql_sync
from ariadne.explorer import ExplorerGraphiQL

type_defs = """
    type Query {
        hello(name: String!): String!
    }
"""

query = QueryType()

@query.field("hello")
def resolve_hello(_, info, name):
    return f"Hola {name}!"

schema = make_executable_schema(type_defs, query)

app = Flask(__name__)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return ExplorerGraphiQL().html(None), 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(schema, data, context_value=request, debug=True)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
