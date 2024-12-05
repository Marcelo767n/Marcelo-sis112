import tkinter as tk
import csv

ventana=tk.Tk()
ventana.title("Mi primera ventana")
ventana.geometry("200x500")

nombreContacto=tk.Label(ventana, text="Nombre")
nombreContacto.pack()

entradaNombre=tk.Entry(ventana)
entradaNombre.pack()
 
numeroTelefono=tk.Label(ventana, text="Numero de telefono")
numeroTelefono.pack()

entradaTelefono=tk.Entry(ventana)
entradaTelefono.pack()

correoelctronico=tk.Label(ventana, text="Correo Electronico")
correoelctronico.pack()

entradacorreo=tk.Entry(ventana)
entradacorreo.pack()

def guardar():
    nombre=entradaNombre.get()
    telefono=entradaTelefono.get()
    correo=entradacorreo.get()
    with open ("Agenda.csv", "a", newline="") as archivo:
        contacto=csv.writer(archivo)
        contacto.writerow([nombre, telefono, correo])

botonGuardar=tk.Button(ventana, text="Guardar contactos", command=guardar)
botonGuardar.pack()

ventana.mainloop() 