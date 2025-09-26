# Ejercicio 10

## ¿Cómo se podrían sumarizar las siguientes direcciones aplicando CIDR?
- 200.10.0.0/24
- 200.10.1.0/24
- 200.10.2.0/24
- 200.10.3.0/24

Para comenzar, se debe revisar hasta que número de bit son coincidentes entre todas las redes que queremos sumarizar. En este caso vemos que difieren a partir del tercer octeto. Entonces partiendo de este, debemos convertir a binario todos lo que se encuentra a continuación para observar con claridad hasta que número de bit son iguales.

- 200.10.0.0/24 = 200.10.|**0000 00**00.0000 0000|
- 200.10.1.0/24 = 200.10.|**0000 00**01.0000 0000|
- 200.10.2.0/24 = 200.10.|**0000 00**10.0000 0000|
- 200.10.3.0/24 = 200.10.|**0000 00**11.0000 0000|

Si contamos los bits de izquierda a derecha, empezando desde el primer octeto hasta la parte en la que dejan de coincidir, podemos ver que son 22 bits.

Luego de identificar los 22 bits, se colocan en cero todos los que se encuentra a continuación.

- 200.10.0.0/24 = 200.10.0000 00|**00.0000 0000**|
- 200.10.1.0/24 = 200.10.0000 00|**00.0000 0000**|
- 200.10.2.0/24 = 200.10.0000 00|**00.0000 0000**|
- 200.10.3.0/24 = 200.10.0000 00|**00.0000 0000**|

Ahora todos los bits coinciden.

Finalmente debemos colocar el valor resultante, utilizando como prefijo /22 ya que que esa es la cantidad de bits que coinciden.

200.10.0.0/22 -> **Resultado de realizar la sumarización**.