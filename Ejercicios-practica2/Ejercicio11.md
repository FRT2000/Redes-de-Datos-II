# Ejercicio 11

##  ¿Cómo quedará la sumarización si necesita agrupar las 8 primeras redes (hasta las 200.10.7.0/24).
- 200.10.0.0/24
- 200.10.1.0/24
- 200.10.2.0/24
- 200.10.3.0/24
- 200.10.4.0/24
- 200.10.5.0/24
- 200.10.6.0/24
- 200.10.7.0/24

Siguiendo las mismas consideraciones que en el ejercicio 10

- 200.10.0.0/24 = 200.10.|**0000 0**000.0000 0000|
- 200.10.1.0/24 = 200.10.|**0000 0**001.0000 0000|
- 200.10.2.0/24 = 200.10.|**0000 0**010.0000 0000|
- 200.10.3.0/24 = 200.10.|**0000 0**011.0000 0000|
- 200.10.4.0/24 = 200.10.|**0000 0**100.0000 0000|
- 200.10.5.0/24 = 200.10.|**0000 0**101.0000 0000|
- 200.10.6.0/24 = 200.10.|**0000 0**110.0000 0000|
- 200.10.7.0/24 = 200.10.|**0000 0**111.0000 0000|

Si contamos los bits de izquierda a derecha, empezando desde el primer octeto hasta la parte en la que dejan de coincidir, podemos ver que son 21 bits.

Luego de identificar los 21 bits, se colocan en cero todos los que se encuentra a continuación.

- 200.10.0.0/24 = 200.10.0000 0|**000.0000 0000**|
- 200.10.1.0/24 = 200.10.0000 0|**000.0000 0000**|
- 200.10.2.0/24 = 200.10.0000 0|**000.0000 0000**|
- 200.10.3.0/24 = 200.10.0000 0|**000.0000 0000**|
- 200.10.4.0/24 = 200.10.0000 0|**000.0000 0000**|
- 200.10.5.0/24 = 200.10.0000 0|**000.0000 0000**|
- 200.10.6.0/24 = 200.10.0000 0|**000.0000 0000**|
- 200.10.7.0/24 = 200.10.0000 0|**000.0000 0000**|

Ahora todos los bits coinciden.

Finalmente debemos colocar el valor resultante, utilizando como prefijo /21 ya que que esa es la cantidad de bits que coinciden.

200.10.0.0/21 -> **Resultado de realizar la sumarización**.