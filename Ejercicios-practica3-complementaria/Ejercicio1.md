# Ejercicio 1

## Aplicando VLSM/CIDR, resolver los siguientes escenarios:

## Dada la red IP 165.10.0.0/22 se necesitan definir:
- 4 (cuatro) redes de 120 hosts 
- 8 (ocho) redes de 12 hosts. 
- 4 (cuatro) redes de 44 hosts.

#### Redes de 120 hosts

Para las redes que necesitan 120 hosts: $2^{7}$ - 2 = 126 hosts.

165.10.0.0/22 -> red original

1010 0101.0000 1010.0000 0000.0|**000 0000**| -> bits tomados para los 120 hosts.

|**1010 0101.0000 1010.0000 00**|00.0000 0000 -> bits de red original

1010 0101.0000 1010.0000 00|**00.0**|000 0000 -> bits tomados para subred

1010 0101.0000 1010.0000 00|**11.1**|000 0000 -> bits tomados para subred colocados en 1

- 165.10.3.128/25 -> **dirección IP asignada para la red número 1 de 120 hosts.**
- 165.10.3.0/25 -> **dirección IP asignada para la red número 2 de 120 hosts.**
- 165.10.2.128/25 -> **dirección IP asignada para la red número 3 de 120 hosts.**
- 165.10.2.0/25 -> **dirección IP asignada para la red número 4 de 120 hosts.**

Finalmente las direcciones: `165.10.0.0` hasta `165.10.1.255` quedan libres para seguir subneteando.

---

#### Redes de 44 hosts

Para las redes que necesitan 44 hosts: $2^{6}$ - 2 = 62 hosts.

165.10.1.255 -> red de la cual partimos

1010 0101.0000 1010.0000 0001.1111 1111 -> red expresada en bits

1010 0101.0000 1010.0000 0001.11|**00 0000**| -> bits tomados para los 44 hosts.

|**1010 0101.0000 1010.0000 00**|01.1100 0000 -> bits de red original

1010 0101.0000 1010.0000 00|**01.11**|00 0000 -> bits tomados para subred

- 165.10.1.192/26 -> **dirección IP asignada para la red número 1 de 44 hosts.**
- 165.10.1.128/26 -> **dirección IP asignada para la red número 2 de 44 hosts.**
- 165.10.1.64/26 -> **dirección IP asignada para la red número 3 de 44 hosts.**
- 165.10.1.0/26 -> **dirección IP asignada para la red número 4 de 44 hosts.**

Finalmente las direcciones: `165.10.0.0` hasta `165.10.0.255` quedan libres para seguir subneteando.

---

#### Redes de 12 hosts

Para las redes que necesitan 12 hosts: $2^{4}$ - 2 = 14 hosts.

165.10.0.255 -> red de la cual partimos

1010 0101.0000 1010.0000 0000.1111 1111 -> red expresada en bits

1010 0101.0000 1010.0000 0000.1111 |**0000**| -> bits tomados para los 12 hosts.

|**1010 0101.0000 1010.0000 00**|00.1111 0000 -> bits de red original

1010 0101.0000 1010.0000 00|**00.1111**| 0000 -> bits tomados para subred

- 165.10.0.240/28 -> **dirección IP asignada para la red número 1 de 12 hosts.**
- 165.10.0.224/28 -> **dirección IP asignada para la red número 2 de 12 hosts.**
- 165.10.0.208/28 -> **dirección IP asignada para la red número 3 de 12 hosts.**
- 165.10.0.192/28 -> **dirección IP asignada para la red número 4 de 12 hosts.**
- 165.10.0.176/28 -> **dirección IP asignada para la red número 5 de 12 hosts.**
- 165.10.0.160/28 -> **dirección IP asignada para la red número 6 de 12 hosts.**
- 165.10.0.144/28 -> **dirección IP asignada para la red número 7 de 12 hosts.**
- 165.10.0.128/28 -> **dirección IP asignada para la red número 8 de 12 hosts.**

Finalmente las direcciones: `165.10.0.0` hasta `165.10.0.127` quedan libres para seguir subneteando.

---

