# REFERENCIACIÓN DE DATOS

## INTRODUCCIÓN

En esta segunda clase vamos a avanzar con temas nuevos y repasar conceptos vistos gráficas a una práctica.
Practicaremos utilización de recursos gráficos, KPI's, creación de nuevas columnas mediante cálculos y como aprovecharlas mediante gráficos.

> [!NOTE]  
> En esta clase trabajamos con un set de datos ya creado Padron_Establecimiento.csv el cual se encuentra aqui mismo.

## ACTIVIDAD RECURSOS DENTRO DEL DATASET

¡Veamos como hacer mas llamativas esas columnas! 

### Cargar datos
Lo primero que tenemos que hacer es importar el set de datos llamado Employee_Data.csv con Excel.

> Datos -> Obtener datos de texto/csv -> Seleccionamos el archivo -> Cargar

> Podemos asignarle un color verde a la pestaña de la hoja.

### Correción columnas

Vamos a modificar las columnas Asignación parcial y Asignación final. Ya que tenemos un signo $, ademas de indicarla como numérica y disminuir el numero de decimales.

> Seleccionamos la columna -> Buscar y seleccionar -> Reemplazar -> Buscar "$" -> Reemplazamos con nada -> Reemplazar todos

> Seleccionamos la columna -> Número -> Número -> Disminuir decimales -> Disminuimos en 2

### Tranformación solo mayúsculas

Veamos como seria transformar una columna tipo texto a solo mayúsculas, esto tambien se puede hacer a solo minúsculas o primera mayúscula.

Insertamos una nueva columna a la derecha de Sector, la renombramos a SECTOR_COLOR
En la primer casilla usamos la formula.
```
=MAYUSC([@Sector])
```

### Regla de colores
Podemos asignar colores para cada tipo de valor, haciendo mas facíl su visualización.

Apliquemos una regla de colores a nuestra nueva columna (verde ESTATAL, azul PRIVADO, naranja SOCIAL/COOPERATIVA).

> Seleccionamos la columna -> Formato condicional -> Administrar reglas

> Nueva regla -> Aplicar formato únicamente a las celdas que contengan -> Texto especifico -> que contiene -> ESTATAL

> Formato -> Seleccionamos verde -> Aceptar -> Aceptar

Repetimos para los otros dos valores...

### Barra de cantidad
Podemos tambien agregar una barra en función de la cantidad escecífica de una celda.

Apliquemos una barra de colores para la cantidad de alumnos.

> Seleccionamos la columna -> Formato condicional

> Barras de datos -> Mas reglas -> Seleccionamos el color -> Aceptar

> [!IMPORTANT]  
> Vemos como al integrar la barra el número de la celda resulta dificil de ver, es importante que al agregar caracteristicas a nuestro trabajo estas faciliten la comprensión y no viceversa.

Como no facilita ver cuantos alumnos hay lo re hacemos aparte.

> Seleccionamos la columna -> Formato condicional -> Administrar reglas -> Borrar reglas -> Borrar celdas seleccionadas

Duplicamos la columna cantidad alumnos al lado de la origina, y la renombramos Barra cant alumnos.

> [!CAUTION]
> Mucho cuidado, porque si duplicamos usando copiar y pegar podemos insertar muchisimas filas en blanco debajo de la tabla que afectaran el rendimiento negativamente.
> Es mejor realizar un duplicado usando una función que no copie filas vacias.

Optamos por duplicar con una funcion SI, la cual no agrgara mas registros vacios al final de la tabla.
```
=SI(L2<>""; L2; "")
```
Volvemos a implementar la barra en función de las cantidades.

> Seleccionamos la columna -> Formato condicional -> Barras de datos

> Mas reglas -> Mostrar solo la barra -> Seleccionamos el color -> Aceptar

### KPI's promedios

Vamos a asignar un KPI para cada rango de promedios escolares.

Queremos poner colores (verde para 9 y 10, amarillo para 7 y 8, rojo para menos de 6) para la columna Promedio nota alumnos.

> Seleccionamos la columna -> Formato condicional -> Conjunto de íconos

