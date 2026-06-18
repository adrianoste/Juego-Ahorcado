import random

palabras = [
    "python",
    "algoritmo",
    "variable",
    "programacion",
    "computadora"
]

palabra = random.choice(palabras)

print("Bienvenido al Juego del Ahorcado")
print("La palabra tiene", len(palabra), "letras")
