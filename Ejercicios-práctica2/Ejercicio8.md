# Ejercicio 8

## Para cada una de las siguientes direcciones obtener (si corresponde): Dirección y Clase(A, B, C) de Red. Pública/Privada/Reservada/Inválida. Dirección de Subred y Dirección de Broadcast. Cantidad posible de redes si toda la red se hubiese “subneteado” con la misma máscara. Cantidad de IP para hosts por subred utilizables.

### 163.10.5.66/26

#### Dirección y clase de Red (A, B, C)
Red de **Clase B**.

Utilizamos la máscara predefinida para esta Clase -> 255.255.0.0 ó /16

Hacemos un AND con la dirección que nos asginaron y obtendremos la dirección de red. Podemos realizar la operación en binario bit a bit para facilitar la operación.

163.10.5.66 AND 255.255.0.0 

163.10.0.0/16 -> **Dirección de red original de la cuál se realizo el subneteo**.

#### Pública/Privada/Reservada/inválida
Red **Pública**.

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

Entonces tomando 6 bits para host tendremos: $2^{6}$ - 2 = 62 hosts.

---

### 127.0.0.1/8

#### Dirección y clase de Red (A, B, C)
Red de **Clase A**

Utilizamos la máscara predefinida para esta Clase -> 255.0.0.0 ó /8

Hacemos un AND con la dirección que nos asginaron y obtendremos la dirección de red. Podemos realizar la operación en binario bit a bit para facilitar la operación.

127.0.0.1 AND 255.0.0.0 

127.0.0.0/8 -> **Dirección de red**.

#### Pública/Privada/Reservada/inválida
Red **Reservada**.

Se utiliza para Loopback.

#### Dirección de Subred y Dirección de broadcast
Esta red no se usa para realizar subnetting.

127.255.255.255/8 -> **Dirección de broadcast**.

#### Cantidad posible de redes si toda la red se hubiese “subneteado” con la misma máscara
Solo existe una red ya que no se puede realizar el subnetting.

#### Cantidad de IP para hosts por subred utilizables
No puede asignarse a hosts. Sólo se usa para pruebas locales donde el dispositivo puede comunicarse consigo mismo utilizando cualquier dirección comprendida en ese rango.

---

### 20.6.20.1/18

#### Dirección y clase de Red (A, B, C)
Red de **Clase A**.

Utilizamos la máscara predefinida para esta Clase -> 255.0.0.0 ó /8

Hacemos un AND con la dirección que nos asginaron y obtendremos la dirección de red. Podemos realizar la operación en binario bit a bit para facilitar la operación.

20.6.20.1 AND 255.0.0.0 

20.0.0.0/8 -> **Dirección de red original de la cuál se realizo el subneteo**.

#### Pública/Privada/Reservada/inválida
Red **Pública**.

#### Dirección de Subred y Dirección de broadcast
Para obtener la dirección de subred debemos partir de la dirección de red original sin subnetear y ver cuántos bits se tomaron para la parte de subred.

0001 0100.0000 0000.0000 0000.0000 0000 -> Dirección sin subnetear

Podemos observar que la dirección de Clase A tiene el prefijo /8 y el de nuestra red asignada tiene /18. Esto nos indica que se han tomado 10 bits para realizar el subneteo de la red. Por lo tanto tomamos 10 bits a partir de la dirección original.

0001 0100.|1111 1111.11|00 0000.0000 0000 -> Tomamos 10 bits de la red original.

Con esto podemos armar la máscara que nos permitirá obtener la dirección de subred. Debemos colocar los primeros 18 bits como lo indica el prefijo /18 en uno (1), porque queremos que se mantengan fijos para obtener la dirección de subred.

**1111 1111.1111 1111.11**00 0000.0000 0000 -> Máscara para obtener la subred

255.255.192.0 -> Máscara en decimal

20.6.20.1 AND 255.255.192.0

20.6.0.0/18 -> **Dirección de subred**

20.6.63.255/18 -> **Dirección de broadcast**

#### Cantidad posible de redes si toda la red se hubiese “subneteado” con la misma máscara
Como se han asignado 10 bits para subnetting, entonces tendremos: $2^{10}$ = 1024 subredes.

#### Cantidad de IP para hosts por subred utilizables
Como IPv4 cuenta con direcciones de 32 bits y ya hemos tomado 18, contamos con 14 bits disponibles para host dentro de cada red. Tenemos que considerar que las direcciones de red y de broadcast no son asignables a ningún host, por lo que debemos descontar dos direcciones al momento de realizar el cálculo.

Entonces tomando 14 bits para host tendremos: $2^{14}$ - 2 = 16382 hosts.

---

### 200.5.10.3/30

#### Dirección y clase de Red (A, B, C)
Red de **Clase C**.

