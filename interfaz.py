from cgitb import text
from email import message
import tkinter
from tokenize import cookie_re
from turtle import st, title
tkinter.Tcl().eval('info patchlevel')

from tkinter import *
from tkinter import ttk


raiz = Tk()

#Propiedades de la ventana
raiz.geometry('300x200') #Tamaño de la ventana
raiz.configure(bg= 'beige') #Color del fondo
raiz.title('Aplicación') #Titulo de la aplicación

ttk.Button(raiz, text= 'Salir', command= quit).pack(side= BOTTOM) #Configuracion boton de salida

raiz.mainloop() #Inicializacion de la ventana


class Aplicacion: #Creacion clase de aplicacion
    def __init__(self): #Creacion del Init
        raiz = Tk() #Atributo del tkinter
        raiz.geometry('300x200') #Tamaño de la ventana
        raiz.configure(bg= 'beige') #fondo de la ventana
        raiz.title('Aplicacion') #Titulo de la aplicacion
        ttk.Button(raiz, text= 'Salir', command= raiz.destroy).pack(side= BOTTOM) #Configuracion del boton de salida
        raiz.mainloop() #Incia la ventana
 
def main(): # main es una funcion para iniciar la aplicacion
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__': #Variable especial con el nombre del script main
    main() #Ejecuta la funcion main

class Aplicacion: #Clase aplicacion
    def __init__(self): #Creacion del init
        self.raiz = Tk() #tkinter
        self.raiz.geometry('300x200') #Tamaño de la ventana
        self.raiz.resizable(width= False, height= False) #Esto impide al usuario maximize la ventana
        self.raiz.title('Ver info') #Titulo de la ventana

        self.tinfo = Text(self.raiz, width= 40, height= 10) # Texto
        self.tinfo.pack(side= TOP) #Posicion del texto
        self.binfo = ttk.Button(self.raiz, text= 'Info', command= self.verinfo) #boton de info
        self.binfo.pack(side= LEFT) #Posicion del boton
        self.bsalir = ttk.Button(self.raiz, text= 'Salir', command=self.raiz.destroy) #Creacion del boton de salida
        self.bsalir.pack(side= RIGHT) #Ubicacion del boton de salida

        self.binfo.focus_set() #Pone el boton en el centro
        self.raiz.mainloop() #Inicia aplicacion


    def verinfo(self): #Metodo verinfo
        self.tinfo.delete("1.0", END) 

        info1 = self.raiz.winfo_class() #info 1 a info 9 variables con tipo de informacion de la ventana
        info2 = self.raiz.winfo_geometry()
        info3 = str(self.raiz.winfo_width())
        info4 = str(self.raiz.winfo_height())
        info5 = str(self.raiz.winfo_rootx())
        info6 = str(self.raiz.winfo_rooty())
        info7 = str(self.raiz.winfo_id())
        info8 = self.raiz.winfo_name()
        info9 = self.raiz.winfo_manager()

        texto_info = "Clase de 'raiz': " + info1 + "\n" #texto que regala todo los datos de las anteriores variables
        texto_info += "Resolución y posición: " + info2 + "\n"
        texto_info += "Anchura ventana: " + info3 + "\n"
        texto_info += "Altura ventana: " + info4 + "\n"
        texto_info += "Pos. Ventana X: " + info5 + "\n"
        texto_info += "Pos. Ventana Y: " + info6 + "\n"
        texto_info += "Id. de 'raiz': " + info7 + "\n"
        texto_info += "Nombre objeto: " + info8 + "\n" 
        texto_info += "Gestor ventanas: " + info9 + "\n"

        self.tinfo.insert('1.0', texto_info)

def main(): #main
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__': #funcion especial __name__
    main()

top = tkinter.Tk() #la aplicacion 
messageLabel = tkinter.Label(top,text= 'Hello world') #texto, la posicion es la parte superior
messageLabel.grid() #funcion para colocar el texto en la ventana
quitbutton = tkinter.Button(top, text= 'Quit', command= top.destroy) #Boton de salida
quitbutton.grid() #posicion del boton
tkinter.mainloop() #inicia la aplicacion

def display(): # funcion display y muestra texto "Hello World"
    messageLabel.configure(text= "Hello world")


top = tkinter.Tk() #La aplicacion
messageLabel = tkinter.Label(top, text= "") #Texto vacio con posicion superior pertenece a tikinter.label
messageLabel.grid(row=0,column=0) #posicion del texto fila 0 columna 0

showButton = tkinter.Button(top, text= 'Show', command=display) #boton llamado show
showButton.grid(row=0,column=1) #posicion el fila 0 y columna 1

quitButton = tkinter.Button(top, text= "Quit", command=top.destroy) #boton de salida
quitButton.grid(row=0,column=2) #posicion misma fila columna 2

tkinter.mainloop() #Inicio de la aplicacion

# Linea 115 a 162 no funciona

def display():
    name = textVar.get() 
    messageLabel.configure(text="Hello "+name)

top = tkinter.Tk()

textVar = tkinter.StringVar("")
textEntry = tkinter.Entry(top,textvariable=textVar,width=12) 
textEntry.grid(row=0,column=0)

messageLabel = tkinter.Label(top,text="",width=12) 
messageLabel.grid(row=1,column=0)

showButton = tkinter.Button(top,text="Show",command=display) 
showButton.grid(row=1,column=1)

quitButton = tkinter.Button(top,text="Quit",command=top.destroy) 
quitButton.grid(row=1,column=2)

tkinter.mainloop()

def display():
    name = textVar.get() 
    ch = choice.get()
    if ch == 1:
        message = "Hello "+name 
    elif ch == 2:
        message = "Goodbye "+name 
    else:
        message = "" 
        messageLabel.configure(text=message)

top = tkinter.Tk()
textVar = tkinter.StringVar("")
textEntry = tkinter.Entry(top,textvariable=textVar,width=12) 
textEntry.grid(row=0,column=0)
messageLabel = tkinter.Label(top,text="",width=12) 
messageLabel.grid(row=1,column=0)
choice = tkinter.IntVar(0)
helloButton = tkinter.Radiobutton(top,text="Hello",
variable=choice,value=1,command=display)
helloButton.grid(row=1,column=1)
goodbyeButton = tkinter.Radiobutton(top,text="Goodbye",
variable=choice,value=2,command=display)
goodbyeButton.grid(row=1,column=2)
quitButton = tkinter.Button(top,text="Quit",command=top.destroy) 
quitButton.grid(row=1,column=3)
tkinter.mainloop()





