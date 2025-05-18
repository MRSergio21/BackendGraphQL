from app.data import productos

def resolve_actualizar_stock(_, info, id, cantidad):
    for producto in productos:
        if producto["id"] == id:
            producto["stock"] += cantidad
            producto["disponible"] = producto["stock"] > 0
            return producto
    raise Exception("Producto no encontrado")

def resolve_crear_producto(_, info, nombre, precio, stock):
    nuevo = {
        "id": max([p["id"] for p in productos], default=0) + 1,
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
        "disponible": stock > 0
    }
    productos.append(nuevo)
    return nuevo

def resolve_eliminar_producto(_, info, id):
    global productos
    for i, p in enumerate(productos):
        if p["id"] == id:
            del productos[i]
            return True
    return False

def resolve_actualizar_producto(_, info, id, nombre=None, precio=None, stock=None):
    for producto in productos:
        if producto["id"] == id:
            if nombre is not None:
                producto["nombre"] = nombre
            if precio is not None:
                producto["precio"] = precio
            if stock is not None:
                producto["stock"] = stock
                producto["disponible"] = stock > 0
            return producto
    raise Exception("Producto no encontrado")
