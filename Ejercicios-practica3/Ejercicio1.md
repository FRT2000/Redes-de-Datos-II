# Ejercicio 1

##  Aplicando VLSM, resolver los siguientes ejercicios:

### Dada la red IP 65.0.0.0/24 se necesitan definir:
- 1(una) red de 80 hosts
- 2(dos) redes de 10 hosts.
- 1(una) red de 40 hosts.

#### Red de 80 hosts

Para comenzar a aplicar esta técnica de subnetting, la cual consiste en dividir la red IP original en subredes de diferentes tamaños, debemos iniciar desde la red que necesita más hosts.

Empezamos por la red que necesita 80 hosts. Para esto se necesitarán 7 bits designados para hosts, dado que:
$2^{7}$ - 2 = 126 hosts.

Contamos los 7 bits de derecha a izquierda para saber la parte que corresponde a las direcciones de hosts. Luego contamos cuántos bits hemos tomado para crear subredes a partir de la red original sin subnetear.

65.0.0.0/24 -> red original

0100 0001.0000 0000.0000 0000.0|**000 0000**| -> bits tomados para los 80 hosts.

|**0100 0001.0000 0000.0000 0000**|.0000 0000 -> bits de red original

0100 0001.0000 0000.0000 0000.|**0**|000 0000 -> bits tomados para subred

Ahora colocamos en 1 (uno) cada bit adicional que hayamos tomado para subred, esto nos determinará la dirección que será asignada a la red para 80 hosts. Con esto logramos asignar la última red posible dentro de ese espacio de direcciones. 

0100 0001.0000 0000.0000 0000.|**1**|000 0000 -> bits tomados para subred colocados en 1

No debemos olvidarnos de calcular la nueva máscara de subred, la cual contempla los bits de la red sin subnetear más los bits que se han tomado para subred, en este caso tenemos 25 bits que nos sirven para identificar la red.
Por lo tanto el resultado final será:

65.0.0.128/25 -> **dirección IP asignada para los 80 hosts.**

Finalmente la red `65.0.0.0/25` queda libre para seguir subneteando.

---

#### Red de 40 hosts

Partimos de la red 65.0.0.0/25 la cual queda libre para seguir con el mismo procedimiento.

En este caso la red necesita 40 hosts. Para esto se necesitarán 6 bits designados para hosts, dado que:

$2^{6}$ - 2 = 62 hosts.

Contamos los 6 bits de derecha a izquierda para saber la parte que corresponde a las direcciones de hosts. Luego contamos cuántos bits hemos tomado para crear subredes a partir de la red anterior, la cual ha quedado libre después de asignar la dirección para los 80 hosts.

65.0.0.0/25 -> red de la cual iniciamos el subnetting

0100 0001.0000 0000.0000 0000.00|**00 0000**| -> bits tomados para los 40 hosts.

|**0100 0001.0000 0000.0000 0000.0**|000 0000 -> bits de red

0100 0001.0000 0000.0000 0000.0|**0**|00 0000 -> bits tomados para subred

Ahora colocamos en 1 (uno) cada bit adicional que hayamos tomado para subred, esto nos determinará la dirección que será asignada a la red para 40 hosts. De la misma manera que para el caso anterior, esto nos permite asignar la última red posible dentro de ese espacio de direcciones.

0100 0001.0000 0000.0000 0000.0|**1**|00 0000 -> bits tomados para subred colocados en 1

No debemos olvidarnos de calcular la nueva máscara de subred, la cual contempla los bits de la red que tomamos como punto de partida más los bits que se han tomado para subred, en este caso tenemos 26 bits que nos sirven para identificar la red.

Por lo tanto el resultado final será:

65.0.0.64/26 -> **dirección IP asignada para los 40 hosts.**

Finalmente la red `65.0.0.0/26` queda libre para seguir subneteando.

---

#### Primera red de 10 hosts

Partimos de la red 65.0.0.0/26 la cual queda libre para seguir con el mismo procedimiento.

En este caso la red necesita 10 hosts. Para esto se necesitarán 4 bits designados para hosts, dado que:

$2^{4}$ - 2 = 14 hosts.

Contamos los 4 bits de derecha a izquierda para saber la parte que corresponde a las direcciones de hosts. Luego contamos cuántos bits hemos tomado para crear subredes a partir de la red anterior, la cual ha quedado libre después de asignar la dirección para los 40 hosts.

65.0.0.0/26 -> red de la cual iniciamos el subnetting

