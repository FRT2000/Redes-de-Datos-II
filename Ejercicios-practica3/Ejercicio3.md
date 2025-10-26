# Ejercicio 3

## Resolver los ejercicios 1a) con la red IPv6: 2001:db8:1111::/48 y 1b) con la red 2001:db8:1111:2200::/56.

### Con IPv6: 2001:db8:1111::/48

En la mayoría de las aplicaciones es recomendable utilizar el prefijo /64 dentro de IPv6, donde reservamos 64 bits para la red y 64 bits para los hosts.

El espacio de direcciones por cada red es más que suficiente para la cantidad que nos solicita el ejercicio. Entonces podemos asignar las redes de la siguiente manera:

#### Red de 80 hosts.

|**2001:0db8:1111**|:0000:0000:0000:0000:0000/64 -> Bits para dirección de red

2001:0db8:1111:|**0000**|:0000:0000:0000:0000/64 -> Bits para dirección de subred

2001:0db8:1111:0001:0000:0000:0000:0000/64 -> |**Dirección asignada a la red de 80 hosts**|

---

#### Redes de 10 hosts.

2001:0db8:1111:0002:0000:0000:0000:0000/64 -> |**Dirección asignada a la red número 1 de 10 hosts**|

2001:0db8:1111:0003:0000:0000:0000:0000/64 -> |**Dirección asignada a la red número 2 de 10 hosts**|

---

#### Red de 40 hosts.

2001:0db8:1111:0004:0000:0000:0000:0000/64 -> |**Dirección asignada a la red de 40 hosts**|

---

### Con IPv6: 2001:db8:1111:2200::/56

#### Redes de 2000 hosts.

|**2001:0db8:1111:22**|00:0000:0000:0000:0000/64 -> Bits para dirección de red

2001:0db8:1111:22|**00**|:0000:0000:0000:0000/64 -> Bits para dirección de subred

2001:0db8:1111:2201:0000:0000:0000:0000/64 -> |**Dirección asignada a la red número 1 de 2000 hosts**|

2001:0db8:1111:2202:0000:0000:0000:0000/64 -> |**Dirección asignada a la red número 2 de 2000 hosts**|

---

#### Redes de 500 hosts.

2001:0db8:1111:2203:0000:0000:0000:0000/64 -> |**Dirección asignada a la red número 1 de 500 hosts**|

2001:0db8:1111:2204:0000:0000:0000:0000/64 -> |**Dirección asignada a la red número 2 de 500 hosts**|

---

#### Redes de 300 hosts.

2001:0db8:1111:2205:0000:0000:0000:0000/64 -> |**Dirección asignada a la red número 1 de 300 hosts**|

2001:0db8:1111:2206:0000:0000:0000:0000/64 -> |**Dirección asignada a la red número 2 de 300 hosts**|

2001:0db8:1111:2207:0000:0000:0000:0000/64 -> |**Dirección asignada a la red número 3 de 300 hosts**|

2001:0db8:1111:2208:0000:0000:0000:0000/64 -> |**Dirección asignada a la red número 4 de 300 hosts**|

2001:0db8:1111:2209:0000:0000:0000:0000/64 -> |**Dirección asignada a la red número 5 de 300 hosts**|

2001:0db8:1111:220A:0000:0000:0000:0000/64 -> |**Dirección asignada a la red número 6 de 300 hosts**|

2001:0db8:1111:220B:0000:0000:0000:0000/64 -> |**Dirección asignada a la red número 7 de 300 hosts**|

2001:0db8:1111:220C:0000:0000:0000:0000/64 -> |**Dirección asignada a la red número 8 de 300 hosts**|

2001:0db8:1111:220D:0000:0000:0000:0000/64 -> |**Dirección asignada a la red número 9 de 300 hosts**|

2001:0db8:1111:220E:0000:0000:0000:0000/64 -> |**Dirección asignada a la red número 10 de 300 hosts**|

2001:0db8:1111:220F:0000:0000:0000:0000/64 -> |**Dirección asignada a la red número 11 de 300 hosts**|

2001:0db8:1111:2210:0000:0000:0000:0000/64 -> |**Dirección asignada a la red número 12 de 300 hosts**|

2001:0db8:1111:2211:0000:0000:0000:0000/64 -> |**Dirección asignada a la red número 13 de 300 hosts**|

2001:0db8:1111:2212:0000:0000:0000:0000/64 -> |**Dirección asignada a la red número 14 de 300 hosts**|

2001:0db8:1111:2213:0000:0000:0000:0000/64 -> |**Dirección asignada a la red número 15 de 300 hosts**|

2001:0db8:1111:2214:0000:0000:0000:0000/64 -> |**Dirección asignada a la red número 16 de 300 hosts**|

2001:0db8:1111:2215:0000:0000:0000:0000/64 -> |**Dirección asignada a la red número 17 de 300 hosts**|

2001:0db8:1111:2216:0000:0000:0000:0000/64 -> |**Dirección asignada a la red número 18 de 300 hosts**|

2001:0db8:1111:2217:0000:0000:0000:0000/64 -> |**Dirección asignada a la red número 19 de 300 hosts**|

2001:0db8:1111:2218:0000:0000:0000:0000/64 -> |**Dirección asignada a la red número 20 de 300 hosts**|

---

#### Redes de 200 hosts.

2001:0db8:1111:2219:0000:0000:0000:0000/64 -> |**Dirección asignada a la red número 1 de 200 hosts**|

2001:0db8:1111:221A:0000:0000:0000:0000/64 -> |**Dirección asignada a la red número 2 de 200 hosts**|

2001:0db8:1111:221B:0000:0000:0000:0000/64 -> |**Dirección asignada a la red número 3 de 200 hosts**|

...

2001:0db8:1111:224A:0000:0000:0000:0000/64 -> |**Dirección asignada a la red número 50 de 200 hosts**|

---

#### Red de blackbone.

2001:0db8:1111:224B:0000:0000:0000:0000/64 -> |**Dirección asignada a la red de backbone**|