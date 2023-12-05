import time
menorDistancia = 99
mayorDistancia = 0
menoresDistancias = []
mayoresDistancias = []
mensaje_distancia = []

def calcular_distancia_levenshtein(cadena1, cadena2):
    # Variables globales
    global menorDistancia
    global mayorDistancia
    global menoresDistancias
    global mayoresDistancias 

    # Calcula la matriz de distancia de Levenshtein
    matriz = [[0] * (len(cadena2) + 1) for _ in range(len(cadena1) + 1)]

    for i in range(len(cadena1) + 1):
        matriz[i][0] = i

    for j in range(len(cadena2) + 1):
        matriz[0][j] = j

    for i in range(1, len(cadena1) + 1):
        for j in range(1, len(cadena2) + 1):
            costo = 0 if cadena1[i - 1] == cadena2[j - 1] else 1
            matriz[i][j] = min(matriz[i - 1][j] + 1, matriz[i][j - 1] + 1, matriz[i - 1][j - 1] + costo)

    distancia = matriz[len(cadena1)][len(cadena2)]

    if distancia != 0:
        # menor distancia
        if distancia < menorDistancia:
            menorDistancia = distancia
            menoresDistancias = ([[cadena1, cadena2]])
        elif distancia == menorDistancia:
            menoresDistancias.append([cadena1,cadena2])
        # mayor distancia
        if distancia > mayorDistancia:
            mayorDistancia = distancia
            mayoresDistancias = ([[cadena1, cadena2]])
        elif distancia == mayorDistancia:
            mayoresDistancias.append([cadena1,cadena2])

        

    # Mostrar Distancia entre cadenas
    mensaje_distancia.append([f"La distancia de la cadena '{cadena1}' a la cadena '{cadena2}' es de: {distancia}"])


def calcular_nuevamente():
    respuesta = ""
    while (respuesta == ""):
        respuesta = input("Desea calcular otra distancia? Coloque S/N: \n")
        if (respuesta.upper() != "S" and respuesta.upper() != "N"):
            respuesta = ""
    return respuesta

def pedir_cadenas(cadena1 = "", cadena2 = "",):
    # Pedir cadena 1
    while (cadena1 == ""):
        cadena = input("Ingrese una cadena: ")
        if (cadena.strip() == ""):
            print("No puede ingresar una cadena vacía.")
        cadena1 = cadena.strip()
    # Pedir cadena 2
    while (cadena2 == ""):
        cadena = input("Ingrese una cadena: ")
        if (cadena.strip() == ""):
            print("No puede ingresar una cadena vacía.")
        cadena2 = cadena.strip()
    

    # Calcular la distancia de Levenshtein
    calcular_distancia_levenshtein(cadena1, cadena2)

    # Preguntar si desea calcular otras palabras
    # respuesta = calcular_nuevamente()
    # if (respuesta.upper() == "S"):
    #     pedir_cadenas()

# pedir_cadenas()

lista_palabras = ["CEDRO", "OMBU", "PINO", "JACARANDA", "TIPA", "ALGARROBO", "CHAÑAR", "QUEBRACHO", "SAUCE"]
for cadena1 in lista_palabras:
    menorDistancia = 99
    mayorDistancia = 0
    menoresDistancias = []
    mayoresDistancias = []
    print("---------------------------------")
    print("DISTANCIAS DESDE LA CADENA: " + cadena1)
    for cadena2 in lista_palabras:
        pedir_cadenas(cadena1,cadena2)
    mensaje_distancia.append("----------- FIN " + cadena1 + "-----------")
    print("")
    print(f"Menores distancias de la cadena {cadena1} con una distancia de {menorDistancia}:\n {menoresDistancias}")
    print(f"Mayores distancias de la cadena {cadena1} con una distancia de {mayorDistancia}:\n {mayoresDistancias}")
    print("")
    time.sleep(1)

result = input("Desea ver las distancias calculadas? S/N: \n")
if result.upper() == "S":
    print(f"\n {mensaje_distancia} ")

