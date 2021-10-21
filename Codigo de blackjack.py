#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import random
import time

Cartas={"As Corazones ♥":(1,11), "2 Corazones ♥":2, "3 Corazones ♥":3, "4 Corazones ♥":4, "5 Corazones ♥":5, "6 Corazones ♥":6, "7 Corazones ♥":7, "8 Corazones ♥":8, "9 Corazones ♥":9, "10 Corazones ♥":10, "J Corazones ♥":10, "Q Corazones ♥":10, "K Corazones ♥":10, "As Treboles ♣":(1,11), "2 Treboles ♣":2, "3 Treboles ♣":3, "4 Treboles ♣":4, "5 Treboles ♣":5, "6 Treboles ♣":6, "7 Treboles ♣":7, "8 Treboles ♣":8, "9 Treboles ♣":9, "10 Treboles ♣":10, "J Treboles ♣":10, "Q Treboles ♣":10, "K Treboles ♣":10, "As Picas ♠":(1,11), "2 Picas ♠":2, "3 Picas ♠":3, "4 Picas ♠":4, "5 Picas ♠":5, "6 Picas ♠":6, "7 Picas ♠":7, "8 Picas ♠":8, "9 Picas ♠":9, "10 Picas ♠":10, "J Picas ♠":10, "Q Picas ♠":10, "K Picas ♠":10, "As Diamantes ♦":(1,11), "2 Diamantes ♦":2, "3 Diamantes ♦":3, "4 Diamantes ♦":4, "5 Diamantes ♦":5, "6 Diamantes ♦":6, "7 Diamantes ♦":7, "8 Diamantes ♦":8, "9 Diamantes ♦":9, "10 Diamantes ♦":10, "J Diamantes ♦":10, "Q Diamantes ♦":10, "K Diamantes ♦":10}

Nombre_cartas=[carta for carta in Cartas.keys()]

Cartas_Blackjack=["As Corazones ♥", "10 Corazones ♥","J Corazones ♥","Q Corazones ♥","K Corazones ♥","As Treboles ♣","10 Treboles ♣","J Treboles ♣","Q Treboles ♣","K Treboles ♣","As Picas ♠","10 Picas ♠","J Picas ♠","Q Picas ♠","K Picas ♠","As Diamantes ♦","10 Diamantes ♦","J Diamantes ♦","Q Diamantes ♦","K Diamantes ♦"]

dieces=["10 Corazones ♥","10 Treboles ♣","10 Picas ♠","10 Diamantes ♦"]

figuras=["J Corazones ♥","Q Corazones ♥","K Corazones ♥","J Treboles ♣","Q Treboles ♣","K Treboles ♣","J Picas ♠","Q Picas ♠","K Picas ♠","J Diamantes ♦","Q Diamantes ♦","K Diamantes ♦"]

def repartir_carta(lista):
    #Función que reparte cartas a un jugador o a la computadora
    carta=random.choice(lista)
    lista.remove(carta)
    return carta

def simplificar(lista):
    #Función que si obtienes dos As toma la primera con valor 1 siempre
    t=[]
    for i in lista:
        if type(i)==tuple:
            t.append(i)
    
    if len(t)==2:
        lista[lista.index((1,11))]=1
    return(lista)
    
        
def puntuacion(lista):
    #Función que determina el valor que debe darse al As
    p=[]
    for punto in lista:
        if type(punto)==int:
            p.append(punto)
    s=sum(p)        
    for punto in lista:
        if type(punto)==tuple and s<=10:
            p.append(punto[1])
        elif type(punto)==tuple and s>10:
            p.append(punto[0])       
    return sum(p) 



def lista_de_puntos(Dict,lista1,lista2, extra):
    #Función que va agregando el valor de la carta que decide tomar el jugador a la lista de puntos
    
    lista2.append(Dict[lista1[extra.__next__()]])
    return lista2        



def lista_de_puntos1(Dict,lista1,lista2, extra1):
    #Función que va agregando el valor de la carta que decide tomar la computadora a la lista de puntos
    lista2.append(Dict[lista1[extra1.__next__()]])
    return lista2    

