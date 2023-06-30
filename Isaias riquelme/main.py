from Atencion import *
import random
indice=0
imprimir_lista=[]
ciclo=True
while ciclo:
    print("Mechas Locas")
    print("==========================")
    print("1) Grabar")
    print("2) Buscar")
    print("3) Imprimir atencion")
    print("4) Salir")
    print("--------------------------")
    op=int(input("Seleccione (1-4):"))
    print("--------------------------")
    try:
        match op:
            case 1:
                a=Atencion()
                c=False
                while c==False:
                    c_atencion=input("Ingrse codigo de atencion:")
                    c= a.setC_atencion(c_atencion)
                c=False
                while c==False:
                    nombre=input("Ingrese nombre del cliente:")
                    c= a.setNombre(nombre)
                c=False
                while c==False:
                    costo=int(input("Ingrese costo de la cita:"))
                    c= a.setCosto(costo)
                c=False
                while c==False:
                 descripcion=input("Ingrese descripcion de la cita:")
                 c= a.setDescripcion(descripcion)


                a.numero = indice +1
                indice += 1
                a.c_atencion=input("Ingrese codigo de atencion para agregar a lista:")
                imprimir_lista.append(a)
                print(f"Cita agregada N°{indice}")
                print("============================")

            case 2:
                if not imprimir_lista:
                    print("no se encontro en la lista")
                else:
                    print("Buscar cita")
                    print("===================")
                    c_atencion_buscar=input("Ingrse codigo de atencion del cliente")
                    cita_encontrada= None

                    for Atencion in imprimir_lista:
                        if Atencion.c_atencion==c_atencion_buscar:
                            cita_encontrada=Atencion
                        break
                    if cita_encontrada:
                        print("cita encontrada...")
                        print("==================")
                        print("Codigo de atencion:",cita_encontrada.c_atencion)
                        print("nombre del cliente:",cita_encontrada.nombre)
                        print("costo de atencion:",cita_encontrada.costo)
                        print("descripcion de la atencion:",cita_encontrada.descripcion)
                        print("==================")
            case 3:
                print("impresion de la atencion")
                print("1) Boleta:")
                opcion=int(input("Seleccione opcion:"))

                if opcion==1:
                    print("Boleta de atencion")
                    print("=======================================")
                    for item in imprimir_lista:
                        print("Codigo de atencion:",item.c_atencion)
                        print("Nombre del cliente:", item.nombre)
                        print("Costo de la atencion:", item.costo)
                        print("Descripcion dada:", item.descripcion)
                        informe_propina = random.randint(1000, 2000)
                        print("propina dada:", informe_propina)
                        print("===============")
                        print("Imprimir boleta")
                        print("===============")


            case 4:
                print("Salir")
                print("Isaias Riquelme")
            case _:
                print("opciona invalida")
    except BaseException as error:
        print(f"error{error}")
