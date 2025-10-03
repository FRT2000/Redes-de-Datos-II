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

### Monitoree el tráfico ARP desde la PC3_SW ejecutando tcpdump -i eth0 -p arp / tshark -i eth0 arp

### Haga un ping a la PC2_SW y vuelva a observar la tabla ARP de la PC1_SW.

Luego de hacer un ping desde PC1-SW hacia PC2-SW se observa lo siguiente:

![ping de PC2-SW hacia PC2-SW](/Recursos-practica2/ping-PC1sw-PC2sw.png)

### Vea los resultados en la consola de PC3_HUB a fin de observar cuáles son las diferencias respecto a lo observado en el punto (V) en cuanto a cuáles son los paquetes que se ven en este caso.

Resultados con `tshark -i eth0 arp`. Observando el tráfico capturado en PC3-SW

![Resultados tshark](/Recursos-practica2/tshark-arp-PC3sw-VIII.png)

**Comparativa entre ambos escenarios**

- Escenario con HUB (PC3-HUB):
  - En la red conectada por un Hub, la PC que realiza la captura (PC3-HUB) ve toda la conversación ARP entre los otros dos hosts, incluyendo las tramas de Unicast (las respuestas ARP). Esto se debe a que el Hub duplica todas las tramas a todos los nodos, creando un único dominio de colisión y difusión.
- Escenario con SWITCH (PC3-SW):
  - Solicitud ARP (Broadcast): La solicitud inicial es una trama de Broadcast (dirigida a todas las MAC), por  lo que el Switch debe enviarla a todos los puertos (incluido el de PC3-SW). Por eso, el paquete se ve.
  - Respuesta ARP (Unicast): La respuesta es una trama de Unicast (dirigida específicamente a la MAC del host que preguntó). Como el Switch ya ha aprendido la ubicación de esa MAC, filtra la respuesta y la envía directamente al puerto del destinatario. La PC de captura (PC3-SW) no la ve.
  
---

## Figura 4

![Figura 4](/Recursos-practica2/Ejercicio22-figura4.png)

## Observando el gráfico anterior (fig. 4) , conteste las siguientes preguntas:

### Si PC1 envía un ARP Request para saber la dirección MAC de PC2, ¿qué dispositivos los recibirán? ¿Y a la respuesta de PC2?

- Lo recibirán todos los dispositivos pertenecientes a la misma red, ya que PC1 envía ARP Request de tipo broadcast.
- PC2 reconoce que el ARP request pregunta por su IP (172.16.2.11) y responde.
- PC2 envía ARP Reply directamente a PC1. El switch reenvía la respuesta por el puerto de PC1.

### Agregue una entrada estática como superusuario en la tabla ARP de PC1 para que pueda llegar a su router sin utilizar el protocolo. Usar el comando arp -s <IP> <MAC> / ip neigh add <IP> lladdr <MAC> dev <DEV>

En este caso debemos definir manualmente la direcciones IP y MAC del dispositivo con el cual deseamos comunicarnos. Para esto usaremos la topología del archivo "**Ejercicio22-figura4.imn**". En caso de que haya problemas al ejecutar los comandos que se encuentran a continuación, se deberá realizar la ejecución como superusuario (colocando `sudo` delante de cada comando).

Usando arp -s <IP_ROUTER_A> <MAC_ROUTER_A>

Para conocer la MAC del ROUTER A, abrimos la terminal del mismo una vez inicializada la topología y usamos el comando `ifconfig -a`. A continuación del campo "ether" veremos la MAC asociada a esa interfaz del router.

![MAC ROUTER A](/Recursos-practica2/MAC-Router-Fig4.png)

En nuestro caso particular, abriendo la terminal desde PC1 el comando será `arp -s 172.16.2.1 00:00:00:aa:00:02`. Posteriormente verificamos que la tabla ARP de PC1 se haya actualizado correctamente con las direcciones establecidas.

![tabla ARP de PC1 figura 4](/Recursos-practica2/tabla-arp-PC1-Fig4.png)

Usando ip neigh add <IP_ROUTER_A> lladdr <MAC_ROUTER_A> dev <DEV_ROUTER_A>

En nuestro caso particular, abriendo la terminal desde PC1 el comando será `ip neigh add 172.16.2.1 lladdr 00:00:00:aa:00:02 dev eth0`. Posteriormente verificamos que la tabla ARP de PC1 se haya actualizado correctamente con las direcciones establecidas.

![tabla ARP de PC1 figura 4](/Recursos-practica2/tabla-arp-PC1-Fig4-2.png)

### Si PC3 le envía un ping a PC4, ¿cuál es toda la secuencia de mensajes suponiendo que las tablas ARP están vacías? ¿Cómo estarían compuestos estos mensajes?

- PC3 mira la IP destino (165.10.4.3) y ve que está en su misma red → necesita la MAC de PC4.
- PC3 envía ARP Request (broadcast):
    - Frame Ethernet (Request):
        - MAC Destino (ETH dst) = ff:ff:ff:ff:ff:ff
        - MAC Origen (ETH src) = PC3:eth0
    - Paquete ARP (ARP Request):
        - Sender MAC = PC3:eth0
        - Sender IP = 165.10.4.2
        - Target MAC = 00:00:00:00:00:00 (desconocida)
        - Target IP = 165.10.4.3
