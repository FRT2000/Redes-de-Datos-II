 # Ejercicio 24

 ## Transforme las siguientes direcciones MACs en Identificadores de Interfaces de 64 bits de alcance link-local.

 ### 00:1b:77:b1:49:a1

**Primer paso:** separamos la dirección MAC en dos porciones de 3 bytes cada una.

00:1b:77    |   b1:49:a1 -> Dirección MAC en dos partes.

**Segundo paso:** colocamos ff:fe en medio de las dos porciones que habíamos separado anteriormente.

00:1b:77 | **ff:fe** | b1:49:a1 

**Tercer paso:** tomamos el primer octeto de la dirección MAC original e invertimos el segundo bit (contando de derecha a izquierda). Realizar la conversión a binario facilita la visualización. Para este caso el primer octeto es cero.

|**00**|:1b:77:b1:49:a1 -> Primer octeto.

0000 00|**0**|0 -> Segundo bit del primer octeto.

0000 00|**1**|0 -> Se invierte el segundo bit.

**02** -> Valor resultante en hexadecimal del primer octeto luego de invertir el segundo bit.

Ahora reemplazamos el nuevo valor del primer octeto en la dirección que se estaba formando en el segundo paso.

02:1b:77:ff:fe:b1:49:a1

**Cuarto paso:** colocamos el prefijo fe80::/64 ó fe80:0000:0000:0000/64 al principio de la dirección que se formó en el tercer paso.

fe80::02:1b:77:ff:fe:b1:49:a1

Por último, escribimos la dirección link-local obtenida en formato IPv6 (grupos de 16 bits).

fe80::021b:77ff:feb1:49a1/64

---

### e8:1c:23:a3:21:f4

**Primer paso:** separamos la dirección MAC en dos porciones de 3 bytes cada una.

e8:1c:23    |   a3:21:f4 -> Dirección MAC en dos partes.

**Segundo paso:** colocamos ff:fe en medio de las dos porciones que habíamos separado anteriormente.

e8:1c:23 | **ff:fe** | a3:21:f4 

**Tercer paso:** tomamos el primer octeto de la dirección MAC original e invertimos el segundo bit (contando de derecha a izquierda). Realizar la conversión a binario facilita la visualización. Para este caso el primer octeto es cero.

|**e8**|:1c:23:a3:21:f4 -> Primer octeto.

1110 10|**0**|0 -> Segundo bit del primer octeto.

1110 10|**1**|0 -> Se invierte el segundo bit.

**ea** -> Valor resultante en hexadecimal del primer octeto luego de invertir el segundo bit.

Ahora reemplazamos el nuevo valor del primer octeto en la dirección que se estaba formando en el segundo paso.

ea:1c:23:ff:fe:a3:21:f4

**Cuarto paso:** colocamos el prefijo fe80::/64 ó fe80:0000:0000:0000/64 al principio de la dirección que se formó en el tercer paso.

fe80::ea:1c:23:ff:fe:a3:21:f4

Por último, escribimos la dirección link-local obtenida en formato IPv6 (grupos de 16 bits).

fe80::ea1c:23ff:fea3:21f4/64