Utilizamos la máscara predefinida para esta Clase -> 255.255.255.0 ó /24

Hacemos un AND con la dirección que nos asginaron y obtendremos la dirección de red. Podemos realizar la operación en binario bit a bit para facilitar la operación.

200.5.10.3 AND 255.255.255.0 

200.5.10.0/24 -> **Dirección de red original de la cuál se realizo el subneteo**.

#### Pública/Privada/Reservada/inválida
Red **Pública**.

#### Dirección de Subred y Dirección de broadcast
Para obtener la dirección de subred debemos partir de la dirección de red original sin subnetear y ver cuántos bits se tomaron para la parte de subred.

1100 1000.0000 0101.0000 1010.0000 0000 -> Dirección sin subnetear

Podemos observar que la dirección de Clase C tiene el prefijo /24 y el de nuestra red asignada tiene /30. Esto nos indica que se han tomado 6 bits para realizar el subneteo de la red. Por lo tanto tomamos 6 bits a partir de la dirección original.

1100 1000.0000 0101.0000 1010.|**1111 11**|00 -> Tomamos 6 bits de la red original.

Con esto podemos armar la máscara que nos permitirá obtener la dirección de subred. Debemos colocar los primeros 30 bits como lo indica el prefijo /30 en uno (1), porque queremos que se mantengan fijos para obtener la dirección de subred.

**1111 1111.1111 1111.1111 1111.1111 11**00 -> Máscara para obtener la subred

255.255.255.252 -> Máscara en decimal

200.5.10.3 AND 255.255.255.252

200.5.10.0/30 -> **Dirección de subred**

200.5.10.3/30 -> **Dirección de broadcast**

#### Cantidad posible de redes si toda la red se hubiese “subneteado” con la misma máscara
Como se han asignado 6 bits para subnetting, entonces tendremos: $2^{6}$ = 64 subredes.

#### Cantidad de IP para hosts por subred utilizables
Como IPv4 cuenta con direcciones de 32 bits y ya hemos tomado 30, contamos con 2 bits disponibles para host dentro de cada red. Tenemos que considerar que las direcciones de red y de broadcast no son asignables a ningún host, por lo que debemos descontar dos direcciones al momento de realizar el cálculo.

Entonces tomando 2 bits para host tendremos: $2^{2}$ - 2 = 2 hosts.

---

### 172.18.10.0/26

#### Dirección y clase de Red (A, B, C)
Red de **Clase B**.

Utilizamos la máscara predefinida para esta Clase -> 255.255.0.0 ó /16

Hacemos un AND con la dirección que nos asginaron y obtendremos la dirección de red. Podemos realizar la operación en binario bit a bit para facilitar la operación.

172.18.10.0 AND 255.255.0.0

172.18.0.0/16 -> **Dirección de red original de la cuál se realizo el subneteo**.

#### Pública/Privada/Reservada/inválida
Red **Privada**.

#### Dirección de Subred y Dirección de broadcast
Para obtener la dirección de subred debemos partir de la dirección de red original sin subnetear y ver cuántos bits se tomaron para la parte de subred.

1010 1100.0001 0010.0000 0000.0000 0000 -> Dirección sin subnetear

Podemos observar que la dirección de Clase B tiene el prefijo /16 y el de nuestra red asignada tiene /26. Esto nos indica que se han tomado 10 bits para realizar el subneteo de la red. Por lo tanto tomamos 10 bits a partir de la dirección original.

1010 1100.0001 0010.|**1111 11**|00.0000 0000 -> Tomamos 6 bits de la red original.

Con esto podemos armar la máscara que nos permitirá obtener la dirección de subred. Debemos colocar los primeros 26 bits como lo indica el prefijo /26 en uno (1), porque queremos que se mantengan fijos para obtener la dirección de subred.

1111 1111.1111 1111.1111 1111.1100 0000 -> Máscara para obtener la subred

255.255.255.192 -> Máscara en decimal

172.18.10.0 AND 255.255.255.192

172.18.10.0/26 -> **Dirección de subred**

172.18.10.63/26 -> **Dirección de broadcast**

#### Cantidad posible de redes si toda la red se hubiese “subneteado” con la misma máscara
Como se han asignado 10 bits para subnetting, entonces tendremos: $2^{10}$ = 1024 subredes.

#### Cantidad de IP para hosts por subred utilizables
Como IPv4 cuenta con direcciones de 32 bits y ya hemos tomado 26, contamos con 6 bits disponibles para host dentro de cada red. Tenemos que considerar que las direcciones de red y de broadcast no son asignables a ningún host, por lo que debemos descontar dos direcciones al momento de realizar el cálculo.

Entonces tomando 6 bits para host tendremos: $2^{6}$ - 2 = 6 hosts.