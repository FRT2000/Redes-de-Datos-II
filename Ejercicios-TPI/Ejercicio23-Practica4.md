# Ejercicio 23 de la Práctica 4

## Programar en el lenguaje de su elección mediante la API socket un servidor TCP que escuche conexiones en el puerto 9000 y que los datos que reciba los descarte. Correr en el nodo n9 y enviar datos desde otro nodo usando la herramienta nc (netcat) o telnet.




b) En el nodo n9 levantar con el super daemon inetd algunos servicios extras, como tcp echo,
discard y otros. Chequear los servicios TCP y UDP activos.
c) Desde el nodo n13 realizar una conexión TCP y enviar datos mediante un programa cliente
de su elección al servicio discard, y al echo. Capturar el tráfico con la herramienta tcpdump o
wireshark y analizar la cantidad de segmentos, los flags utilizados y las opciones extras que
llevan los encabezados tcp.
d) Sin cerrar las conexiones chequear los servicios activos y ver los Estados.
e ) Generar nuevas conexiones hacia el nodo n9 e inspeccionar los estados. Por ejemplo
realizar varias conexiones simultáneas al servicio tcp echo desde el mismo origen y desde
otros nodos.
f) Intentar generar conexiones a un puerto donde no existe un proceso esperando por recibir
datos. ¿Cómo notifica TCP de este hecho (ver flags)?
g ) Cerrar las conexiones y ver el estado de los servicios en ambos lados. ¿En qué estado
queda el que hace el cierre activo?
h) Observando la captura indicar la cantidad de segmentos y los flags utilizados. ¿Con cuántos
segmentos se cerró la conexión? ¿Existen otras variantes de cierre?
i) Hacer un diagrama de los segmentos intercambiados con los números de secuencia
absolutos para una de las sesiones TCP (Se puede usar la herramienta wireshark u otra).
j ) Alternativo: Realizar una conexión mediante nc indicando un puerto específico para el
cliente. Luego cerrar la conexión desde el cliente e intentar abrirla nuevamente. ¿En qué
estado está el socket? Investigar valor del 2MSL en la plataforma sobre la cual está
haciendo los tests.