#MÓDULOS
import os, sys

#COLORES
class COLOR:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#INTERFAZ
print(f"---------------------------------------------\n\t\t   MENÚ\n{COLOR.BOLD}DATOS DE PACIENTES INFECTADOS POR EL COVID-19{COLOR.END}\n[1] -> Nuevo Registro de Datos\n[2] -> Mostrar Datos\n[3] -> Eliminar Registros Obtenidos\n---------------------------------------------")

#SELECCIÓN
opcion = int(input("Digite una opción: "))
while not opcion in (1, 2, 3):
    opcion=int(input(f"{COLOR.RED}Sistema: Se ha producido un error interno al-\nintentar procesar la opción digitada.{COLOR.END}\n\nDigite una opción válida: "))
    if opcion in(1, 2, 3):
        print(f"{COLOR.GREEN}Sistema: La opción digitada ha sido procesada\nexitosamente.{COLOR.END}")
print("---------------------------------------------")

#REGISTRO
if opcion == 1:
    datos=int(input("Digite el número de pacientes a registrar: "))
    while not datos>0:
        datos=int(input(f"{COLOR.RED}Sistema: Se ha producido un error interno al-\nintentar procesar el número de pacientes digi\ntado.{COLOR.END}\n\nIngrese el numero de pacientes : "))
        if datos>0:
            print (f"{COLOR.GREEN}Sistema: El número de pacientes digitado ha s\nido procesado exitosamente.{COLOR.END}")
    with open('tfinal.csv','w') as archivo:
        for i in range(int(datos)):
            nombre = str(input(f"---------------------------------------------\n\t  NUEVO REGISTRO DE DATOS\n{COLOR.BOLD}\t\t    PACIENTE ({i+1}){COLOR.END}\nNombres: "))
            apellido = str(input("Apellidos: "))
            edad = int(input("---------------------------------------------\nEdad: "))
            while not edad >=0:
                edad = int(input(f"{COLOR.RED}Se ha producido un error interno al intentar-\nprocesar la edad de {nombre} {apellido}.{COLOR.END}\n\nIngrese una edad válida: "))
                if edad >=0:
                    print(f"{COLOR.GREEN}La edad ingresada ha sido procesada exitosame\nnte.{COLOR.END}")
            direccion = str(input("---------------------------------------------\nDirección: "))
            telefono = int(input("---------------------------------------------\nTeléfono: +51 9"))
            while not (len(str(telefono))==8 and telefono>0):
                telefono = int(input(f"{COLOR.RED}Se ha producido un error interno al intentar\nprocesar el número telefónico del paciente.{COLOR.END}\n\nIngrese un teléfono válido: +51 9"))
                if len(str(telefono))==8 and telefono>0:
                    print(f"{COLOR.GREEN}El número de teléfono ingresado ha sido proce\nsado exitosamete.{COLOR.END}\n---------------------------------------------")
            sexo= str(input("Sexo: "))
            while not (sexo=="Hombre" or sexo=="Mujer"):
                sexo = str(input(f"{COLOR.RED}mSe ha producido un error interno al intentar-\nprocesar el sexo del paciente.{COLOR.END}\n\nIngrese un sexo válido: "))
                if sexo=="Hombre" or sexo=="Mujer":
                    print(f"{COLOR.GREEN}El sexo ingresado ha sido procesado exitosame\nnte.{COLOR.END}\n---------------------------------------------")
            nacimiento = str(input("Fecha de nacimiento (dd-mm-aa): "))
            while not len(nacimiento)==8:
                nacimiento = str(input(f"{COLOR.RED}Se ha producido un error interno al intentar-\nprocesar la fecha de nacimiento del paciente.{COLOR.END}\n\nIngrese una fecha de nacimiento válida utilizando el formato (dd-mm-aa): "))
                if len(nacimiento)==8:
                    print(f"{COLOR.GREEN}La fecha de nacimiento ingresada ha sido proc\nesada exitosamente.{COLOR.END}\n---------------------------------------------")
            recom=str(input("Recomendaciones: "))
            print(f"---------------------------------------------\n{COLOR.YELLOW}Sistema: Se han registrado los datos del paci\nente exitosamente.{COLOR.END}")
            archivo.write(f"Nombre: {nombre}\nApellido: {apellido}\nEdad: {edad}\nDirección: {direccion}\nTeléfono: {telefono}\nSexo: {sexo}\nFecha de nacimiento: {nacimiento}\nRecomendaciones: {recom}")
        archivo.close()

#VISUALIZACIÓN
elif opcion == 2:
    print("\t     MOSTRAR REGISTROS\n\t\t\033[1mPACIENTE(S)\033[0m")
    with open("tfinal.csv",'r') as archivo:
        if os.path.getsize("tfinal.csv")==0:
            print(f"{COLOR.YELLOW}Sistema: No se ha encontra ningún registro pa\nra mostrar.{COLOR.END}")
        else: 
            print(archivo.read())
            archivo.close()
#ELIMININACIÓN
else:
    print(f"\t{COLOR.BOLD}ELIMINAR REGISTROS OBTENIDOS{COLOR.END}")
    with open("tfinal.csv",'a') as archivo:
        if os.path.getsize("tfinal.csv")==0:
            print(f"{COLOR.YELLOW}Sistema: No se ha encontrado ningún registro-\npara borrar.{COLOR.END}")
        else:
            archivo.truncate(0)
            print (f"{COLOR.YELLOW}Sistema: Los registros existentes han sido el\niminados exitosamente.{COLOR.END}")
            archivo.close()
print("---------------------------------------------")