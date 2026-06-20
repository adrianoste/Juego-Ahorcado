import random

# Lista de palabras
palabras = [
    "python",
    "algoritmo",
    "variable",
    "programacion",
    "computadora"
]

# Seleccionar palabra aleatoria
palabra = random.choice(palabras)

# Crear palabra oculta
oculta = ["_"] * len(palabra)

# Vidas iniciales
vidas = 6

print("=== JUEGO DEL AHORCADO ===")

while vidas > 0 and "_" in oculta:

    print("\nPalabra:", " ".join(oculta))
    print("Vidas restantes:", vidas)

    letra = input("Ingrese una letra: ").lower()

    # Validación
    if len(letra) != 1:
        print("Debe ingresar una sola letra.")
        continue

    if letra in palabra:

        for i in range(len(palabra)):

            if palabra[i] == letra:
                oculta[i] = letra

        print("¡Correcto!")

    else:
        vidas -= 1
        print("Letra incorrecta.")

# Resultado final
if "_" not in oculta:

    print("\n¡FELICIDADES!")
    print("Has ganado.")

else:

    print("\nGAME OVER")
    print("La palabra era:", palabra)
