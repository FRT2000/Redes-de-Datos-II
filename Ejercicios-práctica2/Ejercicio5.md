# Ejercicio 5

## Dada la red IP 65.0.0.0/8. Se necesitan definir 934 subredes. Indique qué máscara debería ser utilizada. Indique cuál sería la subred número 817 indicando el rango de direcciones asignables, dirección de red y broadcast.

### IP 65.0.0.0/8
Se necesitan 10 bits para 934 subredes, $2^{10}$ = 1024.

**0100 0001**.0000 0000.0000 0000.0000 0000 -> Red Clase A. Primer octeto reservado para dirección de red.

Para armar la máscara dejamos el primer octeto con unos (1), para no modificar la dirección de red. Posterior al último bit utilizado para la dirección de red, colocamos tantos unos (1) como sea necesario para representar las 934 subredes que necesitamos.

1111 1111.|**1111 1111.11**|00 0000.0000 0000 -> máscara utilizada para identificar la red subneteada.

255.255.192.0 -> Máscara de red utilizada al pasar de binario a decimal.

65.0.0.0/18   -> Podemos escribir su equivalente en notación CIDR, le sumamos 10 al prefijo original (/8) ya que, en este caso, se toman 10 bits adicionales para subnetting.

### Subred 817

#### Dirección de subred 817
En este caso vamos a considerar que la primera red es la cero (0).

Partiendo de la red subneteada, escribimos el número de red que deseamos identificar utilizando solamente los 10 bits que han sido reservados para poder identificar las subredes. El primer octeto debe mantenerse siempre igual.

0100 0001.0000 0000.0000 0000.0000 0000 /18 -> Red subneteada.

0011 0011 0001 -> Número 817 en binario

0100 0001.|**1100 1100.01**|00 0000.0000 0000 -> Colocamos el número anterior entre " | " partiendo de derecha a izquierda.

0100 0001.1100 1100.0100 0000.0000 0000 /18 -> **Dirección de red número 817**.

65.204.64.0/18 -> **Dirección de red al pasar de binario a decimal**.

#### Dirección de broadcast de la subred 817
Partiendo de la dirección de red obtenida, colocamos todos los bits reservados para host en uno (1), sin modificar los primeros 18 bits que ya están destinados para identificar la red subneteada.

0100 0001.1100 1100.0100 0000.0000 0000 -> Dirección de subred 817.

0100 0001.1100 1100.01|**11 1111.1111 1111**|

0100 0001.1100 1100.0111 1111.1111 1111 /18 -> **Dirección de broadcast de la subred**.

65.204.127.255/18 -> **Dirección de broadcast al pasar de binario a decimal**.

#### Direcciones asignables
Primero identificamos la primera dirección de red asignable a un host, tomando como referencia la dirección de red que hemos obtenido anteriormente. Como esta dirección nos identifica la red no es posible asignarla, entonces comenzamos a partir de la siguiente red para asignar los host.

65.204.64.0/18 -> Dirección de red.

65.204.64.1/18 -> Primera dirección de red asignable para host.

También podríamos haberlo hecho sumando uno (1) en la parte de bits asignados para host. Llegaremos al mismo resultado si luego convertimos el resultado a decimal.

0100 0001.1100 1100.0100 0000.0000 0000 -> Dirección de red.

0100 0001.1100 1100.01|**00 0000.0000 0001**| -> Primera dirección de red asignable para host.

Ahora debemos identificar la última dirección de red asignable, tomando como referencia la dirección de broadcast de la subred. Al igual que la dirección de red, esta direccíon tampoco puede ser asignada para un host, por lo que la última red asignable será la anterior a esta.

65.204.127.255/18 -> Dirección de broadcast.

65.204.127.254/18 -> Última dirección de red asignable para host.

También podríamos haberlo hecho restando uno (1) en la parte de bits asignados para host. Llegaremos al mismo resultado si luego convertimos el resultado a decimal.

0100 0001.1100 1100.0111 1111.1111 1111 -> Dirección de broadcast.

0100 0001.1100 1100.01|**11 1111.1111 1110**| -> Última dirección de red asignable para host.

**Rango de direcciones asignables** -> `65.204.64.1` - `65.204.127.254`.