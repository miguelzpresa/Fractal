# -Sistemas-Dinámicos
Implementación Fractal
---------------------------------------------------------------------------------------------
Autor: Miguel Ángel Zamorano Presa
contacto: mikezpresa@gmail.com
# Estructura del código
## funciones
6 funciones creadas descritas a continuación:
* give_me_lenght: que para cualquiera 2 puntos dados devuelve la dist euclidiana
*  inner_points : utiliza la información obtenida por startp y con eso identifica y construye los nuevos puntos internos de cada intervalo de lineas
*  startp: dado un intervalo de linea lo que te devuelve son 4 cosas:
  *1era: longitud parcial que no es mas que la distancia euclidiana dividia entre 3
  2nda: dado el intervalo identifica cual de las coordenadas (si x o y) cual de ellas es fija y cual de ellas varía
  3rera: el punto de inicio del intervalo de linea
  4to: el punto de fin del intervalo de linea  
  
* parallel_p: dado dos puntos ,su longitud que con la función dist_euclidiana y el tipo
 es posible contruir un las coordenadas de un cuadrado con la orientación que tu quieras
*  plot_basis: se limita a dibujar rectas de puntos de inicio y fin a puntos internos
* final_plot: función de cerrado,(última iteración)se pensaba como que de manera iterativa iriá procesando las coordenadas obtenidas ,ubicadas en el buffer de bases para que al final hiciera el cerrado de la figura
 
 el tipo 
 el argumento tipo fue con lo que más se batallo ,la idea que se intento seguir fue la de utilizar modulo 4 para distinguir de las posibles
 orientaciones posibles,el valor de tipo( orientación) dependera de la orientación de el intervalo dado como inputes pruebas aisladas todas ellas funcionaron adecuadamente
 
 Complicaciones principales fue en el orquestar el código de manera que funcionara iterativamente
 principalmente la parte del plotting con matplotlib, me faltó tiempo y eso que lo empecé desde el miercoles pasado.
 
 # Código
 input
 un solo número que representa el número de iteraciones del fractal
 output
 el intent fallido plot visualizadao
 # Cuerpo de Código
 1.se obteiene input  
 2.se trata  caso particular: cuando input =0  
 3.se busca por cada iteración contruir y ensamblar las funciones creadas para obtener las coordenadas
 y ellas almacenarlas en órden para despues sean procesadas para matplotlib  
 4.mientras el iterador no equivalgaa ser la última iteración,se busca que mientras vaya contruyendo 
 nuevas coordenadas igualmente vaya haciendo el plotting .  
 5.en el momento que el iterador equivalga a la última   
 se pregunta si el valor de iteraciones fue 1 si sí se aplica un shortcut de ploteo y si nó 
 para cada base generada en el contenedor de buffers de bases queremos que dibuje y cierre coordenadas
 
 



