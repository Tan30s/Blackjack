![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

# Blackjack
Código del juego Blackjack
#### ![](https://github.com/Tan30s/Blackjack/blob/main/imagenes/blackjack1.png)
##Descripción 
Este es un codigo que simula el famoso juego del Blackjack o 21, en este caso se 

##Istrucciones 

La computadora tomará el roll del crupier, reparte dos cartas visibles a cada jugador. El valor del As es 11 o +1, las figuras valen 10, y las cartas numéricas su valor original. El valor del As puede cambiarse según la necesidad de no pasarse del número 21. Si a un jugador le sale un As junto con una carta de valor 10, obtiene blackjack automáticamente, ganando salvo que el crupier obtenga también blackjack. Al terminar de repartir las dos primeras cartas a cada jugador, el crupier pondrá luego su primera carta boca arriba de manera que sea visible para el resto de jugadores, quienes podrán tomar sus decisiones en función de esa carta, mientras que el crupier tendrá una segunda carta boca abajo en espera de su turno. Cada jugador compite únicamente contra el crupier, siendo indiferente a las cartas que tengan el resto de los demás jugadores.
Cada jugador tiene la posibilidad de plantarse y quedarse con cualquier puntuación, o de pedir más cartas hasta alcanzar los 21 puntos. Alcanzar los 21 puntos con más de una carta extra no se considera blackjack, siendo por tanto esa jugada inferior al blackjack con dos cartas. Si al pedir una nueva carta se pasa de 21, el jugador pierde automáticamente la partida y sus cartas y apuesta serán retiradas por el crupier. Cuando todos los jugadores hayan pedido sus cartas, el crupier mostrará su segunda carta boca abajo y sacará más cartas si fuera necesario hasta sumar 17 o más puntos para alcanzar el número 21, momento en el que se plantará.
Entre el crupier y cada jugador, gana finalmente quién obtenga blackjack (As+10) o quien tenga la puntuación más alta sin pasarse de los 21 puntos, habiendo la posibilidad de empate.
Jugaremos la version americana en la que  el crupier, tras poner su primera carta visible, sacará su segunda carta que estará tapada, pero en el caso de que con la carta visible haya posibilidad de conseguir blackjack (un As o una carta de valor 10 visible), comprobará la segunda carta antes de continuar para ver si tiene blackjack. En el caso de tener blackjack, lo comunicará al momento finalizando la mano, con lo que en caso de que continúe el juego por no tener blackjack, sabremos que no estamos jugando contra un blackjack del crupier.
