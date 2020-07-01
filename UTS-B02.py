#INICIO DEL PROGRAMA
print("---------------------------------------------\n\t\t   MENÚ\n\033[1mDATOS DE PACIENTES INFECTADOS POR EL COVID-19\033[0m\n[1] -> Nuevo Registro de Datos\n[2] -> Mostrar Datos\n[3] -> Eliminar Registros Obtenidos\n---------------------------------------------")
opcion = int(input("Digite una opción: "))
while not opcion in (1,2,3):
    opcion=int(input("\033[91mSistema: Se ha producido un error interno al-\nintentar procesar la opción digitada.\033[0m\n\nDigite una opción válida: "))
    if opcion in (1,2,3):
        print("\033[92mSistema: La opción digitada ha sido procesada\nexitosamente.\033[0m")
print("---------------------------------------------")

#PROCESOS DEL PROGRAMA
if opcion == 1:
    datos=int(input("Ingrese el numero de pacientes : "))
    while not datos>0:
        datos=int(input("\033[91mSistema: Se ha producido un error interno al-\nintentar procesar el número de pacientes digi\ntado.\033[0m\n\nIngrese el numero de pacientes : "))
        if datos>0:
            print ("\033[92mSistema: El número de pacientes digitado ha s\nido procesado exitosamente.\033[0m")
    with open("tfinal.csv","a") as archivo:
        for i in range(datos):
            nombre = str(input("---------------------------------------------\n\033[1m\t       NUEVO REGISTRO DE DATOS\033[0m\nNombres del paciente: "))
            apellido = str(input("Apellidos del paciente: "))
            edad = int(input("---------------------------------------------\nColocar edad del paciente: "))
            while not edad >=0:
                edad = int(input(f"\033[91mSe ha producido un error interno al intentar \nprocesar la edad de {nombre} {apellido}.\033[0m\n\nIngrese una edad válida: "))
                if edad >=0:
                    print("\033[92mLa edad ingresada ha sido procesada exitosame\nnte.\033[0m")
            direccion = str(input("---------------------------------------------\nDirección: "))
            telefono = int(input("Colocar el telefono del paciente : "))
            sexo= str(input("Sexo del paciente : "))
            nacimiento = str(input("Fecha de nacimiento: "))
            recom=str(input("Recomendaciones para el paciente: "))
        print ("\033[93mSistema: Se han registrado los datos del pac\niente exitosamente.\033[0m")
        archivo.write(str(i))
        archivo.close()

elif opcion == 2:
    print("\t     \033[1mMOSTRAR REGISTROS\033[0m")
    with open("tfinal.csv","r") as archivo:
        print (archivo.read())
        archivo.close()
elif opcion == 3:
    print("\t\033[1mELIMINAR REGISTROS OBTENIDOS\033[0m")
    with open("tfinal.csv","a") as archivo:
        archivo.truncate(0) #ELIMINAR DATOS.
        print ("\033[93mSistema: Los registros existentes han sido el\niminados exitosamente.\033[0m")
        archivo.close()
print("--------------------------------------------")