0100 0001.0000 0000.0000 0000.0000 |**0000**| -> bits tomados para los 10 hosts.

|**0100 0001.0000 0000.0000 0000.00**|00 0000 -> bits de red

0100 0001.0000 0000.0000 0000.00|**00**| 0000 -> bits tomados para subred

Ahora colocamos en 1 (uno) cada bit adicional que hayamos tomado para subred, esto nos determinará la dirección que será asignada a la red para 10 hosts. De la misma manera que para el caso anterior, esto nos permite asignar la última red posible dentro de ese espacio de direcciones.

0100 0001.0000 0000.0000 0000.00|**11**| 0000 -> bits tomados para subred colocados en 1

No debemos olvidarnos de calcular la nueva máscara de subred, la cual contempla los bits de la red que tomamos como punto de partida más los bits que se han tomado para subred, en este caso tenemos 28 bits que nos sirven para identificar la red.

Por lo tanto el resultado final será:

65.0.0.48/28 -> **dirección IP asignada para los primeros 10 hosts.**

Finalmente las direcciones: `65.0.0.0` hasta la `65.0.0.47` quedan libres para seguir subneteando.

---

#### Segunda red de 10 hosts

Necesitamos otros 10 hosts por lo que la cantidad de bits que debemos tomar no cambia, con los 2 bits disponibles que teníamos para subred en el caso anterior es posible crear 4 subredes ya que: $2^{2}$ = 4. Donde cada una tendrá 10 hosts para este caso.

Ya hemos reservado la última dirección disponible para los primeros 10 hosts.

0100 0001.0000 0000.0000 0000.00|**11**| 0000 -> última red posible en el espacio de direcciones.

Lo que debemos hacer es restarle 1 (uno) a esa dirección de red y de esta manera obtener la anteúltima red posible del espacio de direcciones.

0100 0001.0000 0000.0000 0000.00|**10**| 0000 -> anteúltima red posible en el espacio de direcciones.

Por lo tanto el resultado final será:

65.0.0.32/28 -> **dirección IP asignada para los segundos 10 hosts.**

Si nos pidieran 2 redes más para otros 10 hosts cada una, repetiríamos el proceso de ir restando uno a la red anterior. En caso de necesitar más de 2 redes con 10 hosts cada una a partir de las asignaciones anteriores, no alcanzarían las direcciones. 

Finalmente las direcciones: `65.0.0.0` hasta la `65.0.0.31` quedan disponibles para seguir subneteando. Si sumarizamos, podemos expresarlo como `65.0.0.0/27`

---

###  Dada la red IP 100.0.0.0/16 se necesitan definir:
- 2(dos) redes de 2000 hosts
- 2(dos) redes de 500 hosts.
- 20(veinte) redes de 300 hosts.
- 50(cincuenta) redes de 200 hosts.
- Una red de backbone para unir cada uno de los router de las redes anteriores (74 direcciones).

#### Primera red de 2000 hosts

Empezamos por la red que necesita 2000 hosts. Para esto se necesitarán 11 bits designados para hosts, dado que:
$2^{11}$ - 2 = 2046 hosts.

Contamos los 11 bits de derecha a izquierda para saber la parte que corresponde a las direcciones de hosts. Luego contamos cuántos bits hemos tomado para crear subredes a partir de la red original sin subnetear.

100.0.0.0/16 -> red original

0110 0100.0000 0000.0000 0|**000.0000 0000**| -> bits tomados para los 2000 hosts.

|**0110 0100.0000 0000**|.0000 0000.0000 0000 -> bits de red original

0110 0100.0000 0000.|**0000 0**|000.0000 0000 -> bits tomados para subred

Ahora colocamos en 1 (uno) cada bit adicional que hayamos tomado para subred, esto nos determinará la dirección que será asignada a la red para 2000 hosts. Con esto logramos asignar la última red posible dentro de ese espacio de direcciones. 

0110 0100.0000 0000.|**1111 1**|000.0000 0000 -> bits tomados para subred colocados en 1

No debemos olvidarnos de calcular la nueva máscara de subred, la cual contempla los bits de la red sin subnetear más los bits que se han tomado para subred, en este caso tenemos 21 bits que nos sirven para identificar la red.
Por lo tanto el resultado final será:

100.0.248.0/21 -> **dirección IP asignada para los 2000 hosts.**

Finalmente las direcciones: `100.0.0.0` hasta `100.0.247.255` quedan libres para seguir subneteando.

---

#### Segunda red de 2000 hosts

