# Ejercicio 9

## ¿Cuáles de las siguientes no son direcciones IPv6 válidas, cuáles asignables a un host?

### 2001:0:1019:afde::1
- Dirección válida.
- Puede ser asignada.

### 2001::1871::4
- Dirección inválida.
- Repite " :: " más de una vez para abreviar los ceros consecutivos dentro de la dirección IP.

### 3ffg:8712:0:1:0000:aede:aaaa:1211
- Dirección inválida.
- Contiene una " g " lo cual no pertenece al sistema hexadecimal.

### 3::1
- Dirección válida.
- Puede ser asignada.

### 3ffe:1080:1212:56ed:75da:43ff:fe90:affe
- Dirección válida.
- No asignable a un host (bloque 6Bone 3FFE::/16, retirado en 2006).

### ::
- Dirección válida.
- No asignable a un host. Se usa como dirección no especificada.

### 2001::
- Dirección válida.
- No asignable a un host. Es una dirección de red.

### 3ffe:1080:1212:56ed:75da:43ff:fe90:affe:1001
- Dirección inválida.
- Tiene 9 grupos de 8 bits, cuando solamente debería tener 8 grupos para poder cumplir con los 128 bits de dirección dentro del protocolo.