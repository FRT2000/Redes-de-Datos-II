# Ejercicio 1

## ¿Cuáles son las funciones de la capa de transporte en el modelo OSI? 

La capa de transporte tiene como objetivo principal proveer una comunicación lógica entre procesos de aplicación que se ejecutan en hosts diferentes. No se encarga de la comunicación entre dispositivos (eso es IP), sino entre los programas que corren en ellos.

Sus funciones generales incluyen:
-  **Multiplexación/Demultiplexación:** Permitir que varias aplicaciones usen la red a la vez usando puertos.
-  **Comunicación Proceso a Proceso:** Extender la entrega del host (IP) al proceso específico (aplicación).
-  **Segmentación:** Dividir los datos de la aplicación en trozos manejables.
-  **Confiabilidad (Control de Errores):** Garantizar que los datos lleguen y recuperarlos si se pierden (aunque no todos los protocolos lo hacen).
-  **Control de Flujo y Congestión:** Regular la velocidad para no saturar al receptor ni a la red.

## ¿Cuáles implementan TCP y cuáles UDP? 

De las funciones generales de la capa de transporte, TCP las implementa todas (Multiplexación, Confiabilidad, Ordenamiento, Control de Flujo y Congestión), ofreciendo un servicio orientado a la conexión. En contraste, UDP solamente implementa la Multiplexación (y una detección de errores básica sin recuperación), descartando las funciones de confiabilidad, orden y control de flujo/congestión para ser más ligero.

## ¿Existen otros protocolos de transporte en el stack TCP/IP? 

**QUIC (Quick UDP Internet Connections)**
- Estado: Estándar IETF (RFC 9000).
- Función: Es un protocolo de transporte seguro orientado a conexión que reduce la latencia de establecimiento (handshake).
- Clave: Aunque funciona a nivel de transporte, se encapsula sobre UDP y se implementa usualmente en el espacio de usuario (no en el kernel) para permitir actualizaciones rápidas. Es la base del estándar HTTP/3.


**SCTP (Stream Control Transmission Protocol)**
- Estado: Estándar IETF (RFC 4960).
- Función: Combina lo mejor de TCP y UDP. Es confiable (como TCP) pero orientado a mensajes (como UDP).
- Características únicas:
    - Multi-homing: Permite que una conexión use múltiples direcciones IP simultáneamente (ej: si falla la interfaz WiFi, sigue por 4G sin cortar la conexión).
    - Multi-streaming: Evita el bloqueo de cabecera de línea (Head-of-Line blocking) enviando varios flujos independientes dentro de una misma conexión.
- Uso: Es el estándar de oro en redes de telecomunicaciones (redes móviles 4G/LTE y 5G usan SCTP para la señalización entre antenas y núcleos de red).

**DCCP (Datagram Congestion Control Protocol)**
- Estado: Estándar IETF (RFC 4340).
- Función: Imagínalo como un UDP pero "educado".
- Características: Provee envío de datagramas no confiable (como UDP) pero agrega control de congestión (como TCP).
- Uso: Diseñado para aplicaciones de streaming o juegos que no quieren las retransmisiones de TCP (que causan lag) pero necesitan mecanismos para no saturar la red (algo que UDP no tiene).

## ¿Cuáles son los más utilizados? 

A continuación ordenaremos los protocolos mencionados empezando por el más usado:

- TCP: Sigue dominando la inmensa mayoría del tráfico (Web clásica HTTP/1.1 y HTTP/2, Correo electrónico, Transferencia de archivos, Base de datos). Es el estándar por defecto para todo lo que requiere fiabilidad.
- UDP: Esencial para todo lo que es tiempo real (VoIP, Videoconferencias, Gaming online) y servicios de infraestructura básica como DNS y DHCP.
- QUIC: Ha tenido un crecimiento explosivo. Al ser la base de HTTP/3 y ser impulsado por Google (Chrome, YouTube) y Facebook, ya representa un porcentaje muy significativo del tráfico mundial, desplazando a TCP en la web moderna.
- SCTP: Muy utilizado pero en nichos de infraestructura (Backbones de telefonía móvil), raramente usado directamente por aplicaciones de usuario final web.

## ¿En qué protocolo se encapsulan y en qué parte de un sistema se los suele encontrar: en el kernel del SO, en espacio de usuario, cómo microservicios fuera del kernel?

**¿En qué protocolo se encapsulan?**

- TCP y UDP: Ambos se encapsulan directamente dentro de paquetes IP (Capa de Red).
    - En el encabezado IP, el campo de protocolo indica qué transporte lleva dentro: el valor 6 para TCP y el valor 17 para UDP.
- QUIC: Se encapsula dentro de datagramas UDP. Es decir, viaja "sobre" UDP y, a su vez, ese datagrama UDP viaja dentro de un paquete IP.

**¿En qué parte de un sistema se los suele encontrar?**

- En el Kernel del SO:
    - Acá se encuentran tradicionalmente TCP y UDP.

- En Espacio de Usuario (User Space):
    - Acá es donde se encuentra QUIC.
- Como microservicios fuera del kernel
    - Se alinea con la arquitectura de QUIC y las implementaciones modernas. Al correr en espacio de usuario, el protocolo de transporte no es un servicio monolítico del núcleo, sino que funciona como una librería o parte del binario de la aplicación/microservicio.
