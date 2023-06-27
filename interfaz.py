import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
from tkinter import ttk
from tkinter import messagebox

from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
import mpl_toolkits as mpl




def obtener_nodos_alcanzables(matriz_adyacencia, etiquetas, nodo):
    n = len(matriz_adyacencia)
    visitados = [False] * n
    nodos_alcanzables = []
    
    stack = [nodo]
    visitados[nodo] = True
    
    while stack :
        v = stack.pop()
        nodos_alcanzables.append(etiquetas[v])
        
        for i in range(n):
            if matriz_adyacencia[v][i] != 0 and not visitados[i]:
                stack.append(i)
                visitados[i] = True
    
    return nodos_alcanzables




def obtener_subgrafo(matriz_adyacencia, lista_nodos, nodo):
    subgrafo_nodos = [n for n in lista_nodos if n != nodo]
    if(nodo!=None):
        subgrafo_nodos.insert(0, nodo)  # Insertar el nodo de interés en el primer lugar       
    
    
    subgrafo_matriz = [[matriz_adyacencia[i][j] for j in subgrafo_nodos] for i in subgrafo_nodos]
    
    return subgrafo_matriz, subgrafo_nodos


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Sugerencias")
        self.geometry("1200x600")

        self.label_pelicula = tk.Label(self, text="Ingrese el nombre de la película:")
        self.label_pelicula.place(x=20, y=45)

        self.label_1 = tk.Label(self, text="Director:")
        self.label_1.place(x=900, y=45)

        self.label_2 = tk.Label(self, text="Genero:")
        self.label_2.place(x=600, y=45)

        self.entry_pelicula = tk.Entry(self)
        self.entry_pelicula.place(x=250, y=45)

        self.boton_actualizar = tk.Button(self, text="Sugerencias", command=self.actualizar_grafico)
        self.boton_actualizar.place(x=450, y=40)

        # Crear tabla
        self.tabla = ttk.Treeview(self, columns=("ID", "Nombre", "Director", "Género","Duración(mins)"), show="headings")
        self.tabla.column("ID", width=50)
        self.tabla.column("Nombre", width=150)
        self.tabla.column("Director", width=150)
        self.tabla.column("Género", width=150)
        self.tabla.column("Duración(mins)", width=50)

        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Director", text="Director")
        self.tabla.heading("Género", text="Género")
        self.tabla.heading("Duración(mins)", text="Duración(mins)")

        # Crear scrollbar y asociarlo a la tabla
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)

        # Posicionar la tabla y el scrollbar en la ventana
        self.tabla.place(x=550, y=100, width=600, height=450)
        scrollbar.place(x=1150, y=100, height=450)

        # Leer el archivo CSV y almacenarlo en un DataFrame
        df = pd.read_csv('dataset.csv')

        # Convertir el DataFrame a un array de objetos
        self.data = df.to_dict('records')

        # Obtener una lista de directores únicos
        self.directores = df['director'].unique().tolist()

        # Obtener una lista de géneros únicos (separados por ',')
        self.generos = df['genres'].str.split(',').explode().apply(lambda x: x.strip()).unique().tolist()


        # Crear el combobox de géneros
        self.combo_generos = ttk.Combobox(self)
        self.combo_generos['values'] = self.generos
        self.combo_generos.place(x=690, y=45)

        # Crear el combobox de directores
        self.combo_directores = ttk.Combobox(self)
        self.combo_directores['values'] = self.directores
        self.combo_directores.place(x=990, y=45)

        # CARGADO DE matriz de adyasencia
        self.matriz = np.loadtxt('matrizAdy.csv', delimiter=',')

        # Crear un grafo de ejemplo
        self.actualizar_grafico()

    #BUSQUEDA LINEAL
    def buscar_pelicula(self, nombre_pelicula):
        pelicula = None
        for item in self.data:
            if item['title'] == nombre_pelicula:
                pelicula = item
                break
            try:
                if item['id'] == int(nombre_pelicula):
                    pelicula = item
                    break
            except ValueError:
                pass
        return pelicula

    def actualizar_tabla(self, lista):
        # Limpiar la tabla
        self.tabla.delete(*self.tabla.get_children())

        # Buscar objetos con ID igual a los elementos de la lista
        for i in lista:
            # Agregar el objeto a la tabla
            item = self.data[i]
            self.tabla.insert("", "end", values=(item['id'], item['title'], item['director'], item['genres'],item['duration']))

    def restriccion(self, director, genero, lista):
        sublista = []
        if director and director != "" and director != "-" and genero and genero != "" and genero != "-":
            for i in lista:
                obj = self.data[i]
                if obj["director"] == director and genero in obj["genres"]:
                    sublista.append(i)

        elif director and director != "" and director != "-" :
            for i in lista:
                obj = self.data[i]
                if obj["director"] == director :
                    sublista.append(i)
        
        elif genero and genero != "" and genero != "-":
            for i in lista:
                obj = self.data[i]
                if genero in obj["genres"]:
                    sublista.append(i)
        else:
            for i in lista:
                sublista.append(i)

    
        
        return sublista




    def actualizar_grafico(self):
        nombre_pelicula = self.entry_pelicula.get()
        pelicula = self.buscar_pelicula(nombre_pelicula)

        # OBTENCION DE DATA:
        # Convertir el DataFrame en una matriz de N x N
        n = len(self.matriz)  # Número n (puedes ajustarlo a tu necesidad)
        etiquetas_nodos = list(range(n))  # Llenar el array con los números del 0 al 
        

        subgrafo = self.matriz
        sub_lista = etiquetas_nodos
        nodo_inicial = None
        if pelicula is not None:
            nodo_inicial = pelicula['id']
            nodos_alcanzables = obtener_nodos_alcanzables(self.matriz, etiquetas_nodos, nodo_inicial)

            subgrafo, sub_lista = obtener_subgrafo(self.matriz, nodos_alcanzables, nodo_inicial)
            subgrafo = np.array(subgrafo)

        sub_lista=(self.restriccion(self.combo_directores.get() ,self.combo_generos.get(),sub_lista))
        subgrafo, sub_lista=(obtener_subgrafo(self.matriz, sub_lista, nodo_inicial))
        if(len(sub_lista)==0):
            messagebox.showinfo("ERROR","No hay peliculas que cumplan con el criterio de filtrado...")
            return

        subgrafo = np.array(subgrafo)
        print(subgrafo,sub_lista)

        # Crear un grafo a partir de la matriz de adyacencia
        G = nx.from_numpy_array(subgrafo)

        # Crear el gráfico utilizando networkx y matplotlib
        fig, ax = plt.subplots(figsize=(4, 4))
        nx.draw(G, with_labels=True, ax=ax, labels=dict(zip(G.nodes, sub_lista)))
        fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
        # Crear el widget FigureCanvasTkAgg con tamaño fijo
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.get_tk_widget().configure(width=500, height=450)
        canvas.draw()
        canvas.get_tk_widget().place(x=20, y=100)

        # Crear la barra de herramientas de matplotlib
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        toolbar.place(x=20, y=510)

        self.actualizar_tabla(sub_lista)


ventana_principal = VentanaPrincipal()
ventana_principal.mainloop()
