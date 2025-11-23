# Ejercicio 7

## Dada la siguiente salida del comando (netstat o ss), responder:

## ¿Cuántas conexiones TCP hay establecidas?

- 10.168.1.163:51222 ... ESTABLISHED
- 127.0.0.1:43695 ... ESTABLISHED
- 127.0.0.1:8000 ... ESTABLISHED
- 127.0.0.1:35250 ... ESTABLISHED
- 10.168.1.163:36121 ... ESTABLISHED
- 10.168.1.163:60123 ... ESTABLISHED
- 10.168.1.163:42133 ... ESTABLISHED
- 10.168.1.163:50121 ... ESTABLISHED
- 127.0.0.1:45547 ... ESTABLISHED

Hay 9 conexiones TCP establecidas

## ¿Cuántas conexiones TCP hay establecidas solo como cliente y cuántas como servidor?

**Como Servidor (2 conexiones):**
- 127.0.0.1:43695 (Local): Vemos en la primera línea que el puerto 43695 está en LISTEN. Por tanto, esta conexión aceptó una solicitud.
- 127.0.0.1:8000 (Local): Vemos en la sexta línea que el puerto 8000 está en LISTEN.

**Como Cliente (7 conexiones):**
- Las 5 conexiones externas desde la IP 10.168.1.163 (puertos efímeros 51222, 36121, 60123, 42133, 50121) hacia puertos remotos (443, 7).
- La conexión local desde 127.0.0.1:35250 hacia el puerto 8000.
- La conexión local desde 127.0.0.1:45547 hacia el puerto 43695.

Respuesta: Hay 7 conexiones como Cliente y 2 conexiones como Servidor.

## ¿Cuántas conexiones TCP están aún pendientes por establecerse?

Debemos buscar estados que indiquen un intento de conexión incompleto (SYN_SENT o SYN_RECV).

Observando la línea: tcp ... 10.168.1.163:45123 ... 1.1.1.1:9000 ... SYN_SENT

Hay 1 conexión pendiente (se está intentando conectar con la IP 1.1.1.1 al puerto 9000).

## ¿A qué servicios bien conocidos (puertos 0 a 1023) tiene el host conexiones TCP establecidas?

Debemos observar las líneas **ESTABLISHED** donde actuamos como Cliente (Foreign Address es remota):
- ...:51222 -> 173.194.42.54:443 (HTTPS)
- ...:36121 -> 138.160.162.116:7 (Echo Protocol)
- ...:60123 -> 91.189.89.76:443 (HTTPS)
- ...:42133 -> 173.194.42.33:443 (HTTPS)
- ...:50121 -> 199.16.156.83:443 (HTTPS)

Tiene conexiones establecidas con servicios HTTPS (443) y Echo (7).

## ¿Qué servicios bien conocidos (TCP y UDP) tiene corriendo el host (esperando por recibir información)? (Ver RFC1700)

Observamos los puertos locales en estado LISTEN (TCP) o abiertos (UDP) que estén en el rango 0-1023.

**TCP (LISTEN):**
- 22 (SSH): Visible en 0.0.0.0:22 y :::22.
- 80 (HTTP): Visible en :::80.
- 631 (IPP/Impresión): Visible en 127.0.0.1:631 y ::1:631.

**UDP (Sin estado, solo el puerto):**
- 68 (DHCP Client / Bootpc): Visible en 0.0.0.0:68.
- 69 (TFTP): Visible en 0.0.0.0:69.

El host corre servicios SSH (22), HTTP (80), IPP (631), DHCP (68) y TFTP (69).

## ¿Cuántas conexiones están en proceso de cierre?

Buscamos estados de finalización (TIME_WAIT, CLOSE_WAIT, LAST_ACK, FIN_WAIT): 
- ...:50120 -> CLOSE_WAIT
- ...:40123 -> TIME_WAIT
- ...:58432 -> LAST_ACK
- ...:58433 -> CLOSE_WAIT

Hay 4 conexiones en proceso de cierre.

## ¿Cuáles conexiones TCP tuvieron el cierre iniciado por el host local y cuáles por el remoto?

- Active Close (Yo corté primero): Termino en estado TIME_WAIT (esperando 2MSL por si acaso).
- Passive Close (Ellos cortaron primero): Yo recibo su FIN, paso a CLOSE_WAIT, envío mi FIN y paso a LAST_ACK.

**En nuestro caso:**
- Iniciado por Local (Yo): La conexión con el puerto local 40123 (Estado TIME_WAIT).
- Iniciado por Remoto (Ellos): Las conexiones con puertos locales 50120, 58432 y 58433 (Estados CLOSE_WAIT y LAST_ACK).

## ¿En qué puertos podría recibir datos sobre IPv6 desde otros hosts, tanto TCP6 como UDP6?

Miramos los protocolos tcp6 y udp6.

**TCP6:**
- :::80 (HTTP)
- :::22 (SSH)
- (Descartamos ::1:631 porque es local)

**UDP6:**
- :::59695
- :::5353 (mDNS)

Podría recibir datos IPv6 externos en los puertos TCP 80 y 22, y en los puertos UDP 59695 y 5353.