#MÓDULOS 
from colorama import init, Fore, Back, Style
import os
init(autoreset=True)
#INTERFAZ
print("---------------------------------------------"+Fore.YELLOW+"\n\t\t   FILL19"+Fore.RESET+"\n\t    MENÚ DE HERRAMIENTAS"+Fore.RESET+"\n---------------------------------------------"+"\n[1] -> Nuevo Registro\n[2] -> Mostrar Registro\n[3] -> Editar Registro\n[4] -> Limpiar Registro\n[5] -> Borrar Registro\n[6] -> Salir\n---------------------------------------------")

#SELECCIÓN
opcion = int(input("Digite una opción: "))
while not opcion in (1, 2, 3, 4, 5, 6):
    print(Fore.RED+Back.WHITE+"Sistema: Se ha producido un error interno al intentar procesar la opción digitada.")
    opcion=int(input("Digite una opción válida: "))
    if opcion in(1, 2, 3, 4, 5, 6):
        print(Fore.GREEN+"Sistema: La opción digitada ha sido procesada exitosamente.")
print("---------------------------------------------")

#REGISTRO
if opcion == 1:

    #GENERACIÓN
    name=str(input("Ingresa un nombre para el registro: "))
    docu=name+".csv"

    if os.path.exists(docu):
        print(Fore.RED+f"Sistema: El archivo ({docu}) ya existe.")
    
    else:
        #PACIENTES
        datos=int(input("Digite el número de pacientes a registrar: "))

        #CONDICIÓN
        while not datos>0:
            print(Fore.RED+Back.WHITE+"Sistema: Se ha producido un error interno al intentar procesar el número de pacientes digitado.")
            datos=int(input("Ingrese el numero de pacientes : "))
            if datos>0:
                print (Fore.GREEN+"Sistema: El número de pacientes digitado ha sido procesado exitosamente.")
        
        #ESCRITURA
        with open(docu,'w') as archivo:
            for i in range(int(datos)):
                nombre = str(input("---------------------------------------------"+Fore.YELLOW+"\n\t       NUEVO REGISTRO"+Fore.RESET+f"\n\t        PACIENTE ({i+1})\nNombres: "))
                apellido = str(input("Apellidos: "))
                edad = int(input("---------------------------------------------\nEdad: "))
                while not edad >=0:
                    print(Fore.RED+Back.WHITE+"Se ha producido un error interno al intentar procesar la edad de" + nombre + apellido )
                    edad = int(input(f"Ingrese una edad válida: "))
                    if edad >=0:
                        print(Fore.GREEN+"La edad ingresada ha sido procesada exitosamente.\n")
                direccion = str(input("---------------------------------------------\nDirección: "))
                telefono = int(input("---------------------------------------------\nTeléfono: +51 9"))
                while not (len(str(telefono))==8 and telefono>0):
                    print(Fore.RED+Back.WHITE+"Se ha producido un error interno al intentar procesar el número telefónico de"+ nombre + apellido )
                    telefono = int(input("Ingrese un teléfono válido: +51 9"))
                    if len(str(telefono))==8 and telefono>0:
                        print(Fore.GREEN+"El número de teléfono ingresado ha sido procesado exitosamete.\n---------------------------------------------")
                sexo= str(input("Sexo: "))
                while not (sexo=="Masculino" or sexo=="Femenino"):
                    print(Fore.RED+"Se ha producido un error interno al intentar procesar-\nel sexo de " + nombre + apellido)
                    sexo = str(input("Ingrese un sexo válido: "))
                    if sexo=="Masculino" or sexo=="Femenino":
                        print(Fore.GREEN+"El sexo ingresado ha sido procesado exitosame\nnte."+Fore.RESET+"\n---------------------------------------------")
                nacimiento = str(input("Fecha de nacimiento (dd-mm-aa): "))
                while not len(nacimiento)==8:
                    print(Fore.RED+Back.WHITE+"Se ha producido un error interno al intentar procesar la fecha de nacimiento de " + nombre + apellido )
                    nacimiento = str(input("Ingrese una fecha de nacimiento válida utilizando el formato (dd-mm-aa): "))
                    if len(nacimiento)==8:
                        print(Fore.GREEN+"La fecha de nacimiento ingresada ha sido procesada exitosamente.\n---------------------------------------------")
                recom=str(input("Recomendaciones: "))
                print("---------------------------------------------"+Fore.GREEN+"\nSistema: Se han registrado los datos del paci\nente exitosamente."+Fore.RESET)
                archivo.write(f"Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nDirección: {direccion}\nTeléfono: {telefono}\nSexo: {sexo}\nFecha de nacimiento: {nacimiento}\nRecomendaciones: {recom}\n")

#VISUALIZACIÓN
elif (opcion == 2):   
    print(Fore.YELLOW+"\t      MOSTRAR REGISTRO"+Fore.RESET+"\n\t\t PACIENTE(S)\n---------------------------------------------")

    #GENERACIÓN
    name=str(input("Ingrese el nombre del archivo: "))
    print("---------------------------------------------")
    docu=name+".csv"
    if os.path.exists(docu):
        with open(docu,'r') as archivo:
            if os.path.getsize(docu)==0:
                print(Fore.RED+"Sistema: No se ha encontra ningún registro pa\nra mostrar.")
            else:
                print(archivo.read())
    else:
        print(Fore.RED+f"Sistema: No se ha encontrado el archivo ({docu}).")


