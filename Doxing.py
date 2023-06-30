#!/usr/bin/env python3
# CREATED BY: Hacker nodo
import os
from comorama import init, Fore, Style
init()

def modo_uso():
    print("""el uso de este escript es 1 tener el nombre y por lo menos un apellido de la persona
    o la patente de la persona a investigar
    2 ponerlos en rutificador saber la parte donde vive si en este caso no tienes el nombre completo
    si encuentras la info que buscas\npcopir el rut o guardar ne las notas toda la ifo sacada\ny buscar en el registro de certificados con una cuenta inventada\n
    sacar algun certificado de el ya que tendras el rut de el y la cuenta craeda de gmail \n3 si no tienes el nombre y la patente poner el eutofac y sacar la info\n
    LA IDEA DE ESTE SCRIPT ES SACAR LA INFO PASANDO POR TODOS LOS LINK DE USO PARA PODER JUNTAR LA MAYOT INFORMACION POSIBLE

          """)


def nota():
    print("                       Crear nota para guardar informacion optenida  \n\n")
    datos = input("Ingresa datos copiados: ")
    with open("informacion.txt","a") as con:
        con.write(datos,"\n\n")
        print("datos guardados con exito!!")
        return menu()

def ver():
    print("Datos guardados son:")
    os.system("cat informacion.txt")
    return menu()



def menu():
    while True:
        print(Fore.GREEN_EX+"""                   ###################################
        >>>>>>>>>>>                || CHILE V1 CREADOR: Hans Saldias||               <<<<<<<<<<<<<<<<
                                   ###################################


                                ######################################### 
                   >>>>>>>>>>   || Doxing NoDo busqueda de informacion ||   <<<<<<<<<<<<<<<<<<
                                ######################################### 


                                               #################
                                          [1]  || Rutificador ||
                                               #################
    
                                               ##################
                                          [2]  || certificados ||
                                               ##################
    
                                                  #############
                                             [3]  || Autofac ||
                                                  #############
    
                                             #####################
                                        [4]  || OSINT framework ||
                                             #####################
    
                                           #########################
                                      [5]  || Numeros telefonicos ||
                                           #########################
    
                                          ############################
                                    [6]  || Dominios y direcciones ||
                                         ############################
    
                                           #############################
                                      [7]  || MODO DE USO HERRAMIENTA ||
                                           #############################
                                      
                                           #############################
                                      [8]  || crear nota para guardar ||
                                           #############################
                                      
                                           #########################
                                      [9]  || ver datos guardados ||
                                           #########################
                                      
                                                    ###########
                                               [0]  || Salir ||
                                                    ###########
        """)

        op = int(input("Ingresa la opcion: "))

        if op == 1:
            os.system("termux-open https://www.nombrerutyfirma.com")
        elif op == 2:
            os.system("termux-open https://www.registrocivil.cl/principal/servicios-en-linea")
        elif op == 3:
            os.system("termux-open https://www.autofac.cl/consultar-patente-auto#input-free-report")
        elif op == 4:
            os.system("termux-open https://osintframework.com/")
        elif op == 5:
            os.system("termux-open https://www.whitepages.com/reverse-phone")
        elif op == 6:
            os.system("termux-open https://who.is/")
        elif op == 7:
            modo_uso()
        elif op == 8:
            nota()
        elif op == 0:
            print("creador: Hacker NoDo .... gracias")
            break
        elif op == 9:
            ver()
        else:
            print("No se pudo ejecutar")














menu()