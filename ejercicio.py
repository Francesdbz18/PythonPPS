productos = ["leche", "pan", "huevos", "manzanas", "zumo"]
precios = (1.50, 0.90, 2.50, 3.00, 2.00)
inventario = {"leche": 10, "pan": 20, "huevos": 15, "manzanas": 8, "zumo": 12}
productos_sin_descuento = {"huevos", "zumo"}
for p, precio in zip(productos, precios):
    print(f"- {p}: {precio:.2f} €")
with_descuento = [p for p in productos if p not in productos_sin_descuento]
print("Productos con descuento:")
if with_descuento:
    for p in with_descuento:
        print(f"- {p}")
else:
    print("(ninguno)")
for producto in inventario.keys():
    cantidad = inventario.get(producto, 0)
    if cantidad > 0:
        inventario[producto] = cantidad - 1
    else:
        inventario[producto] = 0
print("Inventario actualizado:")
for producto, cantidad in inventario.items():
    print(f"- {producto}: {cantidad}")
