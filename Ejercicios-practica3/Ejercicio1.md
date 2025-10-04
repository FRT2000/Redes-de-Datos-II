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

Finalmente la red `65.0.0.0/28` queda libre para seguir subneteando.

---

#### Segunda red de 10 hosts

Partimos de la red 65.0.0.0/28 la cual queda libre para seguir con el mismo procedimiento.

Necesitamos otros 10 hosts por lo que la cantidad de bits que debemos tomar no cambia, con los 2 bits disponibles que teníamos para subred en el caso anterior es posible crear 4 subredes ya que: $2^{2}$ = 4. Donde cada una tendrá 10 hosts para este caso.

Ya hemos reservado la última dirección disponible para los primeros 10 hosts.

0100 0001.0000 0000.0000 0000.00|**11**| 0000 -> última red posible en el espacio de direcciones.

Lo que debemos hacer es restarle 1 (uno) a esa dirección de red y de esta manera obtener la anteúltima red posible del espacio de direcciones.

0100 0001.0000 0000.0000 0000.00|**10**| 0000 -> anteúltima red posible en el espacio de direcciones.

Por lo tanto el resultado final será:

65.0.0.32/28 -> **dirección IP asignada para los segundos 10 hosts.**

Si nos pidieran 2 redes más para otros 10 hosts cada una, repetiríamos el proceso de ir restando uno a la red anterior. En caso de necesitar más de 2 redes con 10 hosts cada una a partir de las asignaciones anteriores, no alcanzarían las direcciones. 

Finalmente la red `65.0.0.0/28` queda disponible para seguir subneteando.

---

###  Dada la red IP 100.0.0.0/16 se necesitan definir:
- 2(dos) redes de 2000 hosts
- 2(dos) redes de 500 hosts.
- 20(veinte) redes de 300 hosts.
- 50(cincuenta) redes de 200 hosts.
- Una red de backbone para unir cada uno de los router de las redes anteriores (74 direcciones).