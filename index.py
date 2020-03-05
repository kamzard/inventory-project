import os
import os.path


#Comprobacion archivo de texto, en dado caso que no exista o este fuera borrado se creara uno nuevo
if os.path.isfile("objetos.txt"):
    pass
else:
    f = open ('objetos.txt','w')
    f.write('Producto , Unidades de Producto, Valor de cada producto\n')
    f.close()
    
#funciones basicas del programa
def agregarproducto(nombre,cantidad,valorunit):
    f = open ('objetos.txt','a')
    f.write('\n' + nombre)
    f.write(',' + cantidad)
    f.write(',' + valorunit)
    f.close()

def leerobjetos():
    f = open ('objetos.txt','r')
    mensaje = f.read()
    print(mensaje)
    f.close()
    
def formateararchivo():    
    f = open ('objetos.txt','w')
    f.seek(0)
    f.truncate()
    f.write('Productos,Cantidad de Productos,Valor de cada producto\n')
    f.close()

#Inicio del programa
print("Bienvenido al sistema de almacen\n")
bucle=0

while bucle==0:

    opciones=int(input('Coloque 1 para agregar nuevo producto \nColoque 2 para leer productos guardados \nColoque 3 para borrar todo el contenido del archivo \nColoque 4 para salir del programa \n Que desea hacer?:'))
    
    if opciones==1:
        nombre=input('Nombre del producto: ')
        cantidad=input('Introdusca la cantidad de productos de entrada: ')
        valorunit=input('Introdusca el valor por unidad del producto: ')        
        agregarproducto(nombre,cantidad,valorunit)
        loop2=0
        while loop2==0:
            decision=int(input('Desea agregar otro producto?\n Coloque 1 para si \n Coloque 2 para no \n Que desea hacer: '))
            
            if decision==1:
                nombre=input('Nombre del producto: ')
                cantidad=input('Introdusca la cantidad de productos de entrada: ')
                valorunit=input('Introdusca el valor por unidad del producto: ')        
                agregarproducto(nombre,cantidad,valorunit)

            elif decision==2:
                break

            else:
                decision=int(input('Opcion invalida intente de nuevo: '))

    elif opciones==2:
        leerobjetos()
        limpiarconsola=int(input('Desea continuar limpiando la consola? \n Coloque 1 para si \n Coloque 2 para no\n Que desea hacer: '))
        
        if limpiarconsola==1:
            clear = lambda: os.system('cls')
            clear()

        elif limpiarconsola==2:
            pass
    
        else:
            limpiarconsola=int(input('Opcion invalida intente de nuevo: '))

    elif opciones==3:
        formateararchivo()

    elif opciones==4:
        break

    else:
        print('\n Error, seleccione una opcion valida: \n')
        
