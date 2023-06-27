import tkinter as tk
from tkinter import ttk

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Ventana con Tabla")
        self.geometry("400x300")

        # Crear tabla
        self.tabla = ttk.Treeview(self, columns=("Campo 1", "Campo 2"), show="headings")
        self.tabla.column("Campo 1", width=150)
        self.tabla.column("Campo 2", width=150)
        self.tabla.heading("Campo 1", text="Campo 1")
        self.tabla.heading("Campo 2", text="Campo 2")

        # Agregar datos a la tabla
        self.tabla.insert("", "end", values=("Dato 1", "Dato 2"))
        self.tabla.insert("", "end", values=("Dato 3", "Dato 4"))
        self.tabla.insert("", "end", values=("Dato 5", "Dato 6"))
        self.tabla.insert("", "end", values=("Dato 7", "Dato 8"))
        self.tabla.insert("", "end", values=("Dato 1", "Dato 2"))
        self.tabla.insert("", "end", values=("Dato 3", "Dato 4"))
        self.tabla.insert("", "end", values=("Dato 5", "Dato 6"))
        self.tabla.insert("", "end", values=("Dato 7", "Dato 8"))

        # Crear scrollbar y asociarlo a la tabla
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)

        # Posicionar la tabla y el scrollbar en la ventana
        self.tabla.place(x=50, y=50, width=300, height=200)
        scrollbar.place(x=350, y=50, height=200)

ventana_principal = VentanaPrincipal()
ventana_principal.mainloop()
