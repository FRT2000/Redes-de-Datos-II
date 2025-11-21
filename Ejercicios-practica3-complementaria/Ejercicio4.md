# Ejercicio 4

## Analizar la captura de 01-dhcp.pcap

### Indicar que mensajes DHCP se intercambian en el diálogo para obtener una dirección IP.

El diálogo completo para obtener la dirección IP se ve en las líneas 1, 4, 5 y 6:
- Paquete 1: DHCP Discover (Cliente busca servidor).
- Paquete 4: DHCP Offer (Servidor ofrece IP).
- Paquete 5: DHCP Request (Cliente acepta la oferta).
- Paquete 6: DHCP ACK (Servidor confirma y finaliza).

### Indicar que direcciones físicas/MAC y lógicas/IP utiliza el mensaje Discover.

Dirección Lógica (IP):
- Origen: 0.0.0.0 (El cliente aún no tiene IP).
- Destino: 255.255.255.255 (Broadcast).

Dirección Física (MAC):
- Origen: 52:54:00:12:34:57 (MAC Cliente)
- Destino: ff:ff:ff:ff:ff:ff (Broadcast)

### ¿Qué parámetros solicita para configuración automática el cliente?

- Subnet Mask
- Broadcast Address
- Time Offset
- Router
- Domain Name
- Domain Name Server
- Host Name
- NetBIOS over TCP/IP Name Server
- NetBIOS over TCP/IP Scope

### ¿Cuál es la respuesta al mismo y qué valores le ofrece?

- Client IP address: 200.1.1.205
- DHCP Server Identifier: 200.1.1.201
- IP Address Lease Time: 10 minutes
- Subnet Mask: 255.255.255.192
- Broadcast Address: 200.1.1.255
- Router: 200.1.1.201
- Domain Name: cities.org
- Domain Name Server: 200.1.1.200

### ¿Qué direcciones físicas/MAC y lógicas/IP lleva la respuesta?
Dirección Lógica (IP):
- Origen: 200.1.1.201 (Servidor)
- Destino: 200.1.1.205 (IP ofrecida al cliente)

Dirección Física (MAC):
- Origen: 52:54:00:12:34:56 (MAC Servidor)
- Destino: 52:54:00:12:34:57 (MAC Cliente)

###  ¿Cómo identifica el servidor al cliente, por cuanto tiempo la dirección asignada la deberá tener el cliente antes de intentar renovarla? ¿Qué mensajes utiliza para renovar la dirección y cuáles son las posibles respuestas? ¿Qué direcciones lógicas y físicas utilizan estos mensajes?

El servidor utiliza la dirección física (MAC Address) del cliente para identificarlo de forma única.

El cliente intenta renovar la dirección cuando ha transcurrido el 50% del tiempo de concesión (Lease Time). Este momento se conoce técnicamente como T1 Timer.

El cliente envía un mensaje DHCP REQUEST. A diferencia del proceso inicial (donde el Request suele ser Broadcast), en la renovación este mensaje es Unicast dirigido directamente al servidor, porque el cliente ya sabe quién es.

Posibles respuestas del servidor:
- DHCP ACK (Acknowledgment): "Sí, puedes seguir usando la IP. Reinicio tu contador de tiempo". (El cliente renueva el alquiler).
- DHCP NAK (Negative Acknowledgment): "No, esa IP ya no es válida para ti". (El cliente debe dejar de usar la IP inmediatamente y comenzar el proceso DORA desde cero).

A diferencia del inicio (que usaba 0.0.0.0 y Broadcast), en la renovación el cliente ya tiene identidad:
- Direcciones Lógicas (IP):
    - Origen: La IP actual del Cliente (en tu caso: 200.1.1.205).
    - Destino: La IP del Servidor DHCP (en tu caso: 200.1.1.201).
- Direcciones Físicas (MAC):
    - Origen: MAC del Cliente (52:54:00:12:34:57).
    - Destino: MAC del Servidor (52:54:00:12:34:56).

### ¿Qué protocolo de transporte utiliza DHCP y que puertos?

DHCP utiliza el protocolo de transporte UDP (User Datagram Protocol). No utiliza TCP porque TCP requiere establecer una conexión previa (Three-way handshake) para lo cual se necesitan direcciones IP origen y destino, algo que el cliente no tiene al inicio del proceso.

Los puertos utilizados son:
- Puerto 67 (UDP): Es el puerto de escucha del Servidor. El cliente envía sus mensajes (como el Discover o Request) con destino al puerto 67.
- Puerto 68 (UDP): Es el puerto de escucha del Cliente. El servidor envía sus respuestas (como el Offer o ACK) con destino al puerto 68.

### ¿Históricamente qué protocolo antecedieron a DHCP?

Existen dos antecedentes principales que evolucionaron hasta llegar al DHCP actual:

- RARP (Reverse Address Resolution Protocol): Fue el primer intento (RFC 903). Permitía a una estación sin disco conocer su IP a partir de su dirección MAC.
    - Limitación: Solo entregaba la dirección IP, no podía configurar máscara de subred, ni gateway, ni DNS. Además, no atravesaba routers (no enrutable).

- BOOTP (Bootstrap Protocol): Es el antecesor directo (RFC 951). DHCP se diseñó como una extensión de BOOTP. BOOTP solucionó los problemas de RARP enviando más datos de configuración (máscara, gateway, etc.) y permitiendo el reenvío a través de routers (Relay Agents).
    - Limitación: BOOTP era estático; el administrador debía cargar manualmente la relación MAC-IP en el servidor. No existía el concepto de "arrendamiento" (Lease) dinámico o recuperación automática de IPs.

### ¿Si el cliente decide no usar más el recurso qué mensaje debería enviar? Tiene respuesta?

El cliente debe enviar un mensaje DHCP RELEASE. Este mensaje se utiliza para liberar la dirección IP de forma ordenada antes de que termine el tiempo de concesión.

No tiene respuesta. El protocolo DHCP no contempla un mensaje de confirmación (ACK) para el Release.

Como el cliente está avisando que "se va" o que "cierra la conexión", no tiene sentido que el servidor gaste recursos enviando una confirmación a alguien que probablemente ya desconectó su interfaz de red o borró su dirección IP. El cliente envía el DHCP RELEASE y asume que el servidor lo procesará, cortando la comunicación inmediatamente.
