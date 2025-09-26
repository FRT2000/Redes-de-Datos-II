# Ejercicio 15

## ¿Qué significa y cuál es el uso de la dirección 127.0.0.1?

### Significado
- Es la dirección de loopback o de retorno local.
- Forma parte de toda la red reservada 127.0.0.0/8 (127.0.0.0 – 127.255.255.255).
- En esa red, la más usada es 127.0.0.1, conocida como localhost.
- Representa al propio equipo, no sale a la red externa, todo queda en el host local.

### Uso principal
- Pruebas de conectividad local:
    - Permite verificar que la pila TCP/IP funciona en el dispositivo.
    - Ejemplo: ping 127.0.0.1. Si responde, la tarjeta de red y el protocolo IP están bien configurados en el sistema operativo, aunque no haya conexión física.

- Comunicación entre aplicaciones dentro del mismo host:
    - Una aplicación cliente y un servidor que corren en la misma máquina pueden comunicarse usando 127.0.0.1 en lugar de una dirección externa.
    - Ejemplo: un servidor web local (Apache, Nginx, Node.js) escucha en 127.0.0.1:8080.
- Aislamiento:
    - Permite que un servicio solo sea accesible localmente y no desde la red externa.