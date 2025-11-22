# Ejercicio 2

## Indique que asumen TCP y UDP con respecto a los servicios provistos por la capa de Red/Internetworking sobre la cual se implementan. ¿Cuál es el campo del datagrama IP y los valores utilizados para diferenciarlos en la multiplexación (Hint: buscar en /etc/protocols)?

### ¿Qué asumen TCP y UDP sobre la Capa de Red?

Ambos asumen que la capa de red (IP) ofrece un servicio "Best Effort" (Mejor Esfuerzo). Esto significa que la red subyacente no es confiable:
- Los paquetes pueden perderse.
- Los paquetes pueden duplicarse.
- Los paquetes pueden llegar desordenados.

Diferencias: 
- UDP: Asume estas imperfecciones y las traslada a la aplicación. No intenta corregir los problemas de la red; si IP pierde un paquete, UDP también lo pierde. Es un protocolo "sin conexión" y no provee mecanismos de control de errores ni flujo.
- TCP: Asume que la red es hostil/no confiable, pero se compromete a ocultar estos fallos a la aplicación. Construye una abstracción de "flujo de bytes confiable y ordenado" sobre una red que no lo es, utilizando mecanismos de retransmisión, acknowledgments y ordenamiento.

### Campo del Datagrama IP y Valores de Multiplexación

Para que la capa de Red (IP) sepa a qué protocolo de transporte debe entregarle el contenido del paquete (Demultiplexación), utiliza un campo específico en su cabecera.
- Nombre del Campo:
    - En IPv4, el campo se llama Protocol.
    - En IPv6, el campo se llama Next Header.
- Valores utilizados: Según el estándar IANA:
    - TCP: Se identifica con el valor 6.
    - UDP: Se identifica con el valor 17.

El archivo texto plano **/etc/protocols** mapea los nombres de los protocolos a sus números asignados.

Podemos comprobarlo ejecutando el comando `cat /etc/protocols | grep -E 'tcp|udp'` en la terminal. La salida nos devolverá esto:

tcp     6       TCP    # transmission control protocol

udp     17      UDP    # user datagram protocol