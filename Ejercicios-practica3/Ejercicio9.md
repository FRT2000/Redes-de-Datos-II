# Ejercicio 9

## Fragmentación IPv6: dada la configuración de la figura 3 pero reemplazando IPv4 por IPv6 y considerando que los frames de link layer requieren 18 bytes de overhead y los datagramas IPv6 40 bytes, analizar los MTUs mínimos y responder:

### ¿Cómo se resuelve la fragmentación en IPv6?

- Los routers NO fragmentan: En IPv6, los routers (como n2) nunca fragmentan un paquete. Si un router recibe un paquete que es más grande que el MTU del siguiente enlace, su único trabajo es descartar el paquete.
- Notificación ICMPv6: Después de descartarlo, el router (n2) envía un mensaje ICMPv6 tipo 2, "Packet Too Big" (Paquete Demasiado Grande), de vuelta al host de origen (n1). Este mensaje le informa a n1 cuál es el MTU exacto del enlace problemático.
- El Origen fragmenta: El host de origen (n1) es ahora el único responsable de la fragmentación. n1 debe tomar los datos originales, dividirlos en trozos más pequeños (que quepan en el MTU informado) y volver a enviarlos. Para hacer esto, utiliza una Cabecera de Extensión de Fragmentación en cada nuevo paquete.

#### Recreando el escenario del Ejercicio 7

- n1 quiere enviar 1000 bytes de datos a n3.
- n1 crea un Paquete IP. Tamaño: 1000 (Datos) + 40 (Cabecera) = 1040 bytes.
- Enlace n1 a n2 (IP MTU = 1482 bytes) -> descontamos los 18 bytes de overhead del enlace
- Enlace n2 a n3 (IP MTU = 382 bytes) -> descontamos los 18 bytes de overhead del enlace

**Primer intento de envío**

- n1 Envía: n1 mira su propio enlace, ve un MTU de 1482. Su paquete de 1040 bytes cabe perfectamente. Lo envía.
- n2 Recibe: El paquete de 1040 bytes llega a n2.
- n2 ve que el paquete que tiene (1040 bytes) es MUCHO MÁS GRANDE que 382 bytes.
- n2 Actúa:
    - Descarta el paquete de 1040 bytes.
    - Envía un nuevo paquete ICMPv6 "Packet Too Big" (Paquete Demasiado Grande) de vuelta a n1 informando el MTU del enlace (382 bytes)".

**Segundo intento de envío fragmentando**

- n1 recibe el mensaje ICMPv6 de n2.
- n1 se da cuenta de que él (el origen) debe dividir los 1000 bytes de datos en trozos más pequeños:
    - Cabecera Base: 40 bytes.
    - Cabecera de Fragmentación: IPv6 necesita una "Cabecera de Extensión" extra para fragmentar, que ocupa 8 bytes.
    - Espacio para Datos: 382 (MTU) - 40 (Cabecera Base) - 8 (Cabecera Frag.) = 334 bytes.
    - Al igual que en IPv4, el payload debe ser múltiplo de 8. El múltiplo de 8 más cercano hacia abajo de 334 es 328 bytes.
- n1 (el origen) fragmenta los 1000 bytes de datos originales en 4 nuevos paquetes:
    - Paquete 1: 40B (Cab) + 8B (Frag) + 328B (Datos) = Total 376 bytes.
    - Paquete 2: 40B (Cab) + 8B (Frag) + 328B (Datos) = Total 376 bytes.
    - Paquete 3: 40B (Cab) + 8B (Frag) + 328B (Datos) = Total 376 bytes.
    - Paquete 4 (Último): 40B (Cab) + 8B (Frag) + 16B (Datos) = Total 64 bytes.
- n1 Envía los 4 Fragmentos:
    - Pasan por n2 (porque 376 < 1482).
    - n2 los reenvía. Pasan a n3 (porque 376 < 382, y 64 < 382).
    - n3 Recibe y Reensambla: n3 recibe los 4 fragmentos y los vuelve a unir para obtener los 1000 bytes de datos originales.

Sin embargo, este proceso fallará de todos modos porque la especificación de IPv6 obliga a que cada enlace soporte un MTU mínimo de 1280 bytes.

### ¿Qué se debería cambiar para que funcione?

Para que funcione, el enlace n2 a n3 debe ser actualizado a un MTU de al menos 1298 bytes (1280 Bytes datagrama + 18 Bytes overhead link layer).