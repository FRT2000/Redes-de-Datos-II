# Ejercicio 11

## NAT Tradicional. Dado el diagrama de la figura 4.

### Escoger un bloque IPv4 público para que el router donde está ubicado el cliente pueda hacer una traducción uno a uno en la cual todos los posibles “clientes” de la red “D” puedan tener acceso simultáneo a Internet.

- Cálculo de Hosts: La "Red D" es 192.168.0.0/24. Esta red tiene 256 direcciones. Quitamos la dirección de red (.0) y la de broadcast (.255), lo que nos deja 254 direcciones de host utilizables (desde 192.168.0.1 hasta 192.168.0.254).
- Cálculo de Bloque: Para una traducción 1:1 (NAT Básico), se necesita una IP pública por cada IP privada. Por lo tanto, necesitamos 254 IPs públicas.
- Selección del Bloque: El bloque de red más pequeño que puede proveer 254 direcciones es un /24, que ofrece 256 direcciones. Para este caso elegimos la **Red Clase C** pública 192.167.0.0/24. Este bloque nos da las IPs públicas desde 192.167.0.0 hasta 190.167.0.255

---

### Seleccionar un bloque para que solo el 25 % pueda tener acceso simultáneo. ¿Cómo se resolvería para que los restantes puedan tener acceso?

- Cálculo de Hosts: Se necesita cubrir al 25% de los 254 hosts. Debemos redondear hacia arriba para cubrir la necesidad, por lo que necesitamos 64 direcciones IP.
- Cálculo de Bloque: Para obtener 64 direcciones IP utilizables, necesitamos 7 bits para hosts. Esto requiere un prefijo de /26. 
- Seleccionamos el bloque público 192.0.1.0/26. Este bloque nos da 64 IPs (desde 190.0.1.0 hasta 190.0.1.63).

El acceso para los restantes se resuelve mediante temporizadores (timers).
- El NAT Dinámico "requiere un timer por cada entrada".
- Cuando uno de los 64 hosts activos deja de enviar tráfico, su temporizador comienza a correr.
- Una vez que el temporizador de esa traducción expira (ej. llega a 0:00 ), el router elimina la entrada de la tabla.
- La dirección IP pública que usaba dicho host se libera y vuelve al pool.
- Ahora, cuando el host 65 intente conectarse de nuevo, el router encontrará esa IP libre, se la asignará y el host "restante" podrá tener acceso.

---

### Indicar cómo quedaría la tabla de NAT del router si se hace traducción solo basada en IP cuando el cliente 192.168.0.30 quiere acceder al servidor web 150.0.0.1.

Usaremos el bloque que seleccionamos en el inciso (a), es decir, 192.167.0.0/24. En un NAT Básico 1:1, lo más lógico es mapear el último octeto de la IP privada al último octeto de la IP pública.

| Red privada | Red pública |
| :--- | :--- | 
| 192.168.0.30 | 192.167.0.30 | 

---

### Indicar el posible encabezado que tendría el datagrama que entra al router desde el cliente y cómo sería el encabezado del datagrama que sale del router. ¿Qué campos cambiaron?

El cliente 192.168.0.30 envía un paquete al servidor 150.0.0.1. El router intercepta el paquete de salida y aplica la traducción de la tabla del inciso (c).

- Datagrama que **entra** al router (desde Red D):
    - IP Origen: 192.168.0.30
    - IP Destino: 150.0.0.1
- Datagrama que **sale** del router (a Internet):
    - IP Origen: 192.167.0.30 (¡Traducido!)
    - IP Destino: 150.0.0.1

Como podemos observar el campo que cambió fue la IP de Origen.

---

### Indicar el encabezado posible del paquete IP de la respuesta enviada desde el servidor y qué modificaciones necesita para que llegue al cliente.

El servidor 150.0.0.1 responde al paquete que recibió.

- Datagrama que **entra** al router (desde Internet):
    - IP Origen: 150.0.0.1
    - IP Destino: 192.167.0.30
- Datagrama que **sale** del router (a Red D):
    - IP Origen: 150.0.0.1
    - IP Destino: 192.168.0.30 (¡Traducido de vuelta!)

Como podemos observar el campo que cambió fue la IP de Destino.

---

### ¿Cómo llegaría el datagrama si el router no tuviese activada la funcionalidad de NAT, habría respuesta?

No habría respuesta.

El problema se produce por la naturaleza de las direcciones IP privadas definidas en el RFC-1918.

- Paquete de Salida (OUT):
    - Sin NAT, el router de la Red D simplemente enrutaría el paquete.
    - Este paquete saldría a Internet con la dirección IP de origen 192.168.0.30.
    - Como esta es una dirección privada RFC-1918, los "routers de borde" (como el del ISP) están configurados para filtrar y descartar estos paquetes.

- Paquete de Respuesta (IN):
    - En el caso (altamente improbable) de que el paquete de salida no fuera filtrado y llegara al servidor 150.0.0.1, el servidor intentaría responder.
    - La respuesta estaría destinada a la IP 192.168.0.30.
    - Esta dirección es "no 'enrutable' en Internet". Los routers de la red pública no tienen una ruta para llegar a una dirección privada, por lo que la respuesta sería descartada.

En ambos escenarios la comunicación falla.

### ¿Qué mecanismo sería necesario si no se contase con el bloque IPv4 público y solo se tuviese una única IP pública en el router?

El mecanismo necesario es NAPT (Network Address Port Translation), específicamente la variante conocida como "overloading/masquerading".