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

Finalmente las direcciones: `46.90.16.0` hasta `46.90.21.255` quedan libres para seguir subneteando.

### Red n11/n13 de 328 hosts

Nuevamente necesitamos 9 bits entonces le asiganamos la próxima red disponible decrementando en 1

0010 1110.0101 1010.0001 0|**10**|0.0000 0000 -> bits tomados para subred

46.90.20.0/23 -> **Dirección IP asignada para la red n11/n13.**

Finalmente las direcciones: `46.90.16.0` hasta `46.90.19.255` quedan libres para seguir subneteando.

### Red n9 de 40 hosts

46.90.19.255 -> Red de la cual partimos.

0010 1110.0101 1010.0001 0011.1111 1111 -> red expresada en bits.

0010 1110.0101 1010.0001 0011.11|**00 0000**| -> Colocamos en cero los bits que necesitamos para hosts.

0010 1110.0101 1010.0001 001|**1.11**|00 0000 -> Bits tomados para subred.

La nueva máscara de subred será /26

46.90.19.192/26 -> **Dirección IP asignada para la red n9.**

Finalmente las direcciones: `46.90.16.0` hasta `46.90.19.191` quedan libres para seguir subneteando.

### Red n10 de 2 hosts

46.90.19.191 -> Red de la cual partimos.

0010 1110.0101 1010.0001 0011.1011 1111 -> red expresada en bits

0010 1110.0101 1010.0001 0011.1011 11|**00**| -> Colocamos en cero los bits que necesitamos para hosts.

0010 1110.0101 1010.0001 0011.10|**11 11**|00 -> Bits tomados para subred.

La nueva máscara de subred será /30

46.90.19.188/30 -> **Dirección IP asignada para la red n10.**

Finalmente las direcciones: `46.90.16.0` hasta `46.90.19.187` quedan libres para seguir subneteando.

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

Finalmente las direcciones: `46.90.16.0` hasta `46.90.19.143` quedan libres para seguir subneteando.

---

### Asignación de direcciones a cada red a partir del bloque IPv4 asignado

![Bloques Asignados Ejercicio 12 Práctica 3](/Recursos-TPI/Ejercicio12-Practica3-Bloques-Asignados.png)

### Asignación de direcciones a cada host a partir del bloque IPv4 asignado

![Hosts Asignados Ejercicio 12 Práctica 3](/Recursos-TPI/Ejercicio12-Practica3-HostsIPv4-Asignados.png)

---

## Configurar la red detrás de n5 (n5,n13,n11) y la Red C con el bloque IPv6 asignado.

### Direcciones IPv6 asignadas con el bloque asignado 2001:db81::/32

A diferencia de IPv4, en IPv6 no se aplica VLSM. El espacio de direcciones es tan grande que la práctica estándar es asignar un prefijo /64 a cada subred.

Para organizar el direccionamiento, dividiremos el bloque /32 y lo dividimos en bloques /48 para cada red principal.

#### Asignación para Red A 2001:db81:000A::/48

Se divide la Red A en subredes, asignando un /64 a cada una.

Para este caso solo necesitamos una

Subred (n5, n11, n13):

**Red Asignada: 2001:db81:000A:0001::/64**


#### Asignación para Red C 2001:db81:000C::/48

Se divide la Red C en cuatro subredes, asignando un /64 a cada una.

Subred (n2, n7):

**Red Asignada: 2001:db81:000C:0001::/64**

Subred (n7, n8):

**Red Asignada: 2001:db81:000C:0002::/64**

Subred (n9):

**Red Asignada: 2001:db81:000C:0003::/64**

Subred (n14):

**Red Asignada: 2001:db81:000C:0004::/64**

---

### Asignación de direcciones a cada host a partir del bloque IPv6 asignado

![Hosts IPv6 Asignados Ejercicio 12 Práctica 3](/Recursos-TPI/Ejercicio12-Practica3-HostsIPv6-Asignados.png)

---

## Resolver con ruteo estático la topología.
## Realizar test con ping (ICMP) y traceroute para probar que funciona la topología.

### Comandos aplicados a cada router

**Router n5**
- `ip route add default via 46.90.19.182`

**Router n6**
- `ip route add default via 46.90.19.178`
- `ip route add 46.90.20.0/23 via 46.90.19.185`

