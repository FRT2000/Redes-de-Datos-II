# Ejercicio 22

##  22. Utilizando el CORE, arme la siguiente topología (fig. 3):

![Diagrama ejercicio 22](/Recursos-practica2/Ejercicio22-Diagrama.png)

---

## Si una PC se desea conectar a otra PC en una red distinta, ¿es necesario ejecutar ARP? ¿A quién le envió el ARP Request?
- Sí, se necesita ARP.
- El ARP Request lo envía la PC al gateway/router para obtener su dirección MAC y poder enviarle la trama.

---

## Suponga que PC1_hub, que tiene la tabla ARP vacía, le quiere enviar un ping a PC2_hub. ¿Cuál es la secuencia de mensajes? Indique los mensajes ARP Request y Reply completando los campos de la trama Ethernet y de los mensaje ARP.

Primero PC1-HUB identificará si PC2-HUB se encuentra dentro de la misma red a partir de la dirección IP de dicho destinatario.

Luego de identificar que efectivamente se encuentra en la misma red, PC1-HUB enviará ARP Request de tipo broadcast preguntando por la MAC del dispositivo que tenga la dirección IP 10.0.0.21.

![ARP Request PC1-HUB a PC2-HUB](/Recursos-practica2/ARP-Request-PC1hub-PC2hub.png)

PC2-HUB identifica que el mensaje es para él y responde con ARP Reply colocando su dirección MAC. Esta respuesta solamente es enviada a PC1-HUB.

![ARP Reply PC2-HUB a PC1-HUB](/Recursos-practica2/ARP-Reply-PC2hub-PC1hub.png)

Finalmente, luego de recibir la respuesta, PC1-HUB actualiza su tabla ARP y envía el ICMP Echo Request dentro de una trama ethernet hacia la MAC de PC2-HUB.

![ICMP Echo Request de PC1-HUB a PC2-HUB](/Recursos-practica2/ICMP-Echo-Request-PC1hub-PC2hub.png)

---

## ¿Cómo quedarían los mensajes ARP si el ping ahora es desde PC1_hub hacia PC2_SW? (Suponer que las tablas ARP están vacías)

Primero PC1-HUB identificará si PC2-SW se encuentra dentro de la misma red a partir de la dirección IP de dicho destinatario. En este caso se encuentran en redes diferentes.

Luego de identificar que efectivamente se encuentra en una red diferente, PC1-HUB enviará ARP Request de tipo broadcast preguntando por la MAC del ROUTER perteneciente a su red. Para esto preguntará qué dispositivo tiene la dirección IP 10.0.0.1.

![ARP Request PC1-HUB a ROUTER](/Recursos-practica2/ARP-Request-PC1hub-ROUTER.png)

ROUTER identifica que el mensaje es para él y responde con ARP Reply colocando su dirección MAC. Esta respuesta solamente es enviada a PC1-HUB.

![ARP Reply ROUTER a PC1-HUB](/Recursos-practica2/ARP-Reply-ROUTER-PC1hub.png)

Finalmente, luego de recibir la respuesta, PC1-HUB actualiza su tabla ARP y envía el ICMP Echo Request dentro de una trama ethernet hacia la MAC de ROUTER.

![ICMP Echo Request de PC1-HUB a PC2-SW](/Recursos-practica2/ICMP-Echo-Request-PC1hub-PC2sw.png)

---

## Para analizar los paquetes del protocolo ARP realice las siguientes tareas:

Para realizar todas las tareas a continuación, debemos iniciar la topología del archivo correspondiente (Ejercicio22-Diagrama.imn).

### Ejecute el comando ifconfig -a o ip addr show en la PC1_hub

Usando `ifconfig -a`.

![ifconfig -a con PC1-HUB](/Recursos-practica2/ifconfig-a-PC1hub.png)

Usando `ip addr show`.

![ip addr show con PC1-HUB](/Recursos-practica2/ip-addr-show-PC1hub.png)

### Luego ejecute el comando arp -n o ip -4 neigh show en la PC1_hub para ver su tabla ARP.

Al ejecutar `arp -n` o `ip -4 neigh show` se observa la tabla ARP de PC1-HUB vacía.

![tabla ARP de PC1-HUB](/Recursos-practica2/tabla-arp-vacia-PC1hub.png)

### Monitoree el tráfico ARP desde la PC3_hub ejecutando tcpdump -i eth0 -p arp / tshark -i eth0 arp

Usando `tcpdump -i eth0 -p arp`.

![tcpdump para capturar tráfico ARP](/Recursos-practica2/tcpdump-arp-PC3hub-III.png)

Usando `tshark -i eth0 arp`. Para que este comando funcione correctamente, debemos instalar previamente los paquetes de tshark como usuario root mediante el comando `sudo apt install tshark`.

![tshark para capturar tráfico ARP](/Recursos-practica2/tshark-arp-PC3hub-III.png)

### Envíe un ping desde la PC1_hub a PC2_hub y vuelva a observar la tabla ARP de PC1_hub.

Luego de hacer un ping desde PC1-HUB hacia PC2-HUB se observa lo siguiente:

![ping de PC1-HUB hacia PC2-HUB](/Recursos-practica2/ping-PC1hub-PC2hub.png)

### Vea los resultados en la consola de PC3 a fin de observar las características de los paquetes ARP (MAC Origen, MAC Destino, etc).

Resultados con `tcpdump -i eth0 -p arp`

![Resultados tcpdump](/Recursos-practica2/tcpdump-arp-PC3hub-v.png)

Resultados con `tshark -i eth0 arp`

![Resultados tshark](/Recursos-practica2/tshark-arp-PC3hub-v.png)

### Monitoree el tráfico ARP desde la PC3_SW(asumo que quiere decir PC3_HUB) ejecutando tcpdump -i eth0 -p arp / tshark -i eth0 arp

### Haga un ping a la PC2_SW y vuelva a observar la tabla ARP de la PC1_SW (pienso que quisieron decir PC1_HUB si no sería igual).

Luego de hacer un ping desde PC1-HUB hacia PC2-SW se observa lo siguiente:

![ping de PC1-HUB hacia PC2-HUB](/Recursos-practica2/ping-PC1hub-PC2sw.png)

### Vea los resultados en la consola de PC3_HUB a fin de observar cuáles son las diferencias respecto a lo observado en el punto (V) en cuanto a cuáles son los paquetes que se ven en este caso.

Resultados con `tcpdump -i eth0 -p arp`

![Resultados tcpdump](/Recursos-practica2/tcpdump-arp-PC3hub-VIII.png)

Resultados con `tshark -i eth0 arp`

![Resultados tshark](/Recursos-practica2/tshark-arp-PC3hub-VIII.png)

---

![Figura 4](/Recursos-practica2/Ejercicio22-figura4.png)