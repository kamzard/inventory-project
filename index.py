from io import *

#opciones
main_options=int(input(' 1. para crear nuevo objeto \n 2. para editar un objeto \n 3. para borra un objeto \n 4. para leer objetos guardados \n Introdusca un Numero:'))

#Funcion Guardar Objetos
def save_objet(self,inname,inprice):
    archive_text=open("objetos_inventario.txt", "r+")
    lista_texto=inname,inprice

    archivo_texto.seek(0)

    archivo_texto.writelines(objetos_inventario)

    archivo_texto.close()

if main_options==1:

    inname=input('Nombre del objeto: ')
    inprice=input('Precio: ')
    save_objet(inname,inprice)