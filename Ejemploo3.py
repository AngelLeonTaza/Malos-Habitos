def area_Rectangulo(largo, ancho):
    multiplicacion_rectangulo = largo * ancho
    return multiplicacion_rectangulo

def area_Triangulo(base, altura):
    multiplicacion_triangulo = 0.5 * base * altura
    return multiplicacion_triangulo

def principal():
    largo = 4
    ancho = 6
    print(f"Área del rectángulo es:{area_Rectangulo(largo,ancho)}")

    base = 5
    altura = 8
    print(f"Área del triángulo es:{area_Triangulo(base,altura)}")

#Llamado a funcion principal
principal()