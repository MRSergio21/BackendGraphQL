from ariadne import QueryType, MutationType, make_executable_schema, gql
from app.resolvers import resolve_productos, resolve_modificar_stock

type_defs = gql("""
    type Producto {
        id: Int!
        nombre: String!
        precio: Float!
        stock: Int!
        disponible: Boolean!
    }

    type Query {
        productos: [Producto!]!
    }

    type Mutation {
        modificarStock(id: Int!, cantidad: Int!): Producto
    }
""")

query = QueryType()
mutation = MutationType()

query.set_field("productos", resolve_productos)
mutation.set_field("modificarStock", resolve_modificar_stock)

schema = make_executable_schema(type_defs, query, mutation)
