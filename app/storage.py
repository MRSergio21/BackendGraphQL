productos = [
    {"id": 1, "nombre": "Play Station 4", "precio": 450.0, "stock": 22, "disponible": True},
    {"id": 2, "nombre": "Xbox Series S", "precio": 400.0, "stock": 15, "disponible": True},
    {"id": 3, "nombre": "Nintendo Switch", "precio": 200.0, "stock": 5, "disponible": True},
]

def get_all_products():
    return productos

def get_product_by_id(product_id):
    return next((p for p in productos if p["id"] == product_id), None)

def update_stock(product_id, cantidad):
    producto = get_product_by_id(product_id)
    if not producto:
        return None

    producto["stock"] += cantidad

    if producto["stock"] <= 0:
        producto["stock"] = 0
        producto["disponible"] = False
    else:
        producto["disponible"] = True

    return producto
