from app.storage import get_all_products, update_stock

def resolve_productos(_, info):
    return get_all_products()

def resolve_modificar_stock(_, info, id, cantidad):
    return update_stock(id, cantidad)
