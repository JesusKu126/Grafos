import networkx as nx
import matplotlib.pyplot as plt

estados = {
    "CDMX": 500,
    "Jalisco": 700,
    "Nuevo León": 600,
    "Quintana Roo": 900,
    "Oaxaca": 800,
    "Chihuahua": 750,
    "Yucatán": 850
}

conexiones = [
    ("CDMX", "Jalisco"),
    ("CDMX", "Nuevo León"),
    ("CDMX", "Quintana Roo"),
    ("Jalisco", "Oaxaca"),
    ("Jalisco", "Chihuahua"),
    ("Nuevo León", "Chihuahua"),
    ("Nuevo León", "Yucatán"),
    ("Quintana Roo", "Yucatán"),
    ("Oaxaca", "Chihuahua"),
    ("Chihuahua", "Yucatán")
]

G = nx.Graph()
G.add_nodes_from(estados.keys())

for conexion in conexiones:
    estado1, estado2 = conexion
    costo = max(estados[estado1], estados[estado2])
    G.add_edge(estado1, estado2, weight=costo)

def calcular_costo(ruta):
    costo_total = 0
    for i in range(len(ruta) - 1):
        estado_actual = ruta[i]
        estado_siguiente = ruta[i + 1]
        costo_total += G[estado_actual][estado_siguiente]["weight"]
    return costo_total

def dibujar_grafo():
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=1500, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray", width=2)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Grafo de estados y conexiones")
    plt.show()

def menu():
    while True:
        print("\nMenú:")
        print("a) Recorrer sin repetir estados")
        print("b) Recorrer permitiendo repetir estados")
        print("c) Obtener costo de ir a cada estado")
        print("d) Lista de estados y sus costos")
        print("e) Dibujar el grafo")
        print("f) Salir")
        opcion = input("Elige una opción: ")

        if opcion.lower() == 'a':
            recorrer_sin_repetir()
        elif opcion.lower() == 'b':
            recorrer_con_repetir()
        elif opcion.lower() == 'c':
            obtener_costo()
        elif opcion.lower() == 'd':
            listar_estados_y_costos()
        elif opcion.lower() == 'e':
            dibujar_grafo()
        elif opcion.lower() == 'f':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def recorrer_sin_repetir():
    recorrido = []
    for i in range(len(estados)):
        print(f"Elige el estado {i+1}/{len(estados)}:")
        print([estado for estado in estados if estado not in recorrido])
        estado_elegido = input("Estado: ").capitalize()
        if estado_elegido not in recorrido and estado_elegido in estados:
            recorrido.append(estado_elegido)
        else:
            print("Estado inválido o ya seleccionado. Inténtalo de nuevo.")
    print("Recorrido sin repetir estados:", recorrido)
    costo_total = calcular_costo(recorrido)
    print("Costo total del recorrido:", costo_total)

def recorrer_con_repetir():
    recorrido = []
    opcion = 's'
    while opcion.lower() == 's':
        print("Elige un estado:")
        print(list(estados.keys()))
        estado_elegido = input("Estado: ").capitalize()
        if estado_elegido in estados:
            recorrido.append(estado_elegido)
        else:
            print("Estado inválido. Inténtalo de nuevo.")
        opcion = input("¿Deseas agregar otro estado? (s/n): ")
    print("Recorrido con repetición de estados:", recorrido)
    costo_total = calcular_costo(recorrido)
    print("Costo total del recorrido:", costo_total)

def obtener_costo():
    for estado, costo in estados.items():
        print(f"{estado}: ${costo}")

def listar_estados_y_costos():
    for estado, costo in estados.items():
        print(f"{estado}: ${costo}")

menu()
