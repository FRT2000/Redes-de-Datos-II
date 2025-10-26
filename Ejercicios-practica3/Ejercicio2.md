# Ejercicio 2

##  Resolver el ejercicio (1b) teniendo en cuenta una capacidad de crecimiento del 20 % para cada subred sin considerar el backbone.

Ahora necesitamos:
- 2 redes de 2000 hosts → 2000 × 1.2 = 2400 hosts cada una.
- 2 redes de 500 hosts → 500 × 1.2 = 600 hosts cada una.
- 20 redes de 300 hosts → 300 × 1.2 = 360 hosts cada una.
- 50 redes de 200 hosts → 200 × 1.2 = 240 hosts cada una.

#### Redes de 2400 hosts

Se necesitarán 12 bits designados para hosts, dado que:
$2^{12}$ - 2 = 4094 hosts.

100.0.0.0/16 -> red original

0110 0100.0000 0000.0000 |**0000.0000 0000**| -> bits tomados para los 2000 hosts.

|**0110 0100.0000 0000**|.0000 0000.0000 0000 -> bits de red original

0110 0100.0000 0000.|**0000**| 0000.0000 0000 -> bits tomados para subred 

0110 0100.0000 0000.|**1111**| 0000.0000 0000 -> bits tomados para subred colocados en 1

Nueva máscara de subred /20

100.0.240.0/20 -> **dirección IP asignada para los primeros 2000 hosts.**

100.0.224.0/20 -> **dirección IP asignada para los segundos 2000 hosts.** 

Finalmente las direcciones: `100.0.0.0/20` hasta `100.0.223.255/20` quedan libres para seguir subneteando.

---

#### Redes de 600 hosts

Se necesitarán 10 bits designados para hosts, dado que:

$2^{10}$ - 2 = 1022 hosts.

Para esto nos posicionamos en la última red libre para empezar el subnetting:

100.0.223.255/20 -> Red de la cual partimos.

0110 0100.0000 0000.1101 1111.1111 1111 -> red expresada en bits.

0110 0100.0000 0000.1101 11|**00.0000 0000**| -> Colocamos en cero los bits que necesitamos para hosts.

0110 0100.0000 0000.|**1101 11**|00.0000 0000 -> Bits tomados para subred.

La nueva máscara de subred será /22

100.0.220.0/22 -> **dirección IP asignada para la primera red de 600 hosts.**

100.0.216.0/22 -> **dirección IP asignada para los segundos 600 hosts.** 

Finalmente las direcciones: `100.0.0.0/22` hasta `100.0.215.255/22` quedan disponibles para seguir subneteando.

---

#### Redes de 360 hosts

Se necesitarán 9 bits designados para hosts, dado que:

$2^{9}$ - 2 = 510 hosts.

Para esto nos posicionamos en la última red libre para empezar el subnetting:

100.0.215.255/22 -> Red de la cual partimos.

0110 0100.0000 0000.1101 0111.1111 1111 -> red expresada en bits.

0110 0100.0000 0000.1101 011|**0.0000 0000**| -> Colocamos en cero los bits que necesitamos para hosts.

0110 0100.0000 0000.|**1101 011**|0.0000 0000 -> Bits tomados para subred.

La nueva máscara de subred será /23

100.0.214.0/23 -> **dirección IP asignada para la red número 1 de 360 hosts.**

100.0.212.0/23 -> **dirección IP asignada para la red número 2 de 360 hosts.**

100.0.210.0/23 -> **dirección IP asignada para la red número 3 de 360 hosts.**

100.0.208.0/23 -> **dirección IP asignada para la red número 4 de 360 hosts.**

100.0.206.0/23 -> **dirección IP asignada para la red número 5 de 360 hosts.**

100.0.204.0/23 -> **dirección IP asignada para la red número 6 de 360 hosts.**

100.0.202.0/23 -> **dirección IP asignada para la red número 7 de 360 hosts.**

100.0.200.0/23 -> **dirección IP asignada para la red número 8 de 360 hosts.**

100.0.198.0/23 -> **dirección IP asignada para la red número 9 de 360 hosts.**

100.0.196.0/23 -> **dirección IP asignada para la red número 10 de 360 hosts.**

100.0.194.0/23 -> **dirección IP asignada para la red número 11 de 360 hosts.**

100.0.192.0/23 -> **dirección IP asignada para la red número 12 de 360 hosts.**

100.0.190.0/23 -> **dirección IP asignada para la red número 13 de 360 hosts.**

100.0.188.0/23 -> **dirección IP asignada para la red número 14 de 360 hosts.**

100.0.186.0/23 -> **dirección IP asignada para la red número 15 de 360 hosts.**

100.0.184.0/23 -> **dirección IP asignada para la red número 16 de 360 hosts.**

100.0.182.0/23 -> **dirección IP asignada para la red número 17 de 360 hosts.**

100.0.180.0/23 -> **dirección IP asignada para la red número 18 de 360 hosts.**

100.0.178.0/23 -> **dirección IP asignada para la red número 19 de 360 hosts.**

100.0.176.0/23 -> **dirección IP asignada para la red número 20 de 360 hosts.**

Finalmente las direcciones: `100.0.0.0/23` hasta `100.0.175.255/23` quedan disponibles para seguir subneteando.

---

#### Redes de 240 hosts

Se necesitarán 8 bits designados para hosts, dado que:

$2^{8}$ - 2 = 254 hosts.

Para esto nos posicionamos en la última red libre para empezar el subnetting:

100.0.175.255/23 -> Red de la cual partimos.

0110 0100.0000 0000.1010 1111.1111 1111 -> red expresada en bits.

0110 0100.0000 0000.1010 1111.|**0000 0000**| -> Colocamos en cero los bits que necesitamos para hosts.

0110 0100.0000 0000.|**1010 1111**|.0000 0000 -> Bits tomados para subred.

La nueva máscara de subred será /24

100.0.175.0/24 -> **dirección IP asignada para la primera red de 240 hosts.**

Ahora siguiendo con el mismo procedimiento asignando las direcciones de forma decremental, las direcciones asignadas para cada red de 240 hosts quedan: 100.0.174.0/24; 100.0.173.0/24; 100.0.172.0/24 ... hasta 100.0.126.0/24 inclusive.

Finalmente las direcciones: `100.0.0.0/24` hasta `100.0.125.255/24` quedan disponibles para seguir subneteando.