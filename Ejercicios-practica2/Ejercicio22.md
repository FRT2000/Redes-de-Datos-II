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

![Figura 4](/Recursos-practica2/Ejercicio22-figura4.png)