Ya hemos reservado la última dirección disponible para los primeros 2000 hosts.

0110 0100.0000 0000.|**1111 1**|000.0000 0000 -> última red posible en el espacio de direcciones.

Lo que debemos hacer es restarle 1 (uno) a esa dirección de red y de esta manera obtener la anteúltima red posible del espacio de direcciones.

0110 0100.0000 0000.|**1111 0**|000.0000 0000 -> anteúltima red posible en el espacio de direcciones.

Por lo tanto el resultado final será:

100.0.240.0/21 -> **dirección IP asignada para los segundos 2000 hosts.** 

Finalmente las direcciones a partir de `100.0.0.0` hasta `100.0.239.255` quedan libres para seguir subneteando.

---

#### Primera red de 500 hosts

En este caso la red necesita 500 hosts. Para esto se necesitarán 9 bits designados para hosts, dado que:

$2^{9}$ - 2 = 510 hosts.

Para esto nos posicionamos en la última red libre para empezar el subnetting:

100.0.239.255 -> Red de la cual partimos.

0110 0100.0000 0000.1110 1111.1111 1111 -> red expresada en bits.

0110 0100.0000 0000.1110 111|**0.0000 0000**| -> Colocamos en cero los bits que necesitamos para hosts.

0110 0100.0000 0000.|**1110 111**|0.0000 0000 -> Bits tomados para subred.

La nueva máscara de subred será /23

100.0.238.0/23 -> **dirección IP asignada para la primera red de 500 hosts.**

---

#### Segunda red de 500 hosts

Ya hemos reservado la última dirección disponible para los primeros 500 hosts.

0110 0100.0000 0000.|**1110 111**|0.0000 0000 -> última red posible en el espacio de direcciones.

Lo que debemos hacer es restarle 1 (uno) a esa dirección de red y de esta manera obtener la anteúltima red posible del espacio de direcciones.

0110 0100.0000 0000.|**1110 110**|0.0000 0000 -> anteúltima red posible en el espacio de direcciones.

Por lo tanto el resultado final será:

100.0.236.0/23 -> **dirección IP asignada para los segundos 500 hosts.** 

Finalmente las direcciones: `100.0.0.0` hasta `100.0.235.255` quedan disponibles para seguir subneteando.

---

#### Red número 1 de 300 host

Partimos de la red 100.0.235.255 la cual queda libre para seguir con el mismo procedimiento.

En este caso la red necesita 300 hosts. Para esto se necesitarán 9 bits designados para hosts, dado que:

$2^{9}$ - 2 = 510 hosts.

Podemos observar que necesitamos la misma cantidad de bits que para el caso de 500 hosts. Por lo tanto, seguimos asignando las direcciones de forma decremental, restando 1 (uno) al espacio destinado para subred.

0110 0100.0000 0000.|**1110 110**|0.0000 0000 -> Última red tomada para los 500 hosts.

0110 0100.0000 0000.|**1110 101**|0.0000 0000 -> Decrementando en 1 (uno) la dirección de subred anterior.

Por lo tanto el resultado final será:

100.0.234.0/23 -> **dirección IP asignada para la red número 1 de 300 hosts.**

---

#### Red número 2 de 300 host

0110 0100.0000 0000.|**1110 101**|0.0000 0000 -> Última red tomada para los 300 hosts.

0110 0100.0000 0000.|**1110 100**|0.0000 0000 -> Decrementando en 1 (uno) la dirección de subred anterior.

Por lo tanto el resultado final será:

100.0.232.0/23 -> **dirección IP asignada para la red número 2 de 300 hosts.**

---

#### Red número 3 de 300 host

0110 0100.0000 0000.|**1110 100**|0.0000 0000 -> Última red tomada para los 300 hosts.

0110 0100.0000 0000.|**1110 011**|0.0000 0000 -> Decrementando en 1 (uno) la dirección de subred anterior.

Por lo tanto el resultado final será:

100.0.230.0/23 -> **dirección IP asignada para la red número 3 de 300 hosts.**

---

#### Red número 4 de 300 host

0110 0100.0000 0000.|**1110 011**|0.0000 0000 -> Última red tomada para los 300 hosts.

0110 0100.0000 0000.|**1110 010**|0.0000 0000 -> Decrementando en 1 (uno) la dirección de subred anterior.

Por lo tanto el resultado final será:

100.0.228.0/23 -> **dirección IP asignada para la red número 4 de 300 hosts.**

---

#### Red número 5 de 300 host