**Router n3**
- `ip route add 46.90.20.0/23 via 46.90.19.181`
- `ip route add 46.90.19.184/30 via 46.90.19.181`
- `ip route add 46.90.19.188/30 via 46.90.19.166`
- `ip route add 46.90.19.160/30 via 46.90.19.166`
- `ip route add 46.90.19.168/30 via 46.90.19.174`
- `ip route add 46.90.19.152/30 via 46.90.19.158`
- `ip route add 46.90.19.148/30 via 46.90.19.158`
- `ip route add 46.90.19.144/30 via 46.90.19.158`
- `ip route add 46.90.19.192/26 via 46.90.19.158`
- `ip route add 46.90.22.0/23 via 46.90.19.158`

**Router n1**
- `ip route add 46.90.20.0/23 via 46.90.19.165`
- `ip route add 46.90.19.184/30 via 46.90.19.165`
- `ip route add 46.90.19.180/30 via 46.90.19.165`
- `ip route add 46.90.19.176/30 via 46.90.19.165`
- `ip route add 46.90.19.156/30 via 46.90.19.165`
- `ip route add 46.90.19.172/30 via 46.90.19.165`
- `ip route add 46.90.19.168/30 via 46.90.19.165`
- `ip route add 46.90.19.152/30 via 46.90.19.162`
- `ip route add 46.90.19.148/30 via 46.90.19.162`
- `ip route add 46.90.19.144/30 via 46.90.19.162`
- `ip route add 46.90.19.192/26 via 46.90.19.162`
- `ip route add 46.90.22.0/23 via 46.90.19.162`


**Router n15**
- `ip route add 46.90.20.0/23 via 46.90.19.173`
- `ip route add 46.90.19.184/30 via 46.90.19.173`
- `ip route add 46.90.19.180/30 via 46.90.19.173`
- `ip route add 46.90.19.176/30 via 46.90.19.173`
- `ip route add 46.90.19.164/30 via 46.90.19.173`
- `ip route add 46.90.19.188/30 via 46.90.19.173`
- `ip route add 46.90.19.160/30 via 46.90.19.173`
- `ip route add 46.90.19.156/30 via 46.90.19.173`
- `ip route add 46.90.19.152/30 via 46.90.19.170`
- `ip route add 46.90.19.148/30 via 46.90.19.170`
- `ip route add 46.90.19.144/30 via 46.90.19.170`
- `ip route add 46.90.19.192/26 via 46.90.19.170`
- `ip route add 46.90.22.0/23 via 46.90.19.170`


**Router n4**
- `ip route add default via 46.90.19.154`
- `ip route add 46.90.20.0/23 via 46.90.19.169`
- `ip route add 46.90.19.184/30 via 46.90.19.169`
- `ip route add 46.90.19.180/30 via 46.90.19.169`
- `ip route add 46.90.19.176/30 via 46.90.19.169`
- `ip route add 46.90.19.164/30 via 46.90.19.169`
- `ip route add 46.90.19.188/30 via 46.90.19.169`
- `ip route add 46.90.19.172/30 via 46.90.19.169`

**Router n2**
- `ip route add default via 46.90.19.150`
- `ip route add 46.90.20.0/23 via 46.90.19.157`
- `ip route add 46.90.19.184/30 via 46.90.19.157`
- `ip route add 46.90.19.180/30 via 46.90.19.157`
- `ip route add 46.90.19.176/30 via 46.90.19.157`
- `ip route add 46.90.19.164/30 via 46.90.19.157`
- `ip route add 46.90.19.172/30 via 46.90.19.157`
- `ip route add 46.90.19.168/30 via 46.90.19.153`
- `ip route add 46.90.19.188/30 via 46.90.19.161`

**Router n7**
- `ip route add default via 46.90.19.149`
- `ip route add 46.90.19.192/26 via 46.90.19.146`
- `ip route add 46.90.22.0/23 via 46.90.19.146`

**Router n8**
- `ip route add default via 46.90.19.145`

---

## Alternativo: Asignar a n10 una IP según RFC-1918 y configurar NAT en n1 para que pueda alcanzar al resto de los equipos.

