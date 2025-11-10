# Ejercicio 12 de la Práctica 3

## Resolver el direccionamiento IPv4 con el bloque IP asignado. Considerar los enlaces punto a punto salvo la red de n9, n10, n11, n13 y n14. Para la red de n9 considerar 40 hosts; para la red de n11 y n13, 328 hosts y para la red de n14, 500 hosts.

![Diagrama Ejercicio 12 Práctica 3](/Recursos-TPI/Ejercicio12-Practica3-Diagrama.png)

---

### Direcciones IPv4 asignadas con el bloque asignado 46.90.16.0/21

El objetivo es dividir el bloque 46.90.16.0/21 usando VLSM (Máscara de Subred de Longitud Variable) para cubrir todas las necesidades de la topología.

Primero identificamos los requerimientos de cada subred y el prefijo que se le debe asignar

| Red | Requerimiento (Hosts) | Bits necesarios | Prefijo Asignado |
| :--- | :--- | :--- | :--- |
| Red n14 | 500 hosts | 9 | **/23** |
| Red n11/n13 | 328 hosts | 9 | **/23** |
| Red n9 | 40 hosts | 6 | **/26** |
| Red n10 | 2 hosts | 2 | **/30** |
| 11 Enlaces Punto a Punto | 2 hosts c/u | 2 | **/30** (x11) |

### Red n14 de 500 hosts

46.90.16.0/21 -> red original

0010 1110.0101 1010.0001 000|**0.0000 0000**| -> bits tomados para los 500 hosts.

|**0010 1110.0101 1010.0001 0**|000.0000 0000 -> bits de red original

0010 1110.0101 1010.0001 0|**00**|0.0000 0000 -> bits tomados para subred 

0010 1110.0101 1010.0001 0|**11**|0.0000 0000 -> bits tomados para subred colocados en 1

Nueva máscara de subred /23

46.90.22.0/23 -> **Dirección IP asignada para la red n14.**

Finalmente las direcciones: `46.90.16.0/23` hasta `46.90.21.255/23` quedan libres para seguir subneteando.

### Red n11/n13 de 328 hosts

Nuevamente necesitamos 9 bits entonces le asiganamos la próxima red disponible decrementando en 1

0010 1110.0101 1010.0001 0|**10**|0.0000 0000 -> bits tomados para subred

46.90.20.0/23 -> **Dirección IP asignada para la red n11/n13.**

Finalmente las direcciones: `46.90.16.0/23` hasta `46.90.19.255/23` quedan libres para seguir subneteando.

### Red n9 de 40 hosts

46.90.19.255/23 -> Red de la cual partimos.

0010 1110.0101 1010.0001 0011.1111 1111 -> red expresada en bits.

0010 1110.0101 1010.0001 0011.11|**00 0000**| -> Colocamos en cero los bits que necesitamos para hosts.

0010 1110.0101 1010.0001 001|**1.11**|00 0000 -> Bits tomados para subred.

La nueva máscara de subred será /26

46.90.19.192/26 -> **Dirección IP asignada para la red n9.**

Finalmente las direcciones: `46.90.16.0/26` hasta `46.90.19.191/26` quedan libres para seguir subneteando.

### Red n10 de 2 hosts

46.90.19.191/26 -> Red de la cual partimos.

0010 1110.0101 1010.0001 0011.1011 1111 -> red expresada en bits

0010 1110.0101 1010.0001 0011.1011 11|**00**| -> Colocamos en cero los bits que necesitamos para hosts.

0010 1110.0101 1010.0001 0011.10|**11 11**|00 -> Bits tomados para subred.

La nueva máscara de subred será /30

46.90.19.188/30 -> **Dirección IP asignada para la red n10.**

Finalmente las direcciones: `46.90.16.0/30` hasta `46.90.19.187/30` quedan libres para seguir subneteando.

### Enlaces punto a punto

Nuevamente necesitamos 2 bits entonces le asiganamos la próxima red disponible de forma decremental

46.90.19.184/30 -> **Dirección IP asignada para enlace punto a punto número 1.**

46.90.19.180/30 -> **Dirección IP asignada para enlace punto a punto número 2.**

46.90.19.176/30 -> **Dirección IP asignada para enlace punto a punto número 3.**

46.90.19.172/30 -> **Dirección IP asignada para enlace punto a punto número 4.**

46.90.19.168/30 -> **Dirección IP asignada para enlace punto a punto número 5.**

46.90.19.164/30 -> **Dirección IP asignada para enlace punto a punto número 6.**

46.90.19.160/30 -> **Dirección IP asignada para enlace punto a punto número 7.**

46.90.19.156/30 -> **Dirección IP asignada para enlace punto a punto número 8.**

46.90.19.152/30 -> **Dirección IP asignada para enlace punto a punto número 9.**

46.90.19.148/30 -> **Dirección IP asignada para enlace punto a punto número 10.**

46.90.19.144/30 -> **Dirección IP asignada para enlace punto a punto número 11.**

Finalmente las direcciones: `46.90.16.0/30` hasta `46.90.19.143/30` quedan libres para seguir subneteando.

---

La asignación de cada espacio de direcciones a partir del bloque IPv4 asignado es el siguiente:

![Bloques Asignados Ejercicio 12 Práctica 3](/Recursos-TPI/Ejercicio12-Practica3-Bloques-Asignados.png)


a) Configurar la red detrás de n5 (n5,n13,n11) y la Red C con el bloque IPv6 asignado.
b) Resolver con ruteo estático la topología.
c) Alternativo: Asignar a n10 una IP según RFC-1918 y configurar NAT en n1 para que
pueda alcanzar al resto de los equipos.
d) Realizar test con ping (ICMP) y traceroute para probar que funciona la topología.
e) Capturar puntualmente el tráfico de n13 hacia n7 y analizar: ARP e ICMP.
f) Realizar un traceroute entre los mismos equipos, capturar los mensajes.
g) Alternativo: Modificar los MTU para ver la fragmentación.
h) Probar conectividad en las redes con IPv6 (por separado), capturar tráfico y analizar
ICMPv6