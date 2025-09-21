# Ejercicio 3

## ¿Qué es una red clase A? ¿Qué es una red clase B? ¿Qué es una red clase C? ¿Cuántas hay de cada una? ¿Cuántos hosts pueden haber en cada una? 
El rango de direcciones IP se divide en 5 clases: 

- Clase A.
- Clase B.
- Clase C.
- Clase D.
- Clase E.

Las primeras 3 (**A, B y C**) son utilizadas para direcciones **Unicast**, donde la transmisión se realiza desde un único emisor hacia un único receptor. 
La **Clase D** se utiliza para direcciones **Multicast**, donde la transmisión se realiza desde un único emisor hacia un grupo de receptores.
La **Clase E** se encuentra **Reservada** para pruebas futuras. Esta red no puede ser utilizada.

A continuación, se muestran las características principales de las clases A, B y C:

| **Clase** | **Rango de direcciones utilizables**            | **Bits iniciales** | **Máscara por defecto**   | **Cantidad de redes** | **Hosts por red**            |
| ----- | ------------------------------- | -------------- | --------------------- | ----------------- | ------------------------ |
| **A**     | `1.0.0.0` – `126.255.255.255`       | `0xxxxxxx`   | `255.0.0.0` (/8)      | $2^{7}$ = **126**   | $2^{24}$ – 2 = **16,777,214** |
| **B**     | `128.0.0.0` – `191.255.255.255`     | `10xxxxxx`   | `255.255.0.0` (/16)   | $2^{14}$ = **16,384** | $2^{16}$ – 2 = **65,534**     |
| **C**     | `192.0.0.0` – `223.255.255.255`     | `110xxxxx`   | `255.255.255.0` (/24) | $2^{21}$ = **2,097,152** | $2^{8}$ – 2 = **254**         |

---

## ¿Existen clases en IPv6?
No. El direccionamiento IPv6 nunca utilizó el modelo de clases. Desde el inicio se diseñó con CIDR (Classless Inter-Domain Routing), es decir, con prefijos de longitud variable.

---

## ¿Qué significa que el actual direccionamiento sea classless?
Significa que ya no usamos las clases rígidas de IPv4 (A, B, C), sino que ahora las redes se definen con máscaras de longitud variable (CIDR).

Antes:

- Clase A → siempre /8
- Clase B → siempre /16
- Clase C → siempre /24

Ahora (classless):

- Podemos tener cualquier tamaño de red según lo necesitemos: /8, /12, /20, /28, etc.
- Ejemplo: 192.168.1.0/27 → red con 32 direcciones (30 hosts útiles).