0110 0100.0000 0000.|**1110 010**|0.0000 0000 -> Última red tomada para los 300 hosts.

0110 0100.0000 0000.|**1110 001**|0.0000 0000 -> Decrementando en 1 (uno) la dirección de subred anterior.

Por lo tanto el resultado final será:

100.0.226.0/23 -> **dirección IP asignada para la red número 5 de 300 hosts.**

---

#### Red número 6 de 300 host

0110 0100.0000 0000.|**1110 001**|0.0000 0000 -> Última red tomada para los 300 hosts.

0110 0100.0000 0000.|**1110 000**|0.0000 0000 -> Decrementando en 1 (uno) la dirección de subred anterior.

Por lo tanto el resultado final será:

100.0.224.0/23 -> **dirección IP asignada para la red número 6 de 300 hosts.**

---

#### Red número 7 de 300 host

0110 0100.0000 0000.|**1110 000**|0.0000 0000 -> Última red tomada para los 300 hosts.

0110 0100.0000 0000.|**1101 111**|0.0000 0000 -> Decrementando en 1 (uno) la dirección de subred anterior.

Por lo tanto el resultado final será:

100.0.222.0/23 -> **dirección IP asignada para la red número 7 de 300 hosts.**

---

#### Red número 8 de 300 host

0110 0100.0000 0000.|**1101 111**|0.0000 0000 -> Última red tomada para los 300 hosts.

0110 0100.0000 0000.|**1101 110**|0.0000 0000 -> Decrementando en 1 (uno) la dirección de subred anterior.

Por lo tanto el resultado final será:

100.0.220.0/23 -> **dirección IP asignada para la red número 8 de 300 hosts.**

---

#### Red número 9 de 300 host

0110 0100.0000 0000.|**1101 110**|0.0000 0000 -> Última red tomada para los 300 hosts.

0110 0100.0000 0000.|**1101 101**|0.0000 0000 -> Decrementando en 1 (uno) la dirección de subred anterior.

Por lo tanto el resultado final será:

100.0.218.0/23 -> **dirección IP asignada para la red número 9 de 300 hosts.**

---

#### Red número 10 de 300 host

0110 0100.0000 0000.|**1101 101**|0.0000 0000 -> Última red tomada para los 300 hosts.

0110 0100.0000 0000.|**1101 100**|0.0000 0000 -> Decrementando en 1 (uno) la dirección de subred anterior.

Por lo tanto el resultado final será:

100.0.216.0/23 -> **dirección IP asignada para la red número 10 de 300 hosts.**

---

#### Red número 11 de 300 host

0110 0100.0000 0000.|**1101 100**|0.0000 0000 -> Última red tomada para los 300 hosts.

0110 0100.0000 0000.|**1101 011**|0.0000 0000 -> Decrementando en 1 (uno) la dirección de subred anterior.

Por lo tanto el resultado final será:

100.0.214.0/23 -> **dirección IP asignada para la red número 11 de 300 hosts.**

---

#### Red número 12 de 300 host

0110 0100.0000 0000.|**1101 011**|0.0000 0000 -> Última red tomada para los 300 hosts.

0110 0100.0000 0000.|**1101 010**|0.0000 0000 -> Decrementando en 1 (uno) la dirección de subred anterior.

Por lo tanto el resultado final será:

100.0.212.0/23 -> **dirección IP asignada para la red número 12 de 300 hosts.**

---

#### Red número 13 de 300 host

0110 0100.0000 0000.|**1101 010**|0.0000 0000 -> Última red tomada para los 300 hosts.

0110 0100.0000 0000.|**1101 001**|0.0000 0000 -> Decrementando en 1 (uno) la dirección de subred anterior.

Por lo tanto el resultado final será:

100.0.210.0/23 -> **dirección IP asignada para la red número 13 de 300 hosts.**

---

#### Red número 14 de 300 host

0110 0100.0000 0000.|**1101 001**|0.0000 0000 -> Última red tomada para los 300 hosts.

0110 0100.0000 0000.|**1101 000**|0.0000 0000 -> Decrementando en 1 (uno) la dirección de subred anterior.

Por lo tanto el resultado final será:

100.0.208.0/23 -> **dirección IP asignada para la red número 14 de 300 hosts.**

---

#### Red número 15 de 300 host

0110 0100.0000 0000.|**1101 000**|0.0000 0000 -> Última red tomada para los 300 hosts.

0110 0100.0000 0000.|**1100 111**|0.0000 0000 -> Decrementando en 1 (uno) la dirección de subred anterior.

