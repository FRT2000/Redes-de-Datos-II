# Ejercicio 12

##  Y las siguientes:
- 195.80.0.0/24
- 195.80.1.0/24
- 195.80.2.0/24

Resolviendo de la misma manera

- 195.80.0.0/24 = 195.80.|**0000 00**00.0000 0000|
- 195.80.1.0/24 = 195.80.|**0000 00**01.0000 0000|
- 195.80.2.0/24 = 195.80.|**0000 00**10.0000 0000|

Si contamos los bits de izquierda a derecha, empezando desde el primer octeto hasta la parte en la que dejan de coincidir, podemos ver que son 22 bits.

Luego de identificar los 22 bits, se colocan en cero todos los que se encuentra a continuación.

- 195.80.0.0/24 = 195.80.0000 00|**00.0000 0000**|
- 195.80.1.0/24 = 195.80.0000 00|**00.0000 0000**|
- 195.80.2.0/24 = 195.80.0000 00|**00.0000 0000**|

Ahora todos los bits coinciden.

Finalmente debemos colocar el valor resultante, utilizando como prefijo /22 ya que que esa es la cantidad de bits que coinciden.

198.80.0.0/22 -> **Resultado de realizar la sumarización**.