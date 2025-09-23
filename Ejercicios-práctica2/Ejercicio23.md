# Ejercicio 23

## ¿Qué funcionalidad cumplen las direcciones de tipo link-local en IPv6? 
Las direcciones link-local en IPv6 (prefijo asignado FE80::/10, típicamente utilizadas con longitud /64) cumplen la función de permitir la comunicación únicamente dentro del enlace local, es decir, en la red directamente conectada.

Se generan de manera automática en todas las interfaces, incluso aunque el host no haya recibido otra dirección (global o ULA). Esto las hace imprescindibles para:

- Descubrimiento de vecinos (NDP),
- Comunicación con el router de la red (por ejemplo, para el salto siguiente),
- Autoconfiguración básica al inicio de la conexión.

## ¿Qué analogía se puede hacer con IPv4?
En cuanto a la analogía con IPv4, se pueden comparar con las direcciones APIPA (169.254.0.0/16), que permiten la comunicación local cuando no hay un servidor DHCP disponible.

Sin embargo, a diferencia de IPv4, en IPv6 las direcciones link-local no son opcionales: toda interfaz debe tener al menos una dirección link-local y se utilizan de forma activa en el funcionamiento normal de la red.