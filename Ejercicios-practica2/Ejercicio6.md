# Ejercicio 6

## Dada la red IP 195.200.45.0/24. Se necesitan definir 9 subredes. Indique la máscara utilizada y las nueve subredes. Luego tome una de ellas e indique el rango de direcciones asignables en esa subred, dirección de red y broadcast.

### IP 195.200.45.0/24
Se necesitan 4 bits para 9 subredes, $2^{4}$ = 16.

**1100 0011.1100 1000.0010 1101**.0000 0000 -> Red Clase C. Primeros tres octetos reservado para dirección de red.

Para armar la máscara dejamos el primer octeto con unos (1), para no modificar la dirección de red. Posterior al último bit utilizado para la dirección de red, colocamos tantos unos (1) como sea necesario para representar las 9 subredes que necesitamos.

1111 1111.1111 1111.1111 1111.|**1111**| 0000 -> máscara utilizada para identificar la red subneteada.

255.255.255.240 -> **Máscara de red utilizada al pasar de binario a decimal**.

195.200.45.0/28 -> Podemos escribir su equivalente en notación CIDR, le sumamos 4 al prefijo original (/24) ya que, en este caso, se toman 4 bits adicionales para subnetting.

---

### Definir 9 subredes
En este caso tomaremos las 9 subredes a partir de la primera dirección de subred. Podemos elegir la cualquiera de las 16 subredes disponibles dentro del rango comprendido.

195.200.45.0/28 -> Primera dirección de subred. 

Primero debemos identificar el salto de red, es decir, cuántos incrementos ocurren entre cada subred. Para esto nos colocamos en los 4 bits asignados para subredes y sumamos uno (1).

1100 0011.1100 1000.0010 1101.0000 0000 /28 -> Red subneteada. Esta es la primera dirección que puede asignarse para subredes.

1100 0011.1100 1000.0010 1101.|**0001**| 0000 -> Segunda dirección asignable para subredes.

Pasamos a decimal para visualizar fácilmente el incremento entre la primera y segunda subred.

195.200.45.|**16**|/28 -> El incremento fue de 16, por lo tanto las direcciones de subred incrementarán en 16.

Tambíen podemos seguir sumando uno (1) en los bits asignados para las direcciones de subred, al pasar a decimal llegarmos al mismo resultado.

**Primeras 9 subredes elegidas:**

- 195.200.45.0/28
- 195.200.45.16/28
- 195.200.45.32/28
- 195.200.45.48/28
- 195.200.45.64/28
- 195.200.45.80/28
- 195.200.45.95/28
- 195.200.45.112/28
- 195.200.45.128/28

---

### Subred 195.200.45.0/28

Se elige esta subred por simplicidad.
La **dirección de red** será la que elegimos: 195.200.45.0/28

#### Dirección de broadcast
Partiendo de la dirección de red obtenida, colocamos todos los bits reservados para host en uno (1), sin modificar los primeros 28 bits que ya están destinados para identificar la red subneteada.

1100 0011.1100 1000.0010 1101.0000 0000 -> Dirección de subred elegida.

1100 0011.1100 1000.0010 1101.0000 |**1111**|

1100 0011.1100 1000.0010 1101.0000 1111 /28 -> **Dirección de broadcast de la subred**.

195.200.45.15/28 -> **Dirección de broadcast al pasar de binario a decimal**.

---

#### Direcciones asignables
Primero identificamos la primera dirección de red asignable a un host, tomando como referencia la dirección de red que hemos elegido. Como esta dirección nos identifica la red no es posible asignarla, entonces comenzamos a partir de la siguiente red para asignar los host.

195.200.45.0/28 -> Dirección de red.

195.200.45.1/28 -> **Primera dirección de red asignable para host**.

También podríamos haberlo hecho sumando uno (1) en la parte de bits asignados para host. Llegaremos al mismo resultado si luego convertimos el resultado a decimal.

1100 0011.1100 1000.0010 1101.0000 0000 -> Dirección de red.

1100 0011.1100 1000.0010 1101.0000 |**0001**| -> Primera dirección de red asignable para host.

Ahora debemos identificar la última dirección de red asignable, tomando como referencia la dirección de broadcast de la subred. Al igual que la dirección de red, esta direccíon tampoco puede ser asignada para un host, por lo que la última red asignable será la anterior a esta.

195.200.45.15/28 -> Dirección de broadcast.

195.200.45.14/28 -> **Última dirección de red asignable para host**.

También podríamos haberlo hecho restando uno (1) en la parte de bits asignados para host. Llegaremos al mismo resultado si luego convertimos el resultado a decimal.

1100 0011.1100 1000.0010 1101.0000 1111 -> Dirección de broadcast.

1100 0011.1100 1000.0010 1101.0000 |**1110**| -> Última dirección de red asignable para host.

**Rango de direcciones asignables** -> 195.200.45.1 - 195.200.45.14