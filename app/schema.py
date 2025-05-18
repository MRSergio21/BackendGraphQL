from ariadne import QueryType, MutationType, make_executable_schema, gql
from app.resolvers.query_resolver import resolve_productos
from app.resolvers.mutation_resolver import (
    resolve_actualizar_stock,
    resolve_crear_producto,
    resolve_eliminar_producto,
    resolve_actualizar_producto,
)

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
        actualizarStock(id: Int!, cantidad: Int!): Producto!
        crearProducto(nombre: String!, precio: Float!, stock: Int!): Producto!
        eliminarProducto(id: Int!): Boolean!
        actualizarProducto(id: Int!, nombre: String, precio: Float, stock: Int): Producto!
    }
""")

query = QueryType()
query.set_field("productos", resolve_productos)

mutation = MutationType()
mutation.set_field("actualizarStock", resolve_actualizar_stock)
mutation.set_field("crearProducto", resolve_crear_producto)
mutation.set_field("eliminarProducto", resolve_eliminar_producto)
mutation.set_field("actualizarProducto", resolve_actualizar_producto)

schema = make_executable_schema(type_defs, [query, mutation])
