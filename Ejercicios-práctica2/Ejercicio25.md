# Ejercicio 25

## ¿Cuál sería una abreviatura correcta de 3f80:0000:0000:0a00:0000:0000:0000:0845?

- 3f80::a00::845 -> Incorrecta porque usa dos veces " :: ".
- 3f80::a:845 -> Incorrecta porque transforma "0a00" en "a". Sólo pueden omitirse los ceros a la izquierda. Además de que no contempla los ceros entre "0a00" y "0845", cambiando el valor de la dirección.
- 3f80::a00:0:0:0:845:4567 -> Incorrecta porque añade 4567 al final, que no existe en la dirección original.
- 3f80:0:0:a00::845 -> **Opción correcta para la abreviatura**.
- 3f8:0:0:a00::845 -> Incorrecta porque cambia "3f80" a "3f8", quitando el cero a la derecha. Eso altera el valor del bloque.
