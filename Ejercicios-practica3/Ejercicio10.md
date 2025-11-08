# Ejercicio 10

## NAT/NATP: ¿Qué especifica el documento de la IETF RFC-1918 y cómo se relaciona con NAT/NATP?

### Especificación de la IETF RFC-1918
El documento RFC-1918 es un estándar de la IETF (Internet Engineering Task Force) que define los bloques de direcciones IPv4 reservados para ser utilizados en redes privadas.

Las direcciones pertenecientes a estos bloques no son enrutables en la Internet pública. Los routers de borde de los Proveedores de Servicios de Internet (ISP) están configurados, por política, para descartar cualquier paquete que ingrese desde Internet con una de estas direcciones como origen o destino.

### Relación con NAT/NATP
NAT (Traducción de Direcciones de Red) Es un proceso, implementado en el router de borde o gateway de una red privada, que reescribe las cabeceras de los paquetes IP.
- Traducción de Salida: Cuando un host privado (ej. 192.168.0.30) envía un paquete a un servidor público, el router intercepta el paquete. Reescribe la dirección IP de origen, reemplazando la IP privada (192.168.0.30) por la IP pública del router (ej. 200.3.4.2).
- Tabla de Estado: El router registra esta traducción en una tabla de estado interna.
- Traducción de Entrada: Cuando el servidor público responde, envía el paquete de vuelta a la IP pública del router. El router consulta su tabla de estado, identifica a qué conexión interna corresponde la respuesta y reescribe la dirección IP de destino, reemplazando su propia IP pública por la IP privada del host original (192.168.0.30).

NATP (Traducción de Direcciones y Puertos) NATP, comúnmente conocido como PAT (Port Address Translation) o NAT Overload, es la implementación más utilizada de NAT. Este mecanismo permite que múltiples dispositivos de la red privada compartan una única dirección IP pública.

NATP logra esto traduciendo no solo la dirección IP, sino también el número de puerto (TCP/UDP) de origen. Al asignar un puerto de origen único (de su propiedad) a cada conexión saliente, el router puede diferenciar las múltiples conexiones simultáneas y saber exactamente a qué host interno debe entregar cada paquete de respuesta.

