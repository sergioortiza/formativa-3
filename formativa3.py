import os
import time
import csv
cls=("cls")

def registro():
    nombre=input("Ingrese el nombre del trabajador: ")
    cargo=input("Ingrese que cargo posee el trabajador: ")
    sueldo=float(input("Ingrese el sueldo bruto del trabajador: "))
    salud=round(sueldo*0.07 )
    afp=round(sueldo*0.12)
    liquido=round(sueldo- salud- afp)
    return nombre, cargo, sueldo, salud, afp, liquido
    

def trabajador(nombre, cargo, sueldo, salud, afp, liquido, archivo_csv = 'Trabajadores2.csv'):
    with open(archivo_csv, 'a', newline='') as archivo:
        campos= ['Nombre', 'Cargo', 'Sueldo', 'Desc.Salud', 'AFP', 'Liquido']
        escritor_cvs =csv.DictWriter(archivo, fieldnames = campos)

        if archivo.tell()== 0:
            escritor_cvs.writeheader()

        escritor_cvs.writerow({
            'Nombre': nombre,
            'Cargo': cargo,
            'Sueldo': sueldo, 
            'Desc.Salud': salud,
            'AFP': afp,
            'Liquido': liquido
        })



def mostrar1(archivo_csv= 'Trabajadores2.csv'):
    with open(archivo_csv, 'r', newline='') as archivo:
        lector_csv = csv.reader(archivo)
        next(lector_csv)
        print(" Nombre Trabajadores ")
        for fila in lector_csv:
            print(f"Nombre trabajador: {fila[0]}")

def mostrar2(archivo_csv= 'Trabajadores2.csv'):
    with open(archivo_csv, 'r', newline='') as archivo:
        lector_csv = csv.reader(archivo)
        
        next(lector_csv)
        try:
            print(" Plantilla sueldos ")
            print("1. Plantilla todos los trabajadores")
            print("2. Planilla de cargos especificos")
            opc2=int(input("Ingrese una opcion "))
        except ValueError:
            print("Ingrese solo numeros")
        if opc2 >=1 and opc2 <=2:
            if opc2 ==1:
                print("Mostrando todas las plantillas: ")
                for fila in lector_csv:
                    print(f"Nombre trabajador: {fila[0]}", '\n', f"Cargo: {fila[1]}", '\n', f"Sueldo: {fila[2]}", '\n', f"Desc.Salud: {fila[3]}", '\n', f"AFP: {fila[4]}", '\n', f"Liquido: {fila[5]}")
                    print("*"*40)
                    continue
        
            if opc2==2:
                busca_cargo=input("Ingrese el nombre del cargo: ")
                cargoencontrado= False 
                for fila in lector_csv:
                    if fila[1]== busca_cargo:
                        print(f"Nombre: {fila[0]}", '\n', f"Cargo: {fila[1]}", '\n', f"Sueldo: {fila[2]}", '\n', f"Desc.Salud: {fila[3]}", '\n', f"AFP: {fila[4]}", '\n', f"Liquido: {fila[5]}")
                        print('*'*24)
                        cargoencontrado= True 
                    if not cargoencontrado:
                        print(f"Cargo: {busca_cargo} no encontrado")
                        continue

                

def menu():
    os.system(cls)
    while True:
        try:
            print('*'* 20)
            print("Bienvenido al administrador de Trabajadores")
            print("1. Registrar trabajador")
            print("2. Listar todos los trabajadores ")
            print("3. Imprimir plantilla de sueldos ")
            print("4. Salir")
            opc=int(input("Ingrese una opcion: "))
        except ValueError:
            print("Ingrese solo numeros")
        if opc <= 4 and opc >= 1:
            if opc ==1:
                print("Bienvenido al Registro de trabajadores")
                try:
                    cant=int(input("Cuantos trabajadores desea registrar?: "))
                    for i in range(cant):
                        nombre, cargo, sueldo, salud, afp, liquido= registro()
                        trabajador(nombre, cargo, sueldo, salud, afp, liquido)
                        print("El trabajador Fue regisrado en Trabajadores2.csv")
                except ValueError:
                    print("Ingrese solo numeros")
            if opc ==2:
                
                print("Mostrando Plantila Trabajadores:")
                mostrar1()
                print("Espere 3 segundos")
                time.sleep(3)
                continue
            if opc ==3:
                os.system(cls)
                mostrar2()
                print("Espere 3 segundos")
                time.sleep(3)
            if opc ==4: 
                print("Cerrando programa")
                break




menu()