import tkinter as tk # siempre importar  la libreria tkinter para interfaces graficas
from tkinter import COMMAND, END, ttk # para los widgets de estilo 
ventana=tk.Tk() #crea la ventana principal 
ventana.title('calculadora basica ') #titulo para la ventana     
ventana.geometry("200x200") # define el tamano de la ventana 
entradanumero=tk.Entry(ventana)
entradanumero.grid(row=0, columnspan=5, sticky="we")
#funciones de entrada 
i=0
def int_num(n): # esta funcion agrega solo la parte de los numeros a la pantalla
    global i
    entradanumero.insert(i, n)
    i+=1
def int_op(operator): # esta funcion agrega la pate de la operacion a la pantalla
    global i 
    entradanumero.insert(i, operator)
    i+=1
def limpiar_pantalla():
    entradanumero.delete(0, END)
def borrar_elemento(): #borra un solo elemento de la pantalla
    valor_actual=entradanumero.get()
    if len(valor_actual)>0:
        nuevo_valor_actual = valor_actual[:-1] # elimina el ultimo caracter
        limpiar_pantalla()
        entradanumero.insert(0,nuevo_valor_actual)
    else:
        limpiar_pantalla()
        entradanumero.insert(0, 'error')
def calcular(): #calcula la expresion de la pantalla
    valor_actual=entradanumero.get()
    try:
        resultado = eval(valor_actual)
        limpiar_pantalla()
        entradanumero.insert(0, resultado)
    except Exception as e:
        limpiar_pantalla()
        entradanumero.insert(0, "Sintax Error")
        
        
    

##botones numericos
boton1=tk.Button(ventana, text="1", command=lambda:int_num(1)).grid(row=2, column=0, sticky="we")
boton2=tk.Button(ventana, text="2", command=lambda:int_num(2)).grid(row=2, column=1, sticky="we") 
boton3=tk.Button(ventana, text="3", command=lambda:int_num(3)).grid(row=2, column=2, sticky="we")
boton4=tk.Button(ventana, text="4", command=lambda:int_num(4)).grid(row=3, column=0, sticky="we")
boton5=tk.Button(ventana, text="5", command=lambda:int_num(5)).grid(row=3, column=1, sticky="we")
boton6=tk.Button(ventana, text="6", command=lambda:int_num(6)).grid(row=3, column=2, sticky="we")
boton7=tk.Button(ventana, text="7", command=lambda:int_num(7)).grid(row=4, column=0, sticky="we")
boton8=tk.Button(ventana, text="8", command=lambda:int_num(8)).grid(row=4, column=1, sticky="we")
boton9=tk.Button(ventana, text="9", command=lambda:int_num(9)).grid(row=4, column=2, sticky="we")
boton0=tk.Button(ventana, text="0", command=lambda:int_num(0)).grid(row=5, column=1, sticky="we")
#botones especiales 
botonAC=tk.Button(ventana, text="AC", command=lambda: limpiar_pantalla()).grid(row=5, column=0, sticky="we")
botonpunto=tk.Button(ventana, text="%", command=lambda:int_op('%')).grid(row=5, column=2, sticky="we")
botonigual=tk.Button(ventana, text="=", command=lambda: calcular()).grid(row=5, column=4, sticky="we")
botoborrar=tk.Button(ventana, text="˿", command=lambda: borrar_elemento()).grid(row=2, column=4, sticky="we")
#botones de operaciones
botonsuma =tk.Button(ventana, text="+", command=lambda:int_op("+")).grid(row=2, column=3, sticky="we")
botonresta=tk.Button(ventana, text="-", command=lambda:int_op("-")).grid(row=3, column=3, sticky="we")
botonmultiplicacion=tk.Button(ventana, text="x", command=lambda:int_op("*")).grid(row=4, column=3, sticky="we")
botondivision=tk.Button(ventana, text="/", command=lambda:int_op("/")).grid(row=5, column=3, sticky="we")
botonparentesis1=tk.Button(ventana, text="(", command=lambda:int_op("(")).grid(row=3, column=4, sticky="we")
botonparentesis2=tk.Button(ventana, text=")", command=lambda:int_op(")")).grid(row=4, column=4, sticky="We")

ventana.mainloop()
