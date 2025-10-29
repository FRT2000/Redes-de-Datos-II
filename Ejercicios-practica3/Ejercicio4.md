# Ejercicio 4

## IPv6: Dada la topología de la figura 1 cargar en la herramienta de simulación el archivo: ipv6-base2-2023.imn

![Diagrama ejercicio 4](/Recursos-practica3/ipv6-base2-2023.png)

### Completar las direcciones (usando la primera dirección libre de la red, sin usar la “0”) y las tablas de ruteo para que exista comunicación de extremo a extremo. Por ejemplo agregar las rutas de forma manual con comandos como: n2# ip -f inet6 route add default via 2001:db8::128

#### Direcciones asignadas a cada interfaz

![Direcciones asignadas](/Recursos-practica3/ejercicio4-direcciones-asignadas.png)

#### Configuración de las rutas por default

Existen tres caminos para realizar esta configuración. Todo debe realizarse a partir de los servicios (services) presentes en la configuración de cada dispositivo.

Realizamos el ejemplo con el router n1:

- Habilitar el servicio "DefaultRoute". Si vamos a su configuración, observamos que el script de inicialización contiene la ruta configurada por defecto, solo deberíamos reemplazar el valor de la dirección que se encuentra establecida, por la que hayamos asignado en nuestra topología. Si elegimos este camino, debemos deshabilitar la opción de "StaticRoute".

![Servicio DefaultRoute](/Recursos-practica3/servicio-DefaultRoute.png)

![Script servicio DefaultRoute](/Recursos-practica3/script-servicio-DefaultRoute.png)

- Habilitar el servicio "StaticRoute". Si vamos a su configuración podemos colocar el comando `ip -f inet6 route add default via 2001:db8::129` dentro del script de inicialización. Reemplanzado la dirección IPv6 por la que hayamos configurado en la topología. Si elegimos este camino, debemos deshabilitar la opción "DefaultRoute".

![Servicio StaticRoute](/Recursos-practica3/servicio-StaticRoute.png)

![Script servicio StaticRoute](/Recursos-practica3/script-servicio-StaticRoute.png)

- Colocar el comando `ip -f inet6 route add default via 2001:db8::129` dentro de la terminal del router al iniciar la topología. Para esto debemos deshabilitar los servicios anteriores "DefaultRoute" y "StaticRoute". Luego podemos consultar la tabla de ruteo con el comando `ip -6 route`. Debemos recordar que estos cambios no se guardarán al detener la topología e iniciarla nuevamente.

![Terminal de router n2](/Recursos-practica3/servicio-StaticRoute.png)

---

### ¿Cómo quedará la tabla de ruteo del nodo n1 y del nodo n5? ¿Dónde se debe habilitar el forwarding IPv6? ¿Es necesario habilitar el de IPv4?

Consultamos las tablas de ruteo de host "n5" y router "n1" con el comando `ip -6 route`.

![Tabla de ruteo n5](/Recursos-practica3/tabla-ruteo-n5.png)

![Tabla de ruteo n1](/Recursos-practica3/tabla-ruteo-n1.png)

Para habilitar el forwarding IPv6 podemos hacerlo desde la terminal propia de cada nodo, mediante el servicio "IPForward", o configurándolo dentro del script dell servicio "StaticRoute", el cual tiene como objetivo establecer nuestras configuraciones personales.

- Si habilitamos el servicio IPForward, veremos que dentro del script, se inicializa por defecto el forwarding para IPv6.

![Script servicio IPForward](/Recursos-practica3/script-servicio-IPForward.png)

- Si lo hacemos desde el script de "StaticRoute" debemos deshabilitar el servicio "IPForward", y colocar el comando `sysctl -w net.ipv6.conf.all.forwarding=1`

![Comando forwarding dentro de StaticRoute](/Recursos-practica3/script-servicio-StaticRoute-forwarding.png)

No es necesario habilitar el de IPv4 si estamos trabajando únicamente con IPv6. Si necesitamos utilizar tanto IPv4 como IPv6 entonces si es necesario activar el forwarding para ambos, de lo contrario los routers no podrán reenviar los paquetes a través de sus interfaces de red. Podemos consultar el estado del forwarding mediante el comando `cat /proc/sys/net/ipv6/conf/all/forwarding` dentro de la terminal de cada nodo. Si obtenemos 1 (uno) está habilitado, caso contrario, si obtenemos 0 (cero) está deshabilitado.

---

### Indicar cuál será la dirección de link-local para el nodo n5. Notar que el archivo de test tiene las MAC asignadas de forma estática.

Podemos utilizar el comando `ip -6 addr show` para visualizar la dirección de link-local de cada nodo.

![Inciso c](/Recursos-practica3/ejercicio4-inciso-c.png)

En la línea `inet6 fe80::22:22ff:fe00:1/64 scope link`, observamos que la dirección de link-local es: fe80::22:22ff:fe00:1/64

### Si se realiza un ping6 desde n5 a n6, el mismo tiene éxito

Utilizamos el comando: `ping6 -c 4 2001:db8:1::4` desde la terminal de n5.

![Inciso d](/Recursos-practica3/ejercicio4-inciso-d.png)
