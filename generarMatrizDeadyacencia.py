import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

nodos =2000



# Cargamos los datos
data = pd.read_csv('dataset.csv', nrows=nodos)

# Creamos diccionarios para mapear actores, géneros y directores a valores numéricos
actor_dict = {}
genre_dict = {}
director_dict = {}
counter = 0

# Iteramos sobre los datos para crear los diccionarios
data2=[]
for _, row in data.iterrows():
    actors = row['actors'].split(', ')
    genres = row['genres'].split(', ')
    director = row['director']

    # Mapeamos los actores a valores numéricos
    actors_codes = []
    for actor in actors:
        if actor == '' or actor == '-' :
            actors_codes.append(-1)
        else:
            if actor not in actor_dict:
                actor_dict[actor] = counter
                counter += 1
            actors_codes.append(actor_dict[actor])

    # Mapeamos los géneros a valores numéricos
    genres_codes = []
    for genre in genres:
        if genre == '' or genre == '-' :
            genres_codes.append(-1)
        else:
            if genre not in genre_dict:
                genre_dict[genre] = counter
                counter += 1
            genres_codes.append(genre_dict[genre])

    # Mapeamos el director a un valor numérico
    if director == '' or director == '-' :
        director_code = -1
    else:
        if director not in director_dict:
            director_dict[director] = counter
            counter += 1
        director_code = director_dict[director]

    # Obtenemos el id de la película y su duración
    id_ = row['id']
    duration = row['duration']

    # Creamos la lista de valores numéricos para la película actual
    movie_values = [id_, duration, director_code, actors_codes, genres_codes, row['year']]

    data2.append(movie_values)

# Creamos un grafo vacío
G = nx.Graph()

# Generamos la matriz 
matriz_ady = np.full((nodos, nodos), 0)


# Agregamos los nodos al grafo
for movie in data2:
    G.add_node(movie[0])

# Agregamos las aristas al grafo con sus respectivos pesos
for i in range(len(data2)):
    for j in range(i+1, len(data2)):
        peso = 0
        if data2[i][1] == data2[j][1] and data2[i][1]!=-1 :
            peso += 1
        if data2[i][2] == data2[j][2] and data2[i][1]!=-1:
            peso += 5
        for actor_i in data2[i][3]:
            for actor_j in data2[j][3]:
                if actor_i == actor_j and actor_i != -1:
                    peso += 1
        for genre_i in data2[i][4]:
            for genre_j in data2[j][4]:
                if genre_i == genre_j and genre_i != -1:
                    peso += 5
        if data2[i][5] == data2[j][5] and data2[i][1]!=-1:
            peso += 1
        if peso > 2:
            similarity = 100 / peso
            matriz_ady[data2[j][0]][data2[i][0]]=peso
            matriz_ady[data2[i][0]][data2[j][0]]=peso
            G.add_edge(data2[i][0], data2[j][0], weight=peso)

#IMPRIMIR Matriz de adyasencia
df = pd.DataFrame(matriz_ady)
df.to_csv('matrizAdy.csv', index=False, header=False)

# Dibujo del grafo
nx.draw(G, with_labels=False, node_size=5, node_color='black')

# Mostrar la ventana
plt.show()
