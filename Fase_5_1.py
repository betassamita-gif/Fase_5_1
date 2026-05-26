Menu = [
    ["Tacos", "Comida Mexicana", 20000],
    ["Pasta al Pesto", "Comida Italiana", 23000],
    ["Hamburguesa", "Comida Rapida", 20000],
    ["Sushi", "Comida Japonesa", 26000],
    ["Pizza", "Comida Rapida", 25000],
    ["Ensalada Cesar", "Comida Saludable", 27000],
    ["Nachos", "Comida Mexicana", 22000],
    ["Vegetales Salteados", "Comida Saludable", 27000],
    ["Ramen", "Comida Japonesa", 32000],
    ["Lasagna", "Comida Italiana", 25000]
	]
# Se definen la categoría objetivo y el umbral de descuento para la promoción
Categoria_Objetivo = "Comida Mexicana"
umbral_descuento = 19000
def calcular_precio_final(categoria, precio_base):
    descuento = 0.15

    # Aplicamos la promoción según las condiciones
    if categoria == Categoria_Objetivo and precio_base > umbral_descuento:
        precio_final = precio_base - (precio_base * descuento)
    else:
        precio_final = precio_base

    return precio_final

# Mostrar el menú con promociones
print("Menu con promociones aplicadas\n")
	
for producto in Menu:
	    nombre = producto[0]
categoria = producto[1]
precio_base = producto[2]
	    
	    # Se calcula el precio final
precio_final = calcular_precio_final(categoria, precio_base)
	    
	    # Se muestra la información final
print(f"Producto:        {nombre}")
print(f"Categoría:       {categoria}")
print(f"Precio base:     $ {precio_base}")
print(f"Precio final:    $ {precio_final}")
print("=" * 40)