def blackjack(lista):
    #Función que determina si un jugador obtuvo un blackjack
    for carta in figuras:
        if sorted(lista)==["As Corazones ♥", carta]:
            return "blackjack"
        elif sorted(lista)==["As Treboles ♣", carta]:
            return "blackjack"
        elif sorted(lista)==["As Picas ♠", carta]:
            return"blackjack" 
        elif sorted(lista)==["As Diamantes ♦", carta]:
            return "blackjack"
    for carta in dieces:
        if sorted(lista)==[carta,"As Corazones ♥"]:
            return "blackjack"
        elif sorted(lista)==[carta,"As Treboles ♣"]:
            return "blackjack"
        elif sorted(lista)==[carta,"As Picas ♠"]:
            return "blackjack"
        elif sorted(lista)==[carta,"As Diamantes ♦"]:
            return "blackjack"
    return "No hay blackjack, continuamos."

def jugar_de_nuevo():
    quieres=input("¿Quieres jugar de nuevo, escribe si o no = ")
    while quieres.lower()!="si" and quieres.lower()!="no":
                print("\n ☠ Solo puedes escribir si o no \n")
                quieres=input("¿Quieres jugar de nuevo, escribe si o no = ")
    time.sleep(0.5)
    if quieres.lower()=="si":
        juego()
    elif quieres.lower()=="no":
        print("\n Adios,vuelve pronto 🙋‍")

#Comienzo del juego 1° parte

