# Ejercicio 13

## Dada la red IP 195.200.45.0/25. Se necesitan definir 6 subredes de 6 host c/u. Indique la máscara utilizada y la subred número 4.

### Máscara utilizada
Primero determinamos la cantidad de bits necesarios para poder representar los hosts. Para este caso 3 bits.

Con 3 bits tenemos: $2^{3}$ - 2 = 6

Ahora observamos la cantidad de bits que quedan disponibles para las direcciones de red luego de tomar los 3 bits para hosts. Con esto nos aseguramos que todas las redes que queramos asignar tengan hasta 6 hosts disponibles.

195.200.45.0000 0|**000**| -> Bits tomados para hosts.

|**195.200.45.0000 0**|000 -> Bits tomados para dirección de red.

**La máscara utilizada para identificar la red será**

255.255.255.248 ó 195.200.45.0/29

### Subred número 4
Para este caso consideramos que la primera red es la número cero (0).

Contamos con una red de Clase C y se ha subneteado tomando 5 bits para subredes. Debemos colocar el número 4 en binario dentro de ese rango de bits destinado para las direcciones de subred.

195.200.45.|**0000 0**|000 -> Bits tomados para direcciones de subred.

195.200.45.|**0010 0**|000 -> **Dirección de la subred número 4**.

195.200.45.32/29 -> **Dirección de subred número 4 en decimal**.

### Definir 6 subredes
Por simplicidad empezamos desde la primera dirección disponible para asignar las 6 subredes solicitadas.

Calculamos el salto de red, sumando uno a la primera dirección de red disponible.

195.200.45.|**0000 1**|000 

195.200.45.8/29 -> Las subredes tendrán incrementos de a 8.

**Las 6 primeras subredes serán:**

- 195.200.45.0/29
- 195.200.45.8/29
- 195.200.45.16/29
- 195.200.45.24/29
- 195.200.45.32/29
- 195.200.45.40/29