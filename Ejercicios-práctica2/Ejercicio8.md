# Ejercicio 8

## Para cada una de las siguientes direcciones obtener (si corresponde): Dirección y Clase(A, B, C) de Red. Pública/Privada/Reservada/Inválida. Dirección de Subred y Dirección de Broadcast. Cantidad posible de redes si toda la red se hubiese “subneteado” con la misma máscara. Cantidad de IP para hosts por subred utilizables.

### 163.10.5.66/26

#### Dirección y clase de Red (A, B, C)
**Clase B**

Utilizamos la máscara predefinida para esta Clase -> 255.255.0.0/16

Hacemos un AND con la dirección que nos asginaron y obtendremos la dirección de red. Podemos realizar la operación en binario bit a bit para facilitar la operación.

163.10.5.66 AND 255.255.0.0 

163.10.0.0/16 -> **Dirección de red original de la cuál se realizo el subneteo**.

#### Pública/Privada/Reservada/inválida
Red pública

#### Dirección de Subred y Dirección de broadcast
Para obtener la dirección de subred debemos partir de la dirección de red original sin subnetear y ver cuántos bits se tomaron para la parte de subred.

1010 0101.0000 1010.0000 0000.0000 0000 -> Dirección sin subnetear

Podemos observar que la dirección de Clase B tiene el prefijo /16 y el de nuestra red asignada tiene /26. Esto nos indica que se han tomado 10 bits para realizar el subneteo de la red. Por lo tanto tomamos 10 bits a partir de la dirección original.

1010 0101.0000 1010.|**1111 1111.11**|00 0000 -> Tomamos 10 bits de la red original.

Con esto podemos armar la máscara que nos permitirá obtener la dirección de subred. Debemos colocar los primeros 26 bits como lo indica el prefijo /26 en uno (1), porque queremos que se mantengan fijos para obtener la dirección de subred.

**1111 1111.1111 1111.1111 1111.11**00 0000 -> Máscara para obtener la subred

255.255.255.192 -> Máscara en decimal

163.10.5.66 AND 255.255.255.192

163.10.5.64/26 -> **Dirección de subred**

163.10.5.127/26 -> **Dirección de broadcast**

#### Cantidad posible de redes si toda la red se hubiese “subneteado” con la misma máscara
Como se han asignado 10 bits para subnetting, entonces tendremos: $2^{10}$ = 1024 subredes.

#### Cantidad de IP para hosts por subred utilizables
Como IPv4 cuenta con direcciones de 32 bits y ya hemos tomado 26, contamos con 6 bits disponibles para host dentro de cada red. Tenemos que considerar que las direcciones de red y de broadcast no son asignables a ningún host, por lo que debemos descontar dos direcciones al momento de realizar el cálculo.

Entonces tomando 6 bits para host tendremos: $2^{6} - 2 = 62 hosts.