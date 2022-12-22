import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

from Algorithm import a_star_algorithm

# crear nueva instancia class Tk()
ventana = tk.Tk()
ventana.title("Mapa Metro")
ventana.attributes('-fullscreen', True)
ventana.resizable(0, 0)  # no poder usar el ampliar, minimizar, cerrar

# variables interface de entrada###
#opcion1 = IntVar()
estacion_origen = StringVar()
estacion_destino = StringVar()
estTransb_O_D = StringVar()
dia_semana = StringVar()
tramo_horario = StringVar()

distancia = float()
Tiempo_min = int()
Tiempo_sec = int()
Tiempo_min = None
Tiempo_sec = None
estTransb_O_D = StringVar()


def listToString(s):

    str1 = ""
    contador = 0

    for ele in s:
        str1 += ele + " ->  "
        contador += 1
        if contador == 5:
            str1 += "\n"
            contador = 0
    str1 = str1[:len(str1)-5]

    return str1


# La imagen esta al mismo nivel de la aplicación.
mapa = tk.PhotoImage(file="mapa-metroatenas.png")  # Leer la imagen
lbl_mapa = tk.Label(ventana, image=mapa)  # es la Imagen de fondo
lbl_mapa.place(x=0, y=0)  # organizar el widget posicionar la imagen

# boton cerrar de la aplicacion


def salir():
    ventana.destroy()  # cerrar la aplicacion


textoResultado0 = Label(ventana, text="")
textoResultado0.pack()
textoResultado0.place(x=800, y=300)


def resultadoInicio():
    #"Irini", "Syntagma"
    # textoResultado0.destroy()
    inicio = combo1.get()
    final = combo2.get()


def calcular():  # v3 ########modificado###########
    estacion_origen = combo1.get()
    estacion_destino = combo2.get()

    dia_semana = combo3.get()
    tramo_horario = combo4.get()

    # Control Estaciones validas en la entrada de datos: estaciones sin servicio en linea 2 a partir de las 23:30 y servicios nocturnos de 24:00 a 02:00.########nuevo###########
    if estacion_origen == estacion_destino:
        tkinter.messagebox.showinfo(
            "Atención", "Origen y Destino no pueden ser la misma estación")
    if estacion_origen in excluir[:] or estacion_destino in excluir[:]:
        tkinter.messagebox.showinfo(
            "Atención", "Debe seleccionar el nombre de una estación origen y una estación destino")
    # Aplicar Filtros
    # las 5 ultimas estaciones de linea3  a partir de las
    if (estacion_origen in nodosexcep[:] or estacion_destino in nodosexcep[:]) and tramo_horario in tramos[4:]:
        tkinter.messagebox.showinfo(
            "Atención", "No hay servicio en la estación origen o destino a partir de las 23:30")
    # de lunes a jueves  de 24:00 a 2:00
    elif (dia_semana in dias[:4] or dia_semana in dias[6]) and tramo_horario in tramos[5:]:
        tkinter.messagebox.showinfo(
            "Atención", "Solo hay servicio nocturno los viernes y sabados, los dias laborables termina el servicio a las 24:00")

    else:
        resultado = listToString(a_star_algorithm(
            estacion_origen, estacion_destino))
        textoResultado0['text'] = "\n" + resultado
    # pass

   # Calculo Algoritmo

   # Presentacion trayecto


# ComboBox

# La separacion en nodos son las diferentes lineas, las estaciones que son transborodos estan en las dos lineas
nodos = ["###Estaciones Linea1 VERDE",
         "Kifissia", "KAT", "Maroussi", "Neratziotissa", "Irini", "Iraklio", "Nea Ionia", "Pefkakia", "Perissos",
         "Ano Patissia", "Aghios Eleftherios", "Katio Patissia", "Aghios Nikolaos", "Attiki", "Victoria", "Omonia",
         "Monastiraki", "Thissio", "Petralona", "Tavros", "Kallithea", "Moschato", "Faliro", "Piraeus",

         "###Estaciones Linea2 ROJA",
         "Aghios Antonios", "Sepolia", "Attiki", "Larissa Station", "Metaxourghio", "Omonia", "Panepistimio",
         "Syntagma", "Akropoli", "Sygrou - Fix", "Neos Kosmos", "Aghios Ioannis", "Dafni", "Aghios Dimitrios",

         "###Estaciones Linea3 AZUL",
         "Egaleo", "Eleonas", "Kerameikos", "Monastiraki", "Syntagma", "Evangelismos", "Megaro Moussikis", "Ambelokipi"
         "Panormou", "Katehaki", "Ethniki Amyna", "Holargos", "Nomismatokopio", "Aghia Paraskevi", "Halandri",
         "Doukissis Plakentias", "Pallini", "Paiania Kantza", "Koropi", "Airport"]

nodosexcep = ["Doukissis Plakentias", "Pallini",
              "Paiania Kantza", "Koropi", "Airport"]
excluir = ["", "###Estaciones Linea1 VERDE", "###Estaciones Linea2 ROJA",
           "###Estaciones Linea3 AZUL"]  # nuevo###########

combo1 = ttk.Combobox(ventana, state="readonly", width=25,
                      values=nodos, textvariable=estacion_origen)
combo1.place(x=800, y=40)
#combo1.current(0)# ########nuevo, lo comento###########

combo2 = ttk.Combobox(ventana, state="readonly", width=25,
                      values=nodos, textvariable=estacion_destino)
combo2.place(x=980, y=40)
#combo2.current(0) # ########nuevo, lo comento###########


dias = ["Lunes", "Martes", "Miercoles", "Jueves",
        "Viernes", "Sabado", "Domingo"]  # nuevo###########

combo3 = ttk.Combobox(ventana, state="readonly", width=10,
                      values=dias, textvariable=dia_semana)  # modificado###########
combo3.place(x=800, y=100)
combo3.current(0)

tramos = ["De 05:30 a 06:10", "De 06:10 a 20:30", "De 20:30 a 22:00",
          "De 22:00 a 23:30", "De 23:30 a 24:00", "De 24:00 a 02:00"]  # nuevo###########

combo4 = ttk.Combobox(ventana, state="readonly", width=15, values=tramos,
                      textvariable=tramo_horario)  # modificado###########
combo4.place(x=980, y=100)
# si no introduce nada se inicializa al horario diurno mas amplio de 6:10 a  20:30  nuevo
combo4.current(1)

# botones
boton1 = tk.Button(ventana, text="Cacular Ruta", command=calcular,
                   width=20, height=2)  # modificado###########
boton1.pack()
boton1.place(x=1000, y=200)
boton1.config(fore="red")


boton3 = tk.Button(ventana, text="Salir", command=salir,
                   width=7, height=1, fg="green")  # nuevo###########
boton3.pack()
boton3.place(x=1000, y=600)
boton3.config(fore="red")

# Etiquetas
etiqueta1 = tk.Label(ventana, text="Selecciona Origen:", fg="blue")
etiqueta1.pack()
etiqueta1.place(x=800, y=10)

etiqueta2 = tk.Label(ventana, text="Selecciona Destino:", fg="blue")
etiqueta2.pack()
etiqueta2.place(x=980, y=10)

# nuevo############
etiqueta3 = tk.Label(ventana, text="Selecciona Dia de la semana:", fg="blue")
etiqueta3.pack()
etiqueta3.place(x=800, y=80)

etiqueta4 = tk.Label(ventana, text="Selecciona Franja Horaria",
                     fg="blue")  # nuevo############
etiqueta4.pack()
etiqueta4.place(x=980, y=80)

# siempre es la ultima instruccion del programa:
ventana.mainloop()
