# Ejercicio 19

## ¿Para qué sirve el protocolo ARP? 
- ARP (Address Resolution Protocol) se usa en redes IPv4 para mapear direcciones lógicas (IP) a direcciones físicas (MAC) dentro de una red local.
- Ejemplo: cuando un host quiere enviar un paquete a la IP 192.168.1.5, necesita saber cuál es la MAC address de esa máquina en la LAN. ARP se encarga de preguntar “¿quién tiene esta IP?” y el host con esa IP responde con su dirección MAC.

---

## ¿En qué protocolos de enlace no sería necesario? 
- ARP solo es necesario cuando la capa de enlace usa direcciones físicas distintas de las lógicas.
- No se necesita ARP en protocolos de enlace donde la dirección de enlace y la dirección de red coinciden o son la misma cosa, por ejemplo:
    - X.25
    - Frame Relay
    - ATM
    - PPP (Point-to-Point Protocol) → porque es un enlace directo punto a punto, no hay necesidad de resolver direcciones.

---

## ¿Es necesario en IPv6? 
- No. En IPv6 no se usa ARP.

---

## ¿Qué se utiliza en IPv6?
- IPv6 reemplaza ARP con el NDP (Neighbor Discovery Protocol).
- NDP cumple funciones similares, pero además mejora y amplía las capacidades de ARP:
    - Resolución de direcciones (IP → MAC).
    - Descubrimiento de routers.
    - Detección de direcciones duplicadas (Duplicate Address Detection).
    - Descubrimiento de la MTU del enlace.
- NDP funciona mediante mensajes ICMPv6 (Neighbor Solicitation y Neighbor Advertisement).