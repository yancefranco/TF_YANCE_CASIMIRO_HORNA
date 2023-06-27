import pandas as pd

import re


# Lee el primer archivo CSV y guarda solo los primeros 1000 rows desde la fila 500
df1 = pd.read_csv('IMDb Movies India.csv', skiprows=range(1, 500), nrows=1000, encoding='ISO-8859-1')

# Lee el segundo archivo CSV y guarda solo los primeros 1000 rows
df2 = pd.read_csv('IMDB-Movie-Data.csv', nrows=1000, encoding='ISO-8859-1')

# Crea un array de diccionarios con los datos de cada fila del segundo archivo
array2 = []
index1 = 0
for index, row in df2.iterrows():
    data = {
        "id": index1,
        "title": row["Title"],
        "duration": row["Runtime (Minutes)"],
        "director": row["Director"],
        "actors": row["Actors"],
        "genres": row["Genre"] if isinstance(row["Genre"], str) else "",
        "year": row["Year"]
    }
    index1 += 1
    array2.append(data)

# Crea un array de diccionarios con los datos de cada fila del primer archivo
array1 = []
for index, row in df1.iterrows():
    data = {
    "id": index1,
    "title": row["Name"],
    "duration": int(row["Duration"].split()[0]) if isinstance(row["Duration"], str) and len(row["Duration"].split()) == 2 and row["Duration"].split()[0].isdigit() else 0,
    "director": row["Director"],
    "actors": (row["Actor 1"] if isinstance(row["Actor 1"], str) else "-") + ", " + (row["Actor 2"] if isinstance(row["Actor 2"], str) else "-") + ", " + (row["Actor 3"] if isinstance(row["Actor 3"], str) else "-"),
    "genres": row["Genre"] if isinstance(row["Genre"], str) else "-",
    "year": int(re.search(r'\((\d{4})\)', row["Year"]).group(1)) if isinstance(row["Year"], str) and re.search(r'\((\d{4})\)', row["Year"]) and re.search(r'\((\d{4})\)', row["Year"]).group(1).isdigit() else 0
}

    index1 += 1
    # Verifica que el título de la película no se repita con lo que ya hay en el array3
    if data['title'] not in [d['title'] for d in array2]:
        array1.append(data)

# Combina los dos arrays en un tercer array
array3 = array2 + array1

# Imprime el tercer array
print(array3)


import csv

# Abre el archivo CSV y escribe los datos del array3
with open('dataset.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Escribe el encabezado del archivo
    writer.writerow(['id', 'title', 'duration', 'director', 'actors', 'genres', 'year'])
    # Escribe los datos de cada fila del array3
    for movie in array3:
        writer.writerow([movie['id'], movie['title'], movie['duration'], movie['director'], movie['actors'], movie['genres'], movie['year']])

