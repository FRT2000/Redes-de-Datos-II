# Ejercicio 9

## De acuerdo a la siguiente salida del comando netstat responder:

## ¿Cuál es el proceso asignado al port de servicios de impresión de red? (Hint: buscar en /etc/services).

Línea 2: 127.0.0.1:631 ... 11351/cupsd

Línea 7: ::1:631 ... 11351/cupsd

El proceso es cupsd (Common Unix Printing System daemon), con el PID 11351.

## ¿Se podría enviar a imprimir al servidor de impresión de este equipo a través de la red desde otros equipos?

No se puede imprimir desde otros equipos. El servicio cupsd está configurado para escuchar únicamente en la interfaz de Loopback (Localhost: 127.0.0.1 y ::1). Esto significa que solo acepta trabajos de impresión generados desde la misma máquina. Para que fuera accesible desde la red, debería estar escuchando en 0.0.0.0:631 o en la IP de la red 13.10.0.14:631.

## ¿Qué servicios pueden recibir conexiones sobre IPv6?

Línea 5: tcp6 :::80 -> Proceso apache2 (Servidor Web).

Al estar en :::, acepta conexiones IPv6 desde cualquier host.

Línea 6: tcp6 :::22 -> Proceso sshd (Secure Shell).

Al estar en :::, acepta conexiones IPv6 desde cualquier host.

Línea 7: tcp6 ::1:631 -> Proceso cupsd (Impresión).

Solo acepta conexiones IPv6 locales (::1).