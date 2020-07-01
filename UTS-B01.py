#INICIO
print("---------------------------------------------\n\t\t   MENÚ\n\033[1mDATOS DE PACIENTES INFECTADOS POR EL COVID-19\033[0m\n[1] -> Nuevo Registro de Datos\n[2] -> Mostrar Datos\n[3] -> Eliminar Registros Obtenidos\n---------------------------------------------")
opcion = int(input("Digite una opción: "))
while not opcion in (1,2,3):
    opcion=int(input("\033[91mSe produjo un error interno al intentar proce\nsar la opción digitada.\033[0m\n\nDigite una opción válida: "))
if opcion in (1,2,3):
    print("\033[92mLa opción digitada ha sido procesada exitosam\nente.\033[0m")
print("---------------------------------------------")

#PROCESO
if opcion == 1:

    datos=int(input("Ingrese el numero de pacientes : "))
    while not datos>0:
        datos=int(input("\033[91mSe ha producido un error interno al intentar \nprocesar el número de pacientes digitado.\033[0m\n\nIngrese el numero de pacientes : "))

    if datos>0:
        print ("\033[92mEl número de pacientes digitado ha sido proce\nsado exitosamente.\033[0m\n---------------------------------------------\n\033[1m\t       NUEVO REGISTRO DE DATOS\033[0m")
        with open("tfinal.csv","a") as archivo:
            for i in range(datos):
                nombre = str(input("Nombres del paciente : "))
                apellido = str(input("Apellidos del paciente: "))
                edad = int(input("Colocar edad del paciente: "))
                while not edad >=0:
                    edad = int(input(f"---------------------------------------------\n\033[91mSe ha producido un error interno al intentar \nprocesar la edad de {nombre} {apellido}.\033[0m\n---------------------------------------------\nIngrese una edad válida: "))
                direccion = str(input("Dirección: "))
                telefono = int(input("Colocar el telefono del paciente : "))
                sexo= str(input("Sexo del paciente : "))
                nacimiento = str(input("Fecha de nacimiento: "))
                recom=str(input("Recomendaciones para el paciente: "))
    
            print ("Se han registrado los datos del paciente exitosamente")
            archivo.write(i)
            archivo.close()
elif opcion == "2":
    print ("Mostrar Registros")
    with open("tfinal.csv","r") as archivo:
       
        print (archivo.read())
        archivo.close()
elif opcion == "3":
    with open("tfinal.csv","a") as archivo:
        
        archivo.truncate(0) #ELIMINAR DATOS.
        print ("Registros Eliminados")
        archivo.close()



