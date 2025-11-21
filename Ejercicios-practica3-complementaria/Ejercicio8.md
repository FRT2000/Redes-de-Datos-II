# Ejercicio 8

## Analizar la captura: ipv6-nd.pcapng. Indicar cuáles son los mensajes para el SLAAC (Stateless Address Autoconfiguration). ¿Qué parámetros recibe el dispositivo que se conecta a la red. Indicar sus valores. Indicar qué dirección IPv6 se podría autogenerar y con qué long. De prefijo. ¿Cuál sería la utilidad/servicio de DHCPv6 en el caso de tener SLAAC activado? Puede probase con el simulador utilizando el archivo: ipv6-nd-radvd.imn. Previamente debe instalar el servicio radvd.


### Mensajes para SLAAC (Stateless Address Autoconfiguration)

El proceso de autoconfiguración sin estado se basa en el diálogo entre el Host (PC) y el Router.

**Router Solicitation (RS):**

- En la captura: Paquetes Nº 12 (y también 2, 38, 58).
- Descripción: El host (que aún no tiene IP Global) envía este mensaje a la dirección multicast ff02::2 (todos los routers) preguntando: "¿Hay algún router en esta red? Necesito información para configurarme".
- El Host usa su dirección Link-Local (fe80::...) como origen.

**Router Advertisement (RA):**

- En la captura: Paquete Nº 29 (y también 43, 47, 55...).
- Descripción: El router responde enviando este mensaje a ff02::1 (todos los nodos). Dice: "Aquí estoy. Este es el prefijo de red que deben usar".
- Este es el mensaje que contiene los parámetros vitales para SLAAC.

### Parámetros que recibe el dispositivo (Valores)

- Prefijo: 2001:db8:: (Se deduce porque luego las PCs usan IPs que empiezan con esto).
- Longitud de Prefijo: /64 (Es el estándar para SLAAC).
- Flags (Banderas):
    - El Flag A (Autonomous) debe estar en 1 (Set): Esto le dice a la PC "Usa este prefijo para generar tu propia IP".
- MTU: Generalmente 1500.

### Dirección IPv6 Autogenerada

El dispositivo toma el prefijo que le dio el router y le suma su propio ID de interfaz (calculado con su MAC mediante EUI-64).

- Prefijo recibido: 2001:db8::/64
- Interface ID (Host): Si miramos el Paquete 15 (Neighbor Solicitation), vemos que el host tiene la Link-Local fe80::200:ff:feaa:1.
    - Esto nos dice que su sufijo EUI-64 es: ::200:ff:feaa:1.

Resultado de la Autoconfiguración: La dirección IPv6 Global Unicast que se genera es: 2001:db8::200:ff:feaa:1 con prefijo /64.

### ¿Cuál sería la utilidad de DHCPv6 teniendo SLAAC activado?

- SLAAC se encarga de dar la Dirección IP y el Gateway (Rápido y eficiente).
- DHCPv6 se usa solo para entregar "Información Adicional":
    - Direcciones de Servidores DNS.
    - Nombre de Dominio (ej: empresa.local).
    - Servidores NTP (Hora), TFTP, etc.