(Switch2 reenvía a todos sus puertos; lo reciben PC4 y C:eth1.)
- PC4 responde con ARP Reply (unicast):
    - Frame Ethernet (Reply):
        - ETH dst = PC3:eth0
        - ETH src = PC4:eth0
    - Paquete ARP (ARP Reply):
        - Sender MAC = PC4:eth0
        - Sender IP = 165.10.4.3
        - Target MAC = PC3:eth0
        - Target IP = 165.10.4.2
- PC3 actualiza su ARP cache (PC4->MAC) y envía ICMP Echo Request:
    - Frame Ethernet (ICMP Request):
        - ETH src = PC3:eth0
        - ETH dst = PC4:eth0
    - IP (payload):
        - IP src = 165.10.4.2
        - IP dst = 165.10.4.3
    - PC4 responde con ICMP Echo Reply (simétrico).

### Si PC1 le envía un ping a PC4, ¿cuál sería toda la secuencia de mensajes suponiendo que las tablas ARP contienen los datos de la consulta anterior? ¿Cómo estarían compuestos estos mensajes? ¿Cambian las direcciones IP en los paquetes IP? ¿Y las direcciones MACs en las tramas Ethernet?

**Suposiciones para este inciso (según II y III):**

* `PC1` ya tiene una entrada ARP para `172.16.2.1 -> A:eth0` (estática).
* Router `C` ya tiene en su ARP cache la entrada `165.10.4.3 -> PC4:eth0` (por el intercambio PC3↔PC4 anterior).
* También suponemos que los routers A↔B y B↔C ya conocen las MACs de sus enlaces entre sí (o resolverán con ARP si no).

**Flujo extremo a extremo (sin ARP en el trayecto porque las entradas existen):**

1. **Desde PC1 hacia Router A (link 172.16.2.0/24):**

   * `PC1` encapsula el paquete IP destino `165.10.4.3` en una **trama Ethernet** con:

     * `ETH src = PC1:eth0`
     * `ETH dst = A:eth0`  *(usa la entrada ARP estática)*
   * **IP dentro del paquete (NO cambian):**

     * `IP src = 172.16.2.10` (PC1)
     * `IP dst = 165.10.4.3` (PC4)
   * El contenido IP (IP src/dst) **permanece igual** durante todo el recorrido.

2. **Router A (encolado/forwarding) → Router B (link 192.168.10.0/24):**

   * Router A desencapsula la trama L2, mira la tabla de enrutamiento y reencapsula para el siguiente salto (B).
   * **Nueva Frame Ethernet sobre el enlace A:eth1 ↔ B:eth0:**

     * `ETH src = A:eth1`
     * `ETH dst = B:eth0`
   * **IP sigue siendo:**

     * `IP src = 172.16.2.10`, `IP dst = 165.10.4.3` (no cambia).

3. **Router B → Router C (link 200.16.5.0/24):**

   * Reencapsulado en el enlace B:eth1 ↔ C:eth0:

     * `ETH src = B:eth1`
     * `ETH dst = C:eth0`
   * IPs siguen sin cambiar.

4. **Router C → PC4 (link 165.10.4.0/24):**

   * Router C mira tabla de enrutamiento: destino en 165.10.4.0/24 → interfaz `C:eth1`.
   * Router C tiene ya **ARP cache** con `165.10.4.3 -> PC4:eth0` (según supuesto), por lo que **no hace ARP** y envía directamente la trama:

     * `ETH src = C:eth1`
     * `ETH dst = PC4:eth0`
   * **IP dentro del paquete:** `src = 172.16.2.10`, `dst = 165.10.4.3`

5. **PC4** recibe la trama, procesa IP y responde con ICMP Echo Reply que vuelve por la misma ruta inversa; en cada salto las MACs de la trama L2 serán las del emisor y receptor de ese enlace concreto.

**Conclusiones sobre cambios:**

* **Direcciones IP (IP src / IP dst)** del paquete **NO cambian** de extremo a extremo: siempre `172.16.2.10 -> 165.10.4.3`. (A menos que haya NAT; aquí no la hay.)
* **Direcciones MAC (ETH src / ETH dst)** **sí cambian en cada enlace**: en cada salto la trama Ethernet usa la MAC del emisor y la MAC del siguiente salto (router o host). Ejemplo de las MACs por enlace (usando etiquetas):

  * En el enlace PC1 ↔ A: `ETH src = PC1:eth0`, `ETH dst = A:eth0`
  * En el enlace A ↔ B: `ETH src = A:eth1`, `ETH dst = B:eth0`
  * En el enlace B ↔ C: `ETH src = B:eth1`, `ETH dst = C:eth0`
  * En el enlace C ↔ PC4: `ETH src = C:eth1`, `ETH dst = PC4:eth0`

**¿Se envian ARP messages en este caso?**

* **No** para el primer salto en PC1 → A (porque PC1 tiene la entrada estática añadida).
* **No** en el último salto C → PC4 (porque C ya conoce la MAC de PC4 por la consulta PC3→PC4).
* Si alguno de los routers intermedios (A, B, C) NO tuviera la entrada ARP del vecino de enlace, en ese momento ese router haría un ARP request en la red correspondiente. En nuestro supuesto todas las entradas necesarias ya están en cache, así que **no aparecen ARP request/reply** adicionales durante este ping.