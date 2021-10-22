![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

# Blackjack
##### ![](https://github.com/Tan30s/Blackjack/blob/main/imagenes/blackjack1.png)

## Descripción 
Este es un codigo que simula el famoso juego del Blackjack o 21, donde el crupier es la computadora y tu objetivo es obtener las cartas que te permitan llegar lo mas cerca de 21, o 21 y/o Blackjack(As y figura) para ser el ganador de la partida.  

## Instrucciones y desarrollo del juego

- La computadora tomará el roll del crupier y repartira dos cartas visibles a cada jugador. El valor del As puede ser 11 o 1 segun tu beneficio las figuras valen 10, y las cartas numéricas su valor original. 

- Si a un jugador le sale un As junto con una carta de valor 10, obtiene blackjack automáticamente, ganando el juego salvo que la computadora tambien haya obtenido blackjack, en este caso sería un empate. 

- Al terminar de repartir las dos primeras cartas a cada jugador, la computadora mostrara una de sus dos cartas, así los jugadores quienes podrán tomar sus decisiones en función de esa carta, mientras que la computadora tendrá una segunda carta oculta en espera de su turno. 

- Cada jugador tiene la posibilidad de plantarse y quedarse con cualquier puntuación, o de pedir más cartas hasta alcanzar los 21 puntos. 

- Alcanzar los 21 puntos con más de una carta extra no se considera blackjack, siendo por tanto esa jugada inferior al blackjack con dos cartas. 

- Si al pedir una nueva carta se pasa de 21, el jugador pierde automáticamente la partida.

- Cuando todos los jugadores se hayan plantado, la computadora  mostrará su carta oculta y sacará más cartas si fuera necesario hasta sumar mínimo 17 puntos momento en el que se plantará.

- Finalmente se comprueba quien gana.

## Observaciónes
-Jugaremos la version americana en la que  el crupier, tras poner su primera carta visible,en el caso de que haya posibilidad de conseguir blackjack (es decir que la carta visible sea un As o una carta de valor 10), tendrá que comprobar la segunda carta antes de continuar para ver si tiene blackjack. En el caso de tener blackjack, lo comunicará al momento finalizando el juego, con lo que en caso de que continúe el juego por no tener blackjack, sabremos que no estamos jugando contra un blackjack del crupier.

-Para poder jugar el juego, puedes ejecutar el archivo "Codigo de blackjack.py" desde una terminal o llamar la función juego() desde el archivo "Practica del codigo.ipynb"

