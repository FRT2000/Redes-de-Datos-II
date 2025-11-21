# Ejercicio 7

## Capturar mensajes DHCP en vivo, desde su dispositivo e indicar cual es el servidor DHCP, y qué parámetros obtiene del mismo. ¿En el caso de no poder usar DHCP que otro protocolo usan los ISPs sobre tecnologías de enlace que no son broadcast?

Para este punto se modificó el adaptador de Red de la VM para que se conecte como "Adaptador puente", de esta manera fue posible capturar los mensajes DHCP desde mi dispositivo a partir de los siguientes comandos:

- `ip a` -> para reconocer interfaces activas
- `sudo tcpdump -i enp0s3 port 67 or 68 -vv` -> para capturar los mensajes DHCP

Los ISP, cuando la tecnología NO permite broadcast (o sea, no se puede usar DHCP), utilizan:

**PPPoE (Point-to-Point Protocol over Ethernet):**

Es el protocolo más usado cuando NO es posible usar DHCP tradicional, porque:
- Establece una conexión punto a punto (no broadcast)
- Permite autenticación (username + password, estilo ADSL)
- Asigna IP usando PPP, no DHCP

Es típico en:
- ADSL
- FTTH (Fibertel a veces lo usa internamente)
- Redes de acceso que no son Ethernet real

**Otros mecanismos posibles (según el ISP)**

- IP estática provisionada
- DHCP Option 82 (relay con control por puertos)
- DHCPv6-PD (para IPv6 delegación de prefijos, si el medio no soporta broadcast)
- Protocolo de control del dispositivo ONT/ONU (GPON) para autenticar al cliente