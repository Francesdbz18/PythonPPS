import random

def adivina_numero():
    numero = random.randint(1, 10)
    intento = None
    while intento != numero:
        intento = int(input("Adivina el número entre 1 y 10: "))
        if intento < numero:
            print("El número es mayor.")
        elif intento > numero:
            print("El número es menor.")
    print("¡Correcto! Felicitaciones.")

adivina_numero()