> Mas reglas -> Aplicar formato a todas las celdas segun sus valores

Dentro del cuadro completamos
> Icono verde cuando el valor es -> (Regla) >= -> (Valor) 10 -> (Tipo) Número

> Icono amarillo cuando <10 y -> (Regla) >= -> (Valor) 7 -> (Tipo) Número

> Icono rojo cuando < 7

> [!TIP]
> Ahora al seleccionar la columna podemos ver que en la categoria de filtros se encuentra una ópcion "Filtrar por color", la cual usara nuestros KPI's.

### Calculo asignación economica
Teniendo en cuenta que se dará una asignación de $20 por estudiante para cada establecimiento: 
 - Calcular la asignación PARCIAL de cada establecimiento.
 - Calcular la asignación FINAL teniendo en cuenta que si el establecimiento es RURAL, se adiciona un 10% a la asignación por estudiante.

Insertamos una nueva columna que se llame Calculo_parcial.

> [!CAUTION]
> Si utilizamos una formula como `=02*20` puede que excel comienze a insertar columnas incluso cuando tengamos registros en blanco.
> Esto tambien afectaria negativamente el rendimiento.


Para evitar que excel empiece a meter ceros incluso donde ya no tenemos filas podemos usar una expresion SI parecida a:
```
=SI(O2<>""; O2*20; "")
```

Ahora podemos aplicar un procedimiento similar para el cálculo final. 
```
=SI(F2="Rural";P2*1,1;P2)
```

## ACTIVIDAD CREACIÓN DE GRÁFICOS
La mejor manera para entender como se distribuyen nuestros datos es utilizando gráficos, siempre y cuando estos sean adecuados.

Creamos una nueva hoja, la renombramos "gráficos" y le asignamos un color naranja a su pestaña. Además, creamos una pestaña "Reporte" le asignamos un tono naranja a su pestaña.

### Cantidad de establecimiento por tipo

Con este tipo de información un gráfico de barra es la mejor opción.

Para ello lo primero es en la hoja de reportes creamos una tabla con los recuentos para cada tipo de establecimiento.
```
=CONTAR.SI(Padron_Establecimiento[SECTOR_MAYUSC];"ESTATAL")
=CONTAR.SI(Padron_Establecimiento[SECTOR_MAYUSC];"PRIVADO")
=CONTAR.SI(Padron_Establecimiento[SECTOR_MAYUSC];"SOCIAL/COOPERATIVA")
```

En la hoja gráficos vamos a insertar un gráfico de barras


> Gráficos -> Columnas en 2D -> Columnas agrupadas -> Lo ubicamos donde queremos

> Seleccionar datos -> Entrada de leyendas (Series) -> Agregar

> Nombre de la serie -> Gráfico barras establecimientos

> Valores de la serie -> Seleccionamos las 3 casillas con los recuentos para cada tipo de establecimiento -> Aceptar

> Etiquetas del eje horizontal -> Editar -> Seleccionamos las 3 casillas con los nombres para cada tipo de establecimiento -> Aceptar

Vamos a mejorar este gráfico
> Seleccionamos las barras -> Agregar etiquetas de datos

> Seleccionamos de a una barra -> Formato de punto de datos -> Relleno y linea -> Color (verde estatal, azul privado, naranja social/cooperativa)

### Gráfico comparativo promedios vs ámbito escolar
Veamos como es el rendimiento academico de los alumnos de las escuelas rurales y urbanas.

Para poder realizar este gráfico primero tenemos que crear una tabla con las frecuencias absolutas y relativas, que para cada promedio por ámbito escolar.

Para ello en la hoja reporte vamos a agregar 5 columas(notas, rural_abs, rural_fre, urbano_abs, urbano_fre).

En notas pondremos numeros del 1 al 10 y debajo agregaremos total.

Hay que calcular cuantas escuelas rurales tienen un promedio de 1, 2, 3, etc. Para ello usaremos `CONTAR.SI.CONJUNTO`.

```
=CONTAR.SI.CONJUNTO(Padron_Establecimiento!F:F;"Rural";Padron_Establecimiento!R:R;[@NOTA])
```

