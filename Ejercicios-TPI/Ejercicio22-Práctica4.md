# Ejercicio 22 de la Práctica 4

## Levantar un servicio UDP con la herramienta nc (netcat) en el host n9 y enviar información desde n13 usando el mismo comando. Ver el estado de los sockets en ambos extremos. ¿Qué significa el estado ESTABLISHED en UDP?

Partimos de la topología armada en el ejercicio 12 de la práctica 3

![Topología de la Figura 6](/Recursos-TPI/Ejercicio12-Practica3-HostsIPv4-Asignados.png)

Se inicia la topología y se ejecutan los siguientes comandos

### Host n9
- `nc -u -l 8000`
    - u: UDP
    - l: Listen (escuchar)

### Host n13
- `nc -u <IP_de_n9> 8000`

Abrimos otra terminal dentro de este host para verificar la conectividad (Esto puede hacerse en una terminal nueva de cualquiera de los host involucrados)

Ejecutamos:
- `netstat -an | grep udp`

![Conectividad UDP](/Recursos-TPI/Ejercicio22-Practica4-udp-incisoA.png)

Se observa que la conexión se ha establecido correctamente

###  ¿Qué significa el estado ESTABLISHED en UDP?

En UDP, el estado ESTABLISHED es un estado lógico local del sistema operativo y no del protocolo de red. Significa que el socket ha sido configurado para enviar y recibir datos únicamente desde una dirección remota específica, aunque no exista una sesión real ni intercambio de paquetes de negociación (handshake) en la red.

---

## Levantar en el super daemon inetd o similar con el servicio UDP echo y probar con un cliente programado en el lenguaje de su elección mediante la API socket contra este servicio. Inspeccionar el estado. Ver de generar datos hacia el “servidor” desde más de un Nodo.

Se intaló "inetd" dentro de una terminal de linux fuera de la herramiena CORE usando:

`sudo apt install openbsd-inetd`

Posteriormente dentro de cada hosts se realizaron las siguientes configuraciones:

### Host n9
- `vim /etc/inetd.conf` -> Verificamos el archivo
    - `echo   dgram   udp     wait    root    internal` -> nos aseguramos que esta línea esté descomentada (sin "#" al inicio)
- `/etc/init.d/openbsd-inetd restart` -> iniciar el servicio
- `netstat -anu | grep :7` -> verificamos que está funcionando

### Host n11 y n13
Se realizó el script de python "**cliente_udp.py**"

- `python3 <ubicación del script>/cliente_udp.py` -> ejecutamos en una terminal de cada host

Al visualizar el mensaje:

![Mensaje UDP](/Recursos-TPI/Ejercicio22-Practica4-udp-incisoB.png)

Significa que todo se realizó correctamente

c) Enviar información desde n13 a n9 a un port UDP donde no existe un proceso esperando por
recibir datos. ¿Cómo notifica el stack TCP/IP de este hecho? Investigue la herramienta
traceroute que ports utiliza y cómo usa estos mensajes (Ver ejercicio de IP con ruteo
estático).
d ) Para las pruebas anteriores capturar tráfico y ver el formato de los datagramas UDP y como
se encapsulan en IP