Se eliminó la dirección de la red `46.90.19.188/30` en cada router, ya que ahora la red de n10 tiene la dirección privada `192.168.1.0/24`.

Comando agregado dentro del **Router n1** 
- `iptables -t nat -A POSTROUTING -s 192.168.1.0/24 -j MASQUERADE`

### Asignación de direcciones privadas

![Direcciones privadas Asignadas Ejercicio 12 Práctica 3](/Recursos-TPI/Ejercicio12-Practica3-Direcciones-Privadas.png)

---

## Capturar puntualmente el tráfico de n13 hacia n7 y analizar: ARP e ICMP.

### Captura de tráfico realizando ping de n13 hacia n14

![Captura ping n13 hacia n14 Ejercicio 12 Práctica 3](/Recursos-TPI/Ejercicio12-Practica3-Captura-n13-n14.png)

![Captura ping n13 hacia n14 Detalle Ejercicio 12 Práctica 3](/Recursos-TPI/Ejercicio12-Practica3-Captura-n13-n14-detalle.png)

- Análisis ARP (Paquetes 7 y 8):
    - El ping (ICMP) no puede salir de inmediato. n13 sabe que n14 está en otra red, por lo que primero debe encontrar la dirección MAC de su gateway (n5, en ...20.1).
    - Paquete 7: Es la solicitud ARP de n13 ("¿Quién tiene la IP 46.90.20.1?").
    - Paquete 8: Es la respuesta ARP del gateway n5, informando su dirección MAC (00:00:00:aa:00:02).

- Análisis ICMP (Paquetes 9 y 10):
    - Una vez resuelto el ARP, n13 envía el ping.
    - Paquete 9 (Request): Su destino IP es n14 (46.90.22.2), pero su destino MAC es el gateway n5 (00:00:00:aa:00:02).
    - Paquete 10 (Reply): Es la respuesta de n14 que regresa. El gateway n5 la recibe y entrega localmente a la MAC de n13.

---

### Realizar un traceroute entre los mismos equipos, capturar los mensajes.

### Captura de tráfico realizando traceroute de n13 hacia n14

![Captura traceroute n13 hacia n14 Ejercicio 12 Práctica 3](/Recursos-TPI/Ejercicio12-Practica3-Captura-n13-n14-traceroute-completo.png)

- Aparecen numerosas entradas “Time-to-live exceeded (in transit)” provenientes de las interfaces de los routers (enlaces punto-a-punto).
- La última respuesta fue “Destination unreachable (Port unreachable)” desde 46.90.22.2, lo que indica llegada al bloque de RED C y, por lo tanto, al host destino (n14).
- Cada salto presenta varias respuestas porque traceroute emite varios paquetes por TTL (normalmente 3).
- Se observan paquetes UDP salientes y las respuestas ICMP de los saltos intermedios.

---

## Alternativo: Modificar los MTU para ver la fragmentación.

### Comandos utilizados para modificar el MTU del enlace entre n2 y n7
  
**Router n7**

`ip link set dev eth0 mtu 500` -> en la interfaz eth0

`ip link show eth0` -> verificar el MTU configurado en eth0

**Router n2**

`ip link set dev eth3 mtu 500` -> en la interfaz eth3

`ip link show eth3` -> verificar el MTU configurado en eth3

### Captura de tráfico realizando ping de n13 hacia n14 modificando MTU entre n2 y n7

Se utilzó el comando `ping 46.90.22.2 -s 1000 -c 1 -M dont` dentro de n13

![Captura ping n13 hacia n14 MTU Ejercicio 12 Práctica 3](/Recursos-TPI/Ejercicio12-Practica3-Captura-n13-n14-MTU.png)
 
---

## Probar conectividad en las redes con IPv6 (por separado), capturar tráfico y analizar ICMPv6

### Comandos aplicados dentro de los dispositivos dentro de la Red A

Para el caso de la subred (n5, m13 y n11) no hizo falta configurar rutas ya que los dispositivos se encuentran directamente conectados dentro de la misma red.

### Comandos aplicados dentro de la Red C

**Router n2**
- `ip -6 route add default via 2001:db81:000C:0001::2`

**Router n7**
- `ip -6 route add default via 2001:db81:000C:0002::2`

**Router n8**
- `ip -6 route add default via 2001:db81:000C:0002::1`