Y el total de las esculas rurales con `CONTAR.SI`.
```
=CONTAR.SI(Padron_Establecimiento!F:F;"Rural")
```

Una vez tenemos estos dos valores hay que calcular las frecuencias para cada nota.
```
=([@[RURAL_ABS]]/$E$12)
```
Indicamos a la columna como porcentaje. Repetimos el paso para las escuelas urbanas.

De vuelta en la hoja de gráficos vamos a mostrar lo calculado.

> Graficos -> gráficos lineas -> linea con marcadores

> Seleccionar datos -> Entrada de leyendas -> Agregar

> Nombre serie -> Frecuencia rural -> Valores -> Seleccionamos las 10 casillas de rural_fre -> Aceptar

> Entrada de leyendas -> Agregar

> Nombre serie -> Frecuencia urbana -> Valores -> Seleccionamos las 10 casillas de urbana _fre -> Aceptar

Vamos a mejorar este gráfico.

Primero complementado con téxto:

> Seleccionamos el gráfico -> + (Elementos gráficos) -> Título de gráfico (Comparación promedios rural vs urbano)

> Seleccionamos leyendas -> Títulos de eje (Frecuencia) y (Promedio escolar)

Personalizando colores:
> Seleccionamos una línea -> Dar formato a serie de datos -> Relleno y linea

> Línea -> Color del contorno -> Seleccionamos color

> Marcador -> Color del relleno -> Seleccionamos color

Repetimos para la otra línea

### Cantidades de tipos de escuela por provincia
Vamos a ver cuantas escuales estatales, privadas y social/cooperativa hay por cada provincia

Lo primero es extraer los valores únicos de la columna jurisdiccion

> Seleccionamos la columna -> Datos -> Ordenar y filtrar -> Avanzadas

> Copiar a otro lugar -> Copiar a (seleccionmos un apartado al final de la hoja) -> solo registros unicos -> Aceptar


Copiamos las provincias y las pegamos en la hoja de reportes en una columna llamada provincia.
Creamos 3 columnas nuevas ESTATAL_ABS, PRIVADO_ABS y SOCIAL/COOPERATIVA_ABS.

Ahora usamos una funcion `CONTAR.SI.CONJUNTO` donde el criterio 1 será establecimiento estatal y el criterio 2 jurisdicción igual a cada una de las provincias.

Aplicando una formula similar a:

```
=CONTAR.SI.CONJUNTO(Padron_Establecimiento!E:E;"ESTATAL";Padron_Establecimiento!A:A;[@PROVINCIA])
```

> [!TIP]
> Podemos hacer una `SUMAR` al final de todos los valores para comprobar que el total este bien

Repetimos el procedimiento pero en usando "PRIVADO" y "SOCIAL/COOPERATIVA" para cada columna y provincia.

En la hoja de gráficos vamos a representar visualmente lo que calculamos

> Gráfico -> Barras 2D -> Barras apiladas -> Seleccionar datos

> Entrada de leyendas -> Agregar -> Nombre (ESTATAL) -> Seleccionamos los valores estatales por provincia de reporte -> Aceptar

> Entrada de leyendas -> Agregar -> Nombre (PRIVADO)-> Seleccionamos los valores privados por provincia de reporte -> Aceptar

> Entrada de leyendas -> Agregar -> Nombre (SOCIAL/COOPERATIVA) -> Seleccionamos los valores social/cooperativa por provincia de reporte -> Aceptar

> Etiquetas de eje horizontal -> Editar -> Rango rótulo de eje -> Seleccionamos el listado de provincias -> Aceptar


Vamos a mejorar este gráfico. Primero complementado con texto:
> Seleccionamos el gráfico -> + (Elementos gráficos)

> Título de gráfico (Cantidad y tipos de escuelas por provincias) -> Seleccionamos leyendas

Despues ajustando el color para que coincida con lo realizado anteriormente.
> Seleccionamos de a una barra -> Formato de punto de datos -> Relleno y linea -> Color (verde estatal, azul privado, naranja social/cooperativa)
