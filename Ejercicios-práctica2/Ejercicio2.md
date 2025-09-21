# Ejercicio 2

## Tomando un diagrama o una captura de un datagrama IPv4 e IPv6 indique la funcionalidad u objetivo de cada campo.

### IPv4

| **Campo** | **Función / Objetivo** |
|-------|------------------|
| **Version** | Indica la versión del protocolo IP. Para IPv4 siempre es `4`. |
| **Internet Header Length (IHL)** | Longitud del encabezado en palabras de 32 bits. Permite al receptor saber dónde comienza la sección de datos. |
| **Type of Service (TOS)** | Indica la prioridad y el tipo de servicio que se desea para el paquete. |
| &nbsp;&nbsp;&nbsp;&nbsp;**Precedence** | Prioridad del paquete (0 a 7). |
| &nbsp;&nbsp;&nbsp;&nbsp;**Delay** | Minimizar la latencia del paquete. |
| &nbsp;&nbsp;&nbsp;&nbsp;**Throughput** | Maximizar el rendimiento. |
| &nbsp;&nbsp;&nbsp;&nbsp;**Reliability** | Garantizar la entrega confiable. |
| &nbsp;&nbsp;&nbsp;&nbsp;**Reserved** | Reservado para uso futuro. |
| **Total Length (TL)** | Longitud total del datagrama en bytes (encabezado + datos). |
| **Identification** | Identifica el datagrama para reensamblar fragmentos en caso de que se divida. |
| **Flags** | Control de fragmentación. |
| &nbsp;&nbsp;&nbsp;&nbsp;**Reserved** | Reservado, siempre 0. |
| &nbsp;&nbsp;&nbsp;&nbsp;**Don't Fragment (DF)** | Indica que el paquete no debe fragmentarse. |
| &nbsp;&nbsp;&nbsp;&nbsp;**More Fragments (MF)** | Indica si hay más fragmentos del mismo datagrama. |
| **Fragment Offset** | Posición del fragmento dentro del datagrama original. |
| **Time to Live (TTL)** | Número máximo de saltos que el paquete puede realizar antes de descartarse. Evita bucles infinitos. |
| **Protocol** | Indica el protocolo de capa superior (TCP, UDP, ICMP, etc.). |
| **Header Checksum** | Verifica errores en el encabezado IP. |
| **Source Address** | Dirección IP de origen del datagrama. |
| **Destination Address** | Dirección IP de destino del datagrama. |
| **Options** | Opciones adicionales (como seguridad, rutas, timestamps). |
| &nbsp;&nbsp;&nbsp;&nbsp;**Padding** | Relleno para alinear el encabezado a múltiplos de 32 bits. |
| **Data** | Datos o carga útil del datagrama (ej. TCP/UDP). |

### IPv6

| Campo | Función / Objetivo |
|-------|------------------|
| **Version** | Indica la versión del protocolo. Para IPv6 siempre es `6`. |
| **Traffic Class** | Equivalente a TOS en IPv4, indica prioridad y calidad de servicio del paquete. |
| **Flow Label** | Identifica flujos de datos que requieren tratamiento especial, como streaming o VoIP. |
| **Payload Length** | Longitud de la carga útil (datos + encabezados de extensión) en bytes. |
| **Next Header** | Indica el tipo de encabezado que sigue (TCP, UDP, ICMPv6, u otros encabezados de extensión). |
| **Hop Limit** | Equivalente a TTL en IPv4; indica el número máximo de saltos que puede realizar el paquete. |
| **Source Address** | Dirección IP de origen del paquete. |
| **Destination Address** | Dirección IP de destino del paquete. |

---

## Si un paquete llega a un router con un TTL = 1, ¿qué hace el router? ¿Cómo se llama el campo TTL en IPv6?
- Si un paquete llega a un router con **TTL = 1**:
  - El router **descarta el paquete**.  
  - Envía un mensaje ICMP "Time Exceeded" al emisor.  
- En **IPv6**, el campo equivalente se llama **Hop Limit** y funciona de la misma forma.

---

## ¿En qué se diferencia el checksum de IPv4 e IPv6? Y en cuanto a los campos checksum de TCP y UDP, ¿sufren alguna modificación? Si un paquete tiene un error de checksum cuando llega a un router ¿qué sucede en IPv4 y en IPv6?
- **IPv4**: incluye un **checksum en la cabecera**, que se recalcula en cada salto (router).  
- **IPv6**: elimina este campo para simplificar el procesamiento (menor carga en routers).  
- **TCP y UDP**:
  - Ambos siguen teniendo **checksums obligatorios en IPv6** (en IPv4 eran opcionales en UDP).  
  - El cálculo incluye un **pseudo-encabezado** con las direcciones IP, lo cual cambia porque las direcciones son más largas en IPv6.  
- Si un paquete llega con un **error de checksum**:
  - En **IPv4 y en IPv6**: el router no corrige el error, simplemente **descarta el paquete**.  
  - La detección y retransmisión corresponde a la **capa de transporte** (TCP, si aplica).

---

## ¿Por qué no es necesario el campo Header Length en IPv6?
- No es necesario porque la **cabecera de IPv6 tiene tamaño fijo (40 bytes)**.  
- En IPv4 sí se necesita porque el tamaño puede variar debido a las **opciones**.

---

## Si quisiese que IPv4 soporte una nueva funcionalidad, ¿cómo lo haría? ¿y en IPv6?
- **En IPv4**: se agregan mediante el campo de **Opciones** en la cabecera.  
- **En IPv6**: se agregan mediante **Encabezados de Extensión**, encadenados al campo **Next Header**. Estos encabezados, solo aparecen si hacen falta, por lo que no siempre suelen visualizarse dentro de los diagramas de los datagramas IPv6.