Por lo tanto el resultado final será:

100.0.206.0/23 -> **dirección IP asignada para la red número 15 de 300 hosts.**

---

#### Red número 16 de 300 host

0110 0100.0000 0000.|**1100 111**|0.0000 0000 -> Última red tomada para los 300 hosts.

0110 0100.0000 0000.|**1100 110**|0.0000 0000 -> Decrementando en 1 (uno) la dirección de subred anterior.

Por lo tanto el resultado final será:

100.0.204.0/23 -> **dirección IP asignada para la red número 16 de 300 hosts.**

---

#### Red número 17 de 300 host

0110 0100.0000 0000.|**1100 110**|0.0000 0000 -> Última red tomada para los 300 hosts.

0110 0100.0000 0000.|**1100 101**|0.0000 0000 -> Decrementando en 1 (uno) la dirección de subred anterior.

Por lo tanto el resultado final será:

100.0.202.0/23 -> **dirección IP asignada para la red número 17 de 300 hosts.**

---

#### Red número 18 de 300 host

0110 0100.0000 0000.|**1100 101**|0.0000 0000 -> Última red tomada para los 300 hosts.

0110 0100.0000 0000.|**1100 100**|0.0000 0000 -> Decrementando en 1 (uno) la dirección de subred anterior.

Por lo tanto el resultado final será:

100.0.200.0/23 -> **dirección IP asignada para la red número 18 de 300 hosts.**

---

#### Red número 19 de 300 host

0110 0100.0000 0000.|**1100 100**|0.0000 0000 -> Última red tomada para los 300 hosts.

0110 0100.0000 0000.|**1100 011**|0.0000 0000 -> Decrementando en 1 (uno) la dirección de subred anterior.

Por lo tanto el resultado final será:

100.0.198.0/23 -> **dirección IP asignada para la red número 19 de 300 hosts.**

---

#### Red número 20 de 300 host

0110 0100.0000 0000.|**1100 011**|0.0000 0000 -> Última red tomada para los 300 hosts.

0110 0100.0000 0000.|**1100 010**|0.0000 0000 -> Decrementando en 1 (uno) la dirección de subred anterior.

Por lo tanto el resultado final será:

100.0.196.0/23 -> **dirección IP asignada para la red número 20 de 300 hosts.**

Finalmente las direcciones: `100.0.0.0` hasta `100.0.195.255` quedan disponibles para seguir subneteando.

---

#### Redes de 200 hosts

En este caso la red necesita 500 hosts. Para esto se necesitarán 9 bits designados para hosts, dado que:

$2^{8}$ - 2 = 254 hosts.

Para esto nos posicionamos en la última red libre para empezar el subnetting:

100.0.195.255 -> Red de la cual partimos.

0110 0100.0000 0000.1100 0011.1111 1111 -> red expresada en bits.

0110 0100.0000 0000.1100 0011.|**0000 0000**| -> Colocamos en cero los bits que necesitamos para hosts.

0110 0100.0000 0000.|**1100 0011**|.0000 0000 -> Bits tomados para subred.

La nueva máscara de subred será /24

100.0.195.0/24 -> **dirección IP asignada para la primera red de 200 hosts.**

Ahora siguiendo con el mismo procedimiento asignando las direcciones de forma decremental, las direcciones asignadas para cada red de 200 hosts quedan: 100.0.194.0/24; 100.0.193.0/24; 100.0.192.0/24 ... hasta 100.0.146.0/24 inclusive.

Finalmente las direcciones: `100.0.0.0` hasta `100.0.145.255` quedan disponibles para seguir subneteando.

---

#### Red de backbone

Necesitamos 7 bits para las direcciones que se solicitan, ya que: $2^{7}$ - 2 = 126 direcciones asignables.

Para esto nos posicionamos en la última red libre para empezar el subnetting:

100.0.145.255 -> Red de la cual partimos.

0110 0100.0000 0000.1001 0001.1111 1111 -> red expresada en bits.

0110 0100.0000 0000.1001 0001.1|**000 0000**| -> Colocamos en cero los bits que necesitamos para hosts.

0110 0100.0000 0000.|**1001 0001.1**|000 0000 -> Bits tomados para subred.

La nueva máscara de subred será /25

100.0.145.128/25 -> **dirección IP asignada para la red de backbone.**

Finalmente las direcciones: `100.0.0.0` hasta `100.0.145.127` quedan disponibles para seguir subneteando.