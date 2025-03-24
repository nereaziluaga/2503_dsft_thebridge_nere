import pprint #1- primero se ponen todos los imports
import os
import time

     
# 2- DEFINIMOS LAS FUNCIONES
def imprimir_libros(libros):
    return pprint.pprint (libros)
# BUSCAR: búsqueda por título que introduce el usuario 
# y se visualizan todos los campos del libro
def buscar_libro(libros):
    titulo_buscar=input("Introduce el título del libro")
    for libro in libros: 
        titulo_buscar=libro["Titulo"]
        print (f"El titulo {titulo_buscar} está disponible en la biblioteca")
# AÑADIR: se debe solicitar al usuario que introduzca título y 
# autor para el nuevo libro y se añade el libro a la lista de libros
def añadir_libro(libros):
    titulo_añadir=input("Introduce el título del libro que quieras añadir")
    autor_añadir=input("Introduce el nomre de la autora del libro que quieras añadir")
    for libro in libros: 
        print (libros.append(titulo_añadir))
        print (libros.append(autor_añadir))
        print (libros)
# ELIMINAR: se solicita al usuario el título del libro 
# y éste debe ser eliminado de la lista de libros
def eliminar_libro(libros):
    titulo_eliminar=input("Introduce el título del libro que quieras eliminar")
    for libro in libros: 
        titulo_eliminar=libro["Titulo"]
        print (f"El titulo {titulo_eliminar} es el que quieres eliminar")
        print (libros.remove(titulo_eliminar))
        print (libros) 
#ALQUILAR: se solicita al usuario el título se debe pasar el campo "Alquilado" a True
def alquilar_libro (libros):
    titulo_alquiler=input("Dime qué libro quieres alquilar")
    for libro in libros:
        if titulo_alquiler==libro["Titulo"]:
            libro["Alquilado"]=True
# DEVOLVER: se solicita al usuario el título del libro 
# y se debe pasar el campo "Alquilado" a False
def devolver_libro (libros):
    pass







libros = [
    {"Titulo": "Python Data Science Handbook", "Autor": "Jake VanderPlas", "Alquilado": False},
    {"Titulo": "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow", "Autor": "Aurélien Géron", "Alquilado": True},
    {"Titulo": "Pattern Recognition and Machine Learning", "Autor": "Christopher M. Bishop", "Alquilado": False},
    {"Titulo": "Deep Learning", "Autor": "Ian Goodfellow, Yoshua Bengio, Aaron Courville", "Alquilado": True},
    {"Titulo": "The Elements of Statistical Learning", "Autor": "Trevor Hastie, Robert Tibshirani, Jerome Friedman", "Alquilado": False},
    {"Titulo": "Data Science for Business", "Autor": "Foster Provost, Tom Fawcett", "Alquilado": False},
    {"Titulo": "Bayesian Data Analysis", "Autor": "Andrew Gelman et al.", "Alquilado": True},
    {"Titulo": "Introduction to the Theory of Computation", "Autor": "Michael Sipser", "Alquilado": False},
    {"Titulo": "Artificial Intelligence: A Modern Approach", "Autor": "Stuart Russell, Peter Norvig", "Alquilado": True},
    {"Titulo": "Computer Vision: Algorithms and Applications", "Autor": "Richard Szeliski", "Alquilado": False},
    {"Titulo": "Data Science from Scratch", "Autor": "Joel Grus", "Alquilado": True},
    {"Titulo": "The Art of Statistics", "Autor": "David Spiegelhalter", "Alquilado": False},
    {"Titulo": "Python Machine Learning", "Autor": "Sebastian Raschka, Vahid Mirjalili", "Alquilado": True},
    {"Titulo": "An Introduction to Statistical Learning", "Autor": "Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani", "Alquilado": False},
    {"Titulo": "Fundamentals of Data Engineering", "Autor": "Joe Reis, Matt Housley", "Alquilado": False},
    {"Titulo": "Storytelling with Data", "Autor": "Cole Nussbaumer Knaflic", "Alquilado": True},
    {"Titulo": "Building Machine Learning Powered Applications", "Autor": "Emmanuel Ameisen", "Alquilado": False},
    {"Titulo": "Practical Statistics for Data Scientists", "Autor": "Peter Bruce, Andrew Bruce", "Alquilado": True},
    {"Titulo": "SQL for Data Scientists", "Autor": "Renee M. P. Teate", "Alquilado": False},
    {"Titulo": "Data Engineering on Azure", "Autor": "Vlad Riscutia", "Alquilado": True}
]

salir = False

while not salir:
    opcion = input("Visualizar/Buscar/Añadir/Alquilar/Devolver/Salir")
    match opcion:
        case "Visualizar":
            imprimir_libros(libros)
        case "Buscar":
            buscar_libro(libros)
        case "Salir":
            salir = True
    time.sleep(5)
    os.system("cls") #esto borra la pantalla
            
            