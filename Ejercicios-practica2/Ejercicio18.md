# Ejercicio 18

## Utilizando la herramienta CORE indicada por la cátedra, configurar el ruteo estático en la red que se muestra en el gráfico a continuación (fig. 2):

![Diagrama Ejercicio 18](/Recursos-practica2/1-ruteo-estatico.png)

---

### Configuración de rutas por default en los routers

#### Configuración de Router "n2"

Sin ejecutar la topología, seleccionamos el router con click derecho y elegimos la opción "services..."
Para este caso dejamos marcadas las siguientes opciones

![Configuración de servicios](/Recursos-practica2/configuracion-services.png)

Ahora abrimos las configuraciones de "StaticRoute", donde debemos colocar las direcciones que tendrá la tabla de ruteo del router seleccionado. Además de deshabilitar la opción "rp_filter" como lo indica el enunciado.

![Configuración StaticRoute](/Recursos-practica2/configuracion-static-route.png)

![Configuración de comandos StaticRoute](/Recursos-practica2/configuracion-static-route-comandos.png)

Por útimo aplicamos los cambios y guardamos la topología para que no se pierdan los cambios al salir.

---

#### Verificación de tabla de ruteo

Ejecutamos la topología y una vez iniciada (todos los dispositivos deben mostrar el color verde), hacemos doble click sobre el router "n2" para abrir la terminal perteneciente a él. También es posible abrir la terminal haciendo click derecho -> Shell window -> bash.

Colocamos el comando `route -n`. Deberá aparecernos la ruta por default con la dirección IP de router "n3"

![Verificar la ruta default](/Recursos-practica2/verificar-ruta-default.png)

---

### Verificación de conectividad entre las PCs

En este caso hacemos el ejemplo entre las PCs "n9" y "n12"

---

#### Comando PING

Abrimos la terminal de la PC "n9" y colocamos `ping <ip_destino>`.

Para nuestro caso `ping 10.0.5.22`, ya que queremos comunicarnos con la PC "n12".

![Verificar conectividad con ping](/Recursos-practica2/verificar-conectividad-ping.png)

---

#### Comando TRACEROUTE

Abrimos la terminal de la PC "n9" y colocamos `traceroute <ip_destino>`.

Para nuestro caso `traceroute 10.0.5.22`, ya que queremos comunicarnos con la PC "n12".

![Verificar conectividad con traceroute](/Recursos-practica2/verificar-conectividad-traceroute.png)

---

#### Comando PING -NR

Abrimos la terminal de la PC "n9" y colocamos `ping -nR <ip_destino>`.

Para nuestro caso `ping -nR 10.0.5.22`, ya que queremos comunicarnos con la PC "n12".

![Verificar conectividad con ping -nR](/Recursos-practica2/verificar-conectividad-ping-nR.png)

---

#### Comando TRACEROUTE -I

Abrimos la terminal de la PC "n9" y colocamos `traceroute -I <ip_destino>`.

Para nuestro caso `traceroute -I 10.0.5.22`, ya que queremos comunicarnos con la PC "n12".

![Verificar conectividad con traceroute -I](/Recursos-practica2/verificar-conectividad-traceroute-I.png)

---

#### Comando MTR
El comando `mtr <ip_destino>` daba un error pero se solucionó agregando el parámetro "-r" para visualizar la información en modo de reporte. También puede agregarse el parámetro "-c <cantidad_de_ping>" , para indicar cuántos ping queremos hacer entre cada salto al llegar a un dispositivo.

Abrimos la terminal de la PC "n9" y colocamos `mtr -r <ip_destino>`.

Para nuestro caso `mtr -r 10.0.5.22`, ya que queremos comunicarnos con la PC "n12".

Si quisiéramos agregar la cantidad de ping realizados entre cada salto como se mencionó anteriormente, el comando sería: `mtr -r -c 3 10.0.0.5.22`. Acá estamos indicando que queremos visualizar la información en modo de reporte y que además se realicen 3 ping entre cada salto.

![Verificar conectividad con mtr](/Recursos-practica2/verificar-conectividad-mtr.png)

---

### Análisis de tráfico en router intermedio

#### Captura del tráfico en Router "n2"

Primero hacemos un ping desde la PC "n9" hacia la PC "n12".

Luego desde la terminal de Router "n2" utilizamos el comando `tcpdump -i <interfaz_router>`.

En nuestro caso vamos a probar las 3 interfaces. Entonces deberíamos colocar:

- `tcpdump -i eth0`
- `tcpdump -i eth1`
- `tcpdump -i eth2`

![Análisis de tráfico eth0](/Recursos-practica2/analisis-de-trafico-eth0.png)

![Análisis de tráfico eth1](/Recursos-practica2/analisis-de-trafico-eth1.png)

![Análisis de tráfico eth2](/Recursos-practica2/analisis-de-trafico-eth2.png)

---

## Si la estación PC n7 le envía un ping a la estación PC n6:

### ¿Cuál es el camino por el que viaja el requerimiento?¿Cuál es el camino por el que viaja la respuesta?

Verificando con el comando **traceroute**, se obtienen los siguientes caminos:

- IDA: n7 → 10.0.4.1 → 10.0.2.2 → 10.0.1.2 → n6
- VUELTA: n6 → 10.0.1.2 → 10.0.2.2 → 10.0.4.1 → n7

---

## ICMP y RUTEO 1: Desde la PC n6, realice un ping a la dirección IP 5.5.5.5

### ¿Qué indica el mensaje de error recibido?, ¿Quién lo envía?

El mensaje “Time to live exceeded” indica que el paquete ICMP enviado al destino 5.5.5.5 nunca llegó, porque fue descartado en el camino al agotarse el campo TTL (Time To Live). Esto ocurre porque no existe una ruta hacia 5.5.5.5 en la tabla de ruteo, por lo que los routers reenvían el paquete de manera cíclica hasta que el TTL llega a 0 y el paquete es descartado.

El mensaje de error es enviado por el Router "n1" (10.0.0.1), que es el último router en recibir el paquete antes de descartarlo.
Cada vez que el TTL llega a 0, el router que detecta la expiración es el encargado de enviar el mensaje ICMP Type 11 (Time Exceeded) de vuelta al emisor (PC n6 en este caso).

![ICMP y Ruteo 1](/Recursos-practica2/ICMP-Y-Ruteo-1.png)

---

## ICMP y RUTEO 2: Desde la PC n6, realice un ping a la dirección IP 10.0.5.23

### ¿Qué indica el mensaje de error recibido?, ¿Quién lo envió?

El mensaje de error indica que el host de destino (10.0.5.23) es inalcanzable porque no responde en la red local, aunque la red sí es conocida. El mensaje lo envía el router 10.0.2.2, que es el gateway hacia esa red y que, tras fallar la resolución ARP, notifica al emisor.

![ICMP y Ruteo 2](/Recursos-practica2/ICMP-Y-Ruteo-2.png)

---

## ICMP y RUTEO 3: Provoque un loop de enrutamiento entre los routers con una nueva red, por ejemplo la red 200.100.11.0/24 y luego desde la PC n6, realice un ping a la dirección 200.100.11.5

### ¿Qué indica el mensaje de error recibido?, ¿Quién lo envía?