## Dada la red IP 4.2.16.0/23 se necesitan definir:
- 1 red de 100 hosts. 
- 4 (cuatro) redes de 60 hosts 
- Las 5 (cinco) redes se conectan en anillo cada una a partir de un router cabecera.

#### Red de 100 hosts

Para la red que necesita 100 hosts: $2^{7}$ - 2 = 126 hosts.

4.2.16.0 -> red de la cual partimos

0000 0100.0000 0010.0001 0000.0000 0000 -> red expresada en bits

0000 0100.0000 0010.0001 0000.0|**000 0000**| -> bits tomados para los 100 hosts.

|**0000 0100.0000 001**|0.0001 0000.0000 0000 -> bits de red original

0000 0100.0000 0010.0001 000|**1.1**|000 0000 -> bits tomados para subred

- 4.2.17.128/25 -> **dirección IP asignada para la red de 100 hosts.**

Finalmente las direcciones: `4.2.16.0` hasta `4.2.17.127` quedan libres para seguir subneteando.

---

#### Redes de 60 hosts

Para las redes que necesitan 60 hosts: $2^{6}$ - 2 = 62 hosts.

4.2.17.127 -> red de la cual partimos

0000 0100.0000 0010.0001 0001.0111 1111 -> red expresada en bits

0000 0100.0000 0010.0001 0001.01|**00 0000**| -> bits tomados para los 60 hosts.

|**0000 0100.0000 0010.0001 000**|1.0100 0000 -> bits de red original

0000 0100.0000 0010.0001 000|**1.01**|00 0000 -> bits tomados para subred

- 4.2.17.64/26-> **dirección IP asignada para la red número 1 de 60 hosts.**
- 4.2.17.0/26 -> **dirección IP asignada para la red número 2 de 60 hosts.**
- 4.2.16.192/26 -> **dirección IP asignada para la red número 3 de 60 hosts.**
- 4.2.16.128/26 -> **dirección IP asignada para la red número 4 de 60 hosts.**

Finalmente las direcciones: `4.2.16.0` hasta `4.2.16.127` quedan libres para seguir subneteando.

---

#### Redes de 2 hosts

Para las redes que necesitan 2 hosts: $2^{2}$ - 2 = 2 hosts.

4.2.16.127 -> red de la cual partimos

0000 0100.0000 0010.0001 0000.0111 1111 -> red expresada en bits

0000 0100.0000 0010.0001 0000.0111 11|**00**| -> bits tomados para los 60 hosts.

|**0000 0100.0000 0010.0001 000**|0.0111 1100 -> bits de red original

0000 0100.0000 0010.0001 000|**0.0111 11**|00 -> bits tomados para subred

- 4.2.16.124/30-> **dirección IP asignada para la red número 1 de 2 hosts.**
- 4.2.16.120/30 -> **dirección IP asignada para la red número 2 de 2 hosts.**
- 4.2.16.116/30 -> **dirección IP asignada para la red número 3 de 2 hosts.**
- 4.2.16.112/30 -> **dirección IP asignada para la red número 4 de 2 hosts.**
- 4.2.16.108/30 -> **dirección IP asignada para la red número 5 de 2 hosts.**

Finalmente las direcciones: `4.2.16.0` hasta `4.2.16.107` quedan libres para seguir subneteando.

---

## Dada la red IP 200.23.0.0/20 se necesitan definir: 
- 4 (cuatro) redes de 100 hosts. 
- 4 (cuatro) redes de 250 hosts 
- 2 (dos) redes de 500 hosts. 
- Las 10 redes anteriores se conectan cada una de forma individual desde un router spoke contra un router central/hub con conexiones punto a punto.

#### Redes de 500 hosts

Para las redes que necesitan 500 hosts: $2^{9}$ - 2 = 510 hosts.

200.23.0.0 -> red de la cual partimos

1100 1000.0001 0111.0000 0000.0000 0000 -> red expresada en bits

1100 1000.0001 0111.0000 000|**0.0000 0000**| -> bits tomados para los 500 hosts.

|**1100 1000.0001 0111.0000**| 0000.0000 0000 -> bits de red original

1100 1000.0001 0111.0000 |**111**|0.0000 0000 -> bits tomados para subred