def juego():
    extra=iter([i for i in range(2,53)])
    extra1=iter([i for i in range(2,53)])
    print("♣ ♥ ♣ ♦ "*6,"Blackjack","♣ ♥ ♣ ♦ "*6,"\n")
    time.sleep(1)
    nombre=input("¿Cual es tu nombre?")
    
    print("\n¡Bienvenido al juego",nombre,"!","\n")
    time.sleep(1)
    print("-"*10,"Inicia el juego","-"*10,"\n")
    time.sleep(1)
    print("      La computadora te repartira dos cartas al azar\n")
    time.sleep(2)
    Cartas_de_jugador=[]
    puntos_jugador=[]
                                           
    Cartas_de_compu=[]
    puntos_compu=[]
    
    Cartas_de_jugador.append(repartir_carta(Nombre_cartas))
    puntos_jugador.append(Cartas[Cartas_de_jugador[0]])
    
    Cartas_de_jugador.append(repartir_carta(Nombre_cartas))
    puntos_jugador.append(Cartas[Cartas_de_jugador[1]])
    
    simplificar(puntos_jugador)
    
    print("Cartas de ",nombre,"= ", Cartas_de_jugador,"\n")  
    time.sleep(2)
    print("Puntos de", nombre,"= ",puntos_jugador,"\n") 
    time.sleep(2)
    print("Suma de puntos de ",nombre," hasta ahora = ",puntuacion(puntos_jugador),"\n")
    time.sleep(2)
    print(blackjack(Cartas_de_jugador),"\n")
    time.sleep(0.5)
    if blackjack(Cartas_de_jugador)=="blackjack":
        print("Ganaste, ¡¡¡felicidades!!!","😄")
    elif blackjack(Cartas_de_jugador)=="No hay blackjack, continuamos.":
        print("-"*50,"\n")
        Cartas_de_compu.append(repartir_carta(Nombre_cartas))
        puntos_compu.append(Cartas[Cartas_de_compu[0]])
    
        Cartas_de_compu.append(repartir_carta(Nombre_cartas))
        puntos_compu.append(Cartas[Cartas_de_compu[1]])
    
        simplificar(puntos_compu)
        time.sleep(1)
        print("     La compu te muestra una de sus cartas= ",Cartas_de_compu[0],"\n")
        blackjack(Cartas_de_compu)
        time.sleep(2)
        #regla del blackjack americano, si la carta que muestra la compu es un As o vale 10 tiene que verificar si hay un blackjack 
        for i in Cartas_Blackjack:
            if Cartas_de_compu[0]==i:
                print("La compu checara si no tiene blackjack")
                time.sleep(1)
                print(blackjack(Cartas_de_compu))
                if blackjack(Cartas_de_compu)=="blackjack" and blackjack(Cartas_de_jugador)=="No hay blackjack, continuamos.":
                    print("Estas son las cartas de la compu= ",Cartas_de_compu)
                    time.sleep(1)
                    print("La compu ha ganado.😭\n")
                elif blackjack(Cartas_de_compu)=="blackjack" and blackjack(Cartas_de_jugador)=="blackjack":
                    print("Hay un empate. 😑\n")
    #2° parte del juego
    
    if blackjack(Cartas_de_compu)=="No hay blackjack, continuamos." and blackjack(Cartas_de_jugador)=="No hay blackjack, continuamos.":
        print("¿Qué harás ahora?","\n","-"*50,"\n")
        time.sleep(1)
        flag=True
        while flag==True :
            resp=input("    ¿Quieres otra carta?, Escribe si o no = ")
            print("\n")
            while resp.lower()!="si" and resp.lower()!="no":
                print("☠ Solo puedes escribir si o no")
                resp=input("¿Quieres otra carta?, Escribe si o no = ")
            time.sleep(0.5)
            if resp.lower()=="si":
                Cartas_de_jugador.append(repartir_carta(Nombre_cartas))
                lista_de_puntos(Cartas,Cartas_de_jugador,puntos_jugador,extra)
                simplificar(puntos_jugador)
                x=puntuacion(puntos_jugador)
                time.sleep(1)
                print("Cartas de ",nombre,"= ", Cartas_de_jugador,"\n")
                time.sleep(1)
                print("Puntos de", nombre,"= ",puntos_jugador,"\n")
                time.sleep(1)
                print("Suma de puntos de ", nombre,"hasta ahora= ",x,"\n")
                if x>21:
                    time.sleep(1)
                    print("Perdiste, suerte para la proxima.😭","\n")
                    flag=False
                elif x==21 and puntuacion(puntos_compu)==21:
                    time.sleep(2)
                    print("Chequemos las cartas de la computadora= ",Cartas_de_compu,"\n")
                    time.sleep(2)
                    print("Esto es un empate.😑","\n")
                    flag=False
                elif x==21 and puntuacion(puntos_compu)<21:
                    time.sleep(2)
                    print("Chequemos las cartas de la computadora=",Cartas_de_compu,"\n")
                    time.sleep(2)
                    print("La puntuación de la compu fue=",puntuacion(puntos_compu),"\n")
                    time.sleep(2)
                    print("¡¡¡Eres el ganador, felicidades!!!","😄","\n")
                    flag=False
            elif resp.lower()=="no":
                flag = False    
    #3° parte del juego
        if puntuacion(puntos_jugador)<21:
            print("-"*50,"\n")
            time.sleep(1)
            print("    Ahora es tiempo de que juegue la compu","\n")
            time.sleep(1)
            print("La compu muestra sus dos cartas= ",Cartas_de_compu,"\n")
            time.sleep(1)
            print("Puntos hasta ahora de la compu= ",puntos_compu,"\n")
            time.sleep(1)
            print("Suma de puntos hasta ahora de la compu= ",puntuacion(puntos_compu),"\n")
            while puntuacion(puntos_compu)<17:
                Cartas_de_compu.append(repartir_carta(Nombre_cartas))
                lista_de_puntos1(Cartas,Cartas_de_compu,puntos_compu,extra1)
                simplificar(puntos_compu)
                y=puntuacion(puntos_compu)
                time.sleep(2)
                print("     La compu tomara otra carta")
                time.sleep(1)
                print("Cartas de la compu= ",Cartas_de_compu)
                time.sleep(1)
                print("puntos hasta ahora de la compu= ",puntos_compu,"\n")
                time.sleep(1)
                print("Suma de puntos hasta ahora de la compu= ",y,"\n")
            time.sleep(2)    
            print("-"*50,"\n")
            if puntuacion(puntos_compu)>21:
                time.sleep(1)
                print("La compu perdio. ¡¡¡Felicidades tú ganaste!!!😄","\n")
            elif puntuacion(puntos_jugador)>puntuacion(puntos_compu):
                time.sleep(1)
                print("Le ganaste a la compu.¡¡¡Felicidades!!! 😄","\n")
            elif puntuacion(puntos_compu)> puntuacion(puntos_jugador)and 21>puntuacion(puntos_compu):
                time.sleep(1)
                print("Ganó la compu, suerte para la proxima.😭","\n")
            elif puntuacion(puntos_jugador)==puntuacion(puntos_compu):
                time.sleep(1)
                print("Empate.😑","\n")
            elif puntuacion(puntos_compu)==21 and 21>puntuacion(puntos_jugador):
                time.sleep(1)
                print("Ganó la compu, suerte para la proxima.😭","\n")
            time.sleep(1)
            print("Termino juego.🙈")
            jugar_de_nuevo()
        elif puntuacion(puntos_jugador)>21:
            time.sleep(1)
            print("Termino el juego.🙈")
            jugar_de_nuevo()
        elif puntuacion(puntos_jugador)==21:
            time.sleep(1)
            print("Termino el juego.🙈")
            jugar_de_nuevo()
    else:
        time.sleep(1)
        print("Termino el juego.🙈")
        jugar_de_nuevo()

        
        
if __name__ == "__main__":
    juego()