#EDICIÓN
elif (opcion == 3):
    print(Fore.YELLOW+"\t      EDITAR REGISTRO"+Fore.RESET+"\n\t\tPACIENTE(S)\n")

    #GENERACIÓN
    sele=str(input("Ingrese el nombre del archivo: "))
    tuto=sele+".csv"
    if os.path.exists(tuto):
        #PACIENTES
        datos=int(input("Digite el número de pacientes a registrar: "))
        #CONDICION
        while not datos>0:
            print(Fore.RED+Back.WHITE+"Sistema: Se ha producido un error interno al intentar procesar el número de pacientes digitado.")
            datos=int(input("Ingrese el numero de pacientes : "))
            #CONDICION
            if datos>0:
                print (Fore.GREEN+"Sistema: El número de pacientes digitado ha sido procesado exitosamente.")

    
        with open(tuto,'a') as tutorial:
            for i in range(int(datos)):
                nombre = str(input("---------------------------------------------"+Fore.YELLOW+"\n\t       NUEVO REGISTRO"+Fore.RESET+f"\n\t        PACIENTE ({i+1})\nNombres: "))
                apellido = str(input("Apellidos: "))
                edad = int(input("---------------------------------------------\nEdad: "))
                while not edad >=0:
                    print(Fore.RED+Back.WHITE+"Se ha producido un error interno al intentar procesar la edad de" + nombre + apellido )
                    edad = int(input(f"Ingrese una edad válida: "))
                    if edad >=0:
                        print(Fore.GREEN+"La edad ingresada ha sido procesada exitosamente.\n")
                direccion = str(input("---------------------------------------------\nDirección: "))
                telefono = int(input("---------------------------------------------\nTeléfono: +51 9"))
                while not (len(str(telefono))==8 and telefono>0):
                    print(Fore.RED+Back.WHITE+"Se ha producido un error interno al intentar procesar el número telefónico de"+ nombre + apellido )
                    telefono = int(input("Ingrese un teléfono válido: +51 9"))
                    if len(str(telefono))==8 and telefono>0:
                        print(Fore.GREEN+"El número de teléfono ingresado ha sido procesado exitosamete.\n---------------------------------------------")
                sexo= str(input("Sexo: "))
                while not (sexo=="Hombre" or sexo=="Mujer"):
                    print(Fore.RED+f"Se ha producido un error interno al intentar\nprocesar el sexo del paciente")
                    sexo = str(input("Ingrese un sexo válido: "))
                    if sexo=="Hombre" or sexo=="Mujer":
                        print(Fore.GREEN+"El sexo ingresado ha sido procesado exitosame\nnte.\n---------------------------------------------")
                nacimiento = str(input("Fecha de nacimiento (dd-mm-aa): "))
                while not len(nacimiento)==8:
                    print(Fore.RED+Back.WHITE+"Se ha producido un error interno al intentar procesar la fecha de nacimiento de " + nombre + apellido )
                    nacimiento = str(input("Ingrese una fecha de nacimiento válida utilizando el formato (dd-mm-aa): "))
                    if len(nacimiento)==8:
                        print(Fore.GREEN+"La fecha de nacimiento ingresada ha sido procesada exitosamente.\n---------------------------------------------")
                recom=str(input("Recomendaciones: "))
                print("---------------------------------------------"+Fore.GREEN+"\nSistema: Se han registrado los datos del paci\nente exitosamente."+Fore.RESET)
                tutorial.write(f"\nNombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nDirección: {direccion}\nTeléfono: {telefono}\nSexo: {sexo}\nFecha de nacimiento: {nacimiento}\nRecomendaciones: {recom}")
    else:
        print(Fore.RED+f"Sistema: No se ha encontrado el archivo ({tuto}).")

#LIMPIEZA
elif (opcion == 4):
    print(Fore.YELLOW+"\t      LIMPIAR REGISTRO"+Fore.RESET+"\n\t\t PACIENTE(S)\n---------------------------------------------")

    #GENERACIÓN
    name=str(input("Ingrese el nombre del archivo: "))
    docu=name+".csv"
    if os.path.exists(docu) and (os.path.getsize(docu)>=0): #CAMBIOS
        if os.path.getsize(docu)==0:
            print(Fore.RED+f"Sistema: No se ha encontrado nada que limpiar\nen el archivo ({docu}).")
        else:
            with open(docu,'w') as archivo:
                archivo.truncate(0)
                print (Fore.GREEN+f"Sistema: El archivo ({docu}) ha sido-\nlimpiado exitosamente.")

    else:
        print(Fore.RED+f"Sistema: No se ha encontrado el archivo ({docu}).") 
              

#BORRADO
elif (opcion == 5):
    print(Fore.YELLOW+"\t       BORRAR REGISTRO"+Fore.RESET+"\n\t\t PACIENTE(S)\n---------------------------------------------")
    name=str(input("Ingrese el nombre del archivo: "))
    docu=name+".csv"
    if os.path.exists(docu):
        os.remove(docu)
        print (Fore.GREEN+f"Sistema: El archivo ({docu}) ha sido-\neliminado exitosamente.")


    else:
        print(Fore.RED+f"Sistema: No se ha encontrado el archivo ({docu}).")

#SALIR
else:
    print(Fore.GREEN+"Sistema: El programa ha finalizado exitosamente.")

#FIN
print("---------------------------------------------")