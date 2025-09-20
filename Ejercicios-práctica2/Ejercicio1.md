# Ejercicio 1 

## ¿Cuál es la función de la capa de red en el modelo OSI? ¿Qué implementaciones conoce?

La **capa de red** es la **tercera capa** del modelo OSI y su función principal es **encaminar paquetes** desde el origen hasta el destino, incluso si se encuentran en redes distintas.

### Funciones principales:
- Direccionamiento lógico (ejemplo: **direcciones IP**).
- Encaminamiento/ruteo: selección de la mejor ruta hacia el destino.
- Fragmentación y reensamblado de paquetes.
- Control de congestión (en ciertos protocolos).

### Implementaciones comunes:
- **IPv4** (Internet Protocol versión 4).  
- **IPv6** (Internet Protocol versión 6).  
- Protocolos de ruteo: **OSPF, RIP, BGP, EIGRP**.  
- Otros relacionados: **ICMP**, **ARP**.

---

## ¿Qué es IPv6?
Es la **nueva versión del protocolo IP** diseñada para reemplazar a IPv4.  
- Usa **direcciones de 128 bits** (en lugar de 32 bits de IPv4).  
- Ejemplo de dirección IPv6: 2001:0db8:85a3:0000:0000:8a2e:0370:7334

### Características principales:
- Espacio de direcciones mucho más grande.
- Autoconfiguración de direcciones (SLAAC).
- Seguridad integrada (**IPsec obligatorio**).
- Soporte para movilidad y multicast.
- Cabecera simplificada para un ruteo más eficiente.

## ¿Por qué es necesaria su implementación?
- **Agotamiento de IPv4**: ya no hay suficientes direcciones para todos los dispositivos conectados.  
- Aunque existen soluciones como **NAT**, no son definitivas.  
- IPv6 permite que cada dispositivo tenga una dirección única.  
- Mejora la **escalabilidad de Internet**, la seguridad y la eficiencia en el ruteo.

