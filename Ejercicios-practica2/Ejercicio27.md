# Ejercicio 27

## Dado el siguiente diagrama (fig. 5), ¿qué direcciones IPv6 será capaz de auto-configurar el nodo A en cada una de sus interfaces? ¿Cuáles son recomendadas y cuáles sus alcances?

![Diagrama Ejercicio 27](/Recursos-practica2/Ejercicio27-Diagrama.png)

---

## 1. Direcciones Autoconfiguradas (SLAAC)

El NODO-A utilizará el mecanismo de **SLAAC (Stateless Address Autoconfiguration)** para crear dos tipos de direcciones en cada interfaz, combinando el **Prefijo de Red** (proporcionado por el *Router-Adv*) con el **Identificador de Interfaz (Interface ID)**.

El Identificador de Interfaz se genera a partir de la dirección MAC de la interfaz utilizando el método **EUI-64**.

### Paso 1: Generación del Identificador EUI-64

El NODO-A tomará las direcciones MAC de sus interfaces, invertirá el séptimo bit del primer octeto (de $0$ a $1$) e insertará `ff:fe` en medio:

| Interfaz | Dirección MAC | MAC Modificada (EUI-64) |
| :--- | :--- | :--- |
| **`eth0`** | `00:1b:77:b1:49:a1` | `02:1b:77:ff:fe:b1:49:a1` |
| **`eth1`** | `c0:25:ee:ba:93:e1` | `c2:25:ee:ff:fe:ba:93:e1` |

*(El bit invertido transforma `00` en `02` y `c0` en `c2`)*

### Paso 2: Autoconfiguración de Direcciones Globales Únicas

El NODO-A combinará el prefijo de red (`/64`) anunciado por cada router con su EUI-64 para generar su dirección global autoconfigurada:

| Interfaz | Prefijo de Red (Router) | Dirección IPv6 Autoconfigurada |
| :--- | :--- | :--- |
| **`eth0`** | `3ffe:8070:1011:100::/64` | **`3ffe:8070:1011:100:021b:77ff:feb1:49a1`** |
| **`eth1`** | `2818:4fde:5100:0::/64` | **`2818:4fde:5100:0:c225:eeff:feba:93e1`** |

---

## 2. Direcciones de Enlace Local (Link-Local)

Una dirección de Enlace Local es **obligatoria** para cualquier interfaz IPv6 activa, independientemente de la autoconfiguración global. Se utiliza para la comunicación dentro del mismo segmento de red (LAN).

### Autoconfiguración de Direcciones Link-Local

El NODO-A utilizará el prefijo de enlace local (`fe80::/64`) junto con el mismo Identificador EUI-64:

| Interfaz | Prefijo Link-Local | Dirección IPv6 de Enlace Local (Obligatoria) |
| :--- | :--- | :--- |
| **`eth0`** | `fe80::/64` | **`fe80::021b:77ff:feb1:49a1`** |
| **`eth1`** | `fe80::/64` | **`fe80::c225:eeff:feba:93e1`** |

---

## 3. Recomendaciones y Alcances

| Tipo de Dirección | Recomendación | Alcance (Scope) |
| :--- | :--- | :--- |
| **Dirección Global Única** (Ej: `3ffe:8070...`) | **Recomendada para comunicación fuera de la red local.** Permite al NODO-A acceder a internet o a otras redes externas (siempre que los routers Adv lo permitan). | **Global.** Es ruteable por routers en toda la red, similar a una dirección IPv4 pública. |
| **Dirección Link-Local** (Ej: `fe80::...`) | **Obligatoria para la funcionalidad básica de IPv6.** Es crucial para protocolos como ARP (Neighbor Discovery Protocol), SLAAC y para que el nodo se comunique con su router (*gateway*). | **Enlace Local (Link-Local).** No es ruteable por routers. Solo es válida y utilizable para la comunicación dentro del mismo segmento físico de red donde se encuentra la interfaz. |
| **Identificador EUI-64** | **No es la recomendación moderna.** EUI-64 revela la dirección MAC física del dispositivo en la dirección IPv6 global, lo que puede plantear problemas de privacidad y seguimiento. | No aplica, es un componente de la dirección. |
| **Dirección "Privada" Temporal** | **Recomendada para privacidad.** En sistemas operativos modernos, el NODO-A generaría direcciones globales aleatorias y temporales que cambian con el tiempo para evitar el seguimiento (en lugar de usar EUI-64). | **Global.** Ruteable fuera de la red local. |