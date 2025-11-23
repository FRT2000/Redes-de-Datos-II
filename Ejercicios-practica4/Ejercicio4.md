# Ejercicio 4

## ¿Qué sucede si llega un datagrama IPv6 a un host y éste no tiene implementado IPv6?

Si un host no tiene implementada la pila de protocolos IPv6 (Capa de Red), no sabrá cómo interpretar el paquete que recibe desde la Capa de Enlace (Ethernet/Wi-Fi).
- A nivel de Enlace: La tarjeta de red recibe la trama y ve que el campo EtherType indica 0x86DD (IPv6).
- Acción: Al entregarla al Sistema Operativo, este busca un manejador para ese protocolo. Al no tenerlo, la trama se descarta silenciosamente (Silent Drop).
- Consecuencia: No se genera ningún mensaje de error (ICMPv6 ni ICMPv4) hacia el emisor, porque el host receptor ni siquiera "entiende" que eso era un paquete IP válido ni sabe cómo responderle.

## ¿Qué sucede si llega un segmento TCP a un host que no tiene soporte de este protocolo de transporte?

- A nivel de Red (IP): El datagrama IP es recibido y procesado correctamente. IP mira el campo Protocol (IPv4) o Next Header (IPv6) y ve el valor 6 (TCP).
- Acción: IP intenta entregar el contenido a la capa superior. Si el módulo TCP no existe en el kernel, IP no puede entregar la carga útil.
- Respuesta: El protocolo IP genera un mensaje de error ICMP "Destination Unreachable" con el código "Protocol Unreachable" (Protocolo inalcanzable) y lo envía de vuelta al emisor.

## ¿Qué sucede si llega un segmento TCP a un host y éste no tiene un proceso esperando en el puerto destino indicado? ¿Qué sucede si el mensaje es UDP?

**Mensaje UDP (Capa de transporte sin conexión)**
- Acción: Si el datagrama llega y el puerto destino no está abierto por ninguna aplicación, UDP simplemente descarta el datagrama.
- Respuesta: Sin embargo, para avisar al emisor, UDP le solicita a la capa de red (IP/ICMP) que envíe un mensaje de error específico: ICMP Port Unreachable (Puerto Inalcanzable).

**Segmento TCP (Capa de transporte orientada a conexión)**
- Acción: TCP no utiliza ICMP para este caso, ya que tiene sus propios mecanismos de control.
- Respuesta: Si llega un segmento (usualmente un SYN de intento de conexión) a un puerto donde no hay una aplicación escuchando (estado LISTEN), el protocolo TCP del host receptor responde inmediatamente con un segmento TCP con los flags R (Reset) y A (Ack) seteados. Esto le indica al emisor que debe cerrar o abortar el intento de conexión de inmediato (Connection Refused).