- 200.23.14.0/23-> **dirección IP asignada para la red número 1 de 500 hosts.**
- 200.23.12.0/23 -> **dirección IP asignada para la red número 2 de 500 hosts.**

Finalmente las direcciones: `200.23.0.0` hasta `200.23.11.255` quedan libres para seguir subneteando.

---

#### Redes de 250 hosts

Para las redes que necesitan 250 hosts: $2^{8}$ - 2 = 254 hosts.

200.23.11.255 -> red de la cual partimos

1100 1000.0001 0111.0000 1011.1111 1111 -> red expresada en bits

1100 1000.0001 0111.0000 1011.|**0000 0000**| -> bits tomados para los 250 hosts.

|**1100 1000.0001 0111.0000**| 1011.0000 0000 -> bits de red original

1100 1000.0001 0111.0000 |**1011**|.0000 0000 -> bits tomados para subred

- 200.23.11.0/24-> **dirección IP asignada para la red número 1 de 250 hosts.**
- 200.23.10.0/24 -> **dirección IP asignada para la red número 2 de 250 hosts.**
- 200.23.9.0/24 -> **dirección IP asignada para la red número 3 de 250 hosts.**
- 200.23.8.0/24 -> **dirección IP asignada para la red número 4 de 250 hosts.**

Finalmente las direcciones: `200.23.0.0` hasta `200.23.7.255` quedan libres para seguir subneteando.

---

#### Redes de 100 hosts

Para las redes que necesitan 100 hosts: $2^{7}$ - 2 = 126 hosts.

200.23.7.255 -> red de la cual partimos

1100 1000.0001 0111.0000 0111.1111 1111 -> red expresada en bits

1100 1000.0001 0111.0000 0111.1|**000 0000**| -> bits tomados para los 100 hosts.

|**1100 1000.0001 0111.0000**| 0111.1000 0000 -> bits de red original

1100 1000.0001 0111.0000 |**0111.1**|000 0000 -> bits tomados para subred

- 200.23.7.128/25-> **dirección IP asignada para la red número 1 de 100 hosts.**
- 200.23.7.0/25 -> **dirección IP asignada para la red número 2 de 100 hosts.**
- 200.23.6.128/25 -> **dirección IP asignada para la red número 3 de 100 hosts.**
- 200.23.6.0/25 -> **dirección IP asignada para la red número 4 de 100 hosts.**

Finalmente las direcciones: `200.23.0.0` hasta `200.23.5.255` quedan libres para seguir subneteando.

---

#### Redes de 2 hosts

Para las redes que necesitan 2 hosts: $2^{2}$ - 2 = 2 hosts.

200.23.5.255 -> red de la cual partimos

1100 1000.0001 0111.0000 0101.1111 1111 -> red expresada en bits

1100 1000.0001 0111.0000 0101.1111 11|**00**| -> bits tomados para los 2 hosts.

|**1100 1000.0001 0111.0000**| 0101.1111 1100 -> bits de red original

1100 1000.0001 0111.0000 |**0101.1111 11**|00 -> bits tomados para subred

- 200.23.5.252/30-> **dirección IP asignada para la red número 1 de 2 hosts.**
- 200.23.5.248/30 -> **dirección IP asignada para la red número 2 de 2 hosts.**
- 200.23.5.244/30 -> **dirección IP asignada para la red número 3 de 2 hosts.**
- 200.23.5.240/30 -> **dirección IP asignada para la red número 4 de 2 hosts.**
- 200.23.5.236/30 -> **dirección IP asignada para la red número 5 de 2 hosts.**
- 200.23.5.232/30 -> **dirección IP asignada para la red número 6 de 2 hosts.**
- 200.23.5.228/30 -> **dirección IP asignada para la red número 7 de 2 hosts.**
- 200.23.5.224/30 -> **dirección IP asignada para la red número 8 de 2 hosts.**
- 200.23.5.220/30 -> **dirección IP asignada para la red número 9 de 2 hosts.**
- 200.23.5.216/30 -> **dirección IP asignada para la red número 10 de 2 hosts.**

Finalmente las direcciones: `200.23.0.0` hasta `200.23.5.215` quedan libres para seguir subneteando.