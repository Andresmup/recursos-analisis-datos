# TABLAS DINÁMICAS

En esta ocasión vamos a trabajar con tablas dinámicas ademas de aprender tip y herramientas útiles.

## Cargar datos
Lo primero que tenemos que hacer es importar el set de datos llamado Employee_Data.csv con Excel.

> Datos -> Obtener datos de texto/csv -> Seleccionamos el archivo -> Cargar

Vemos que nuestro dataset tiene un problema a la hora de cargar los valores numericos, ya que todos los valores decimales desaparecieron y ahora son numeros enteros.

Vamos a descartar esta importación para hacer una nueva aplicando pasos un poco mas avanzados.

## Cargar datos y editar usando Power Query

Vamos a procesar y transformar las columnas que tenian problemas antes de cargarlas.

> Datos -> Obtener datos de texto/csv -> Seleccionamos el archivo -> Cargar

> [!IMPORTANT]  
> Hacemos click en tranformar datos, lo cual abre el panel de PowerQuery

Vemos que podemos visualizar cada columna, podemos observar los diferentes pasos que excel les aplica al cargarlas.

> Borramos el último paso "Tipo cambiado"

Tenemos reemplazar los "." por "," en nuestras columnas `Sales`, `Quantity`, `Discount`, `Profit` y indicarle que que es un numero decimal o entero según corresponda:

Seleccionamos la columna Sales
> Transformar -> Reemplazar los valores -> Valor que buscar "." -> Reemplazar con "," -> Aceptar

> Transformar -> Tipo de dato -> Número decimal

Seleccionamos la columna Quantity

> Transformar -> Tipo de dato -> Número entero

Seleccionamos la columna Discount
> Transformar -> Reemplazar los valores -> Valor que buscar "." -> Reemplazar con "," -> Aceptar

> Transformar -> Tipo de dato -> Porcentaje

Seleccionamos la columna Profit
> Transformar -> Reemplazar los valores -> Valor que buscar "." -> Reemplazar con "," -> Aceptar

> Transformar -> Tipo de dato -> Número decimal

> [!WARNING]
> Al eliminar el paso `Tipo cambiado` las columnas con fechas quedaron como texto. ¡Hay que formatearlas!

Seleccionamos la columna Order Date
> Transformar -> Tipo de dato -> Fecha

Seleccionamos la columna Ship Date
> Transformar -> Tipo de dato -> Fecha

## Tablas dinamicas

Una vez tenemos nuestra tabla cargada ya podemos usar tablas dinamicas.

Seleccionamos cualquier celda de `Superstore_Dataset` y vamos a:

> Insertar -> Tablas dinamicas -> Tabla o rango = Superstore_dataset

> Seleccionamos la opción `Nueva hoja de calculo` y renomabramos la hoja como `Tablas dinamicas` -> Aceptar

## Ejercicios de aprendizaje

Vamos a aprender los beneficios, posibilidades y opciones que nos brindan las tablas dinamicas.

### Categorias vs ventas

Nuestro reporte quiere mostrar cual fueron las categorias (que tipo de articulos) fueron los que mas dinero ingresaron.

Para ello simplemente en nuestra tabla dinamica tenemos que:

> Seleccionar y arrastrar `Category`-> Filas

> Seleccionar y arrastrar `Sales`-> Valores

Podemos cambiar la forma en que se ven los numeros:

> Seleccionamos las celdas con los valores numericos -> Número -> Mondeda 

> Podemos cambiar el simbolo de la móneda a cualquiera. En `Más formatos de números...`

> [!NOTE]  
> Con esto facilitamos visualizar la información pero no alteramos el contenido de la celda, no agregamos un signo que despues no nos permita operar numéricamente.

### Categorias vs ventas

Ahora queremos hacer algo parecido pero viendo que catergoria fue la que mas profit generó

Podemos agregar una nueva tabla dinamica repitiendo pasos. Seleccionamos cualquier celda de `Superstore_Dataset` y vamos a:

> Insertar -> Tablas dinamicas -> Tabla o rango = Superstore_dataset

> Seleccionamos la opción `Hoja de calculo existente` y ubicamos una celda al costado de la tabla que ya tenemos -> Aceptar

Vamos a insertar la información:

> Seleccionar y arrastrar `Category`-> Filas

> Seleccionar y arrastrar `Sales`-> Valores

Reajustamos nuevamente para que se vean mas fácilmente

> [!TIP]
> Podemos ordenar los valores de mayor a menor cantidad. En Datos -> Ordenar y filtrar -> Z hasta A

### Cantidad de compradores vs región

Vimos como sumar valores por categorias, pero no siempre vamos a querer sumar. Por ejemplo, ahora necesitamos saber cuantos clientes tenemos por cada región.

Insertamos una nueva tabla dinamica en nuestra hoja como ya vimos.

Vamos a insertar la información:
> Seleccionar y arrastrar `Region`-> Filas

> Seleccionar y arrastrar `Costumer ID`-> Valores

> [!IMPORTANT]  
> Haciendo click en el valor y en `configuración de campo` puedo indicar que en vez de sumar quiero contar (o cualquier otra operación).


> [!TIP]
> Podemos mostrar simplemente el % de clientes respecto del total, seleccionando las filas, en el menú del click secundario, mostrar valores como `% del total general`

### Cantidad de ventas por subcategoría para cada mes

Ahora queremos saber cuantas ordenes de compra hubo para cada subcategoria, pero pudiendo evaluar para cada mes

Insertamos una nueva tabla dinamica en nuestra hoja como ya vimos.

Vamos a insertar la información:

> Seleccionar y arrastrar `Sub-category`-> Filas

> Seleccionar y arrastrar `Order ID`-> Valores

> Seleccionar y arrastrar `Order Date`-> Filas -> Descartamos `Años`, `Trimestres` y `Order Date` -> Seleccionar y arrastrar `Meses`-> Filtros

Ahora podemos variar cuantos meses queremos tener de información en nuestra tabla con el filtro.

### Detección de top 5 mayores descuentos por estado para cada categoria

Si quisieramos evaluar en que estados se aplican mayores decuentos, teniendo en cuenta el Segmento (`Home Office`, `Corporate` o `Consumer`) podriamos hacerlo asi:

Insertamos una nueva tabla dinamica en nuestra hoja como ya vimos.

Vamos a insertar la información:

> Seleccionar y arrastrar `State`-> Filas

> Seleccionar y arrastrar `Discount`-> Valores -> Configuramos la operación a realizar con `Promedio`

> Seleccionar y arrastrar `Segment`-> Filtros. **Sin embargo no vamos a usar esta opción.**

> [!IMPORTANT]  
> La forma mas profesional y visual será utilizar Segmentación de datos:
> - Hacemos click en la tabla -> Analizar tabla dinámica -> Insertar Segmentación de datos -> Segment -> Aceptar

Para que se vea mas facilmente podemos reajustar el formato a porcentaje

> [!NOTE]  
> Para poner los top 5 simplemente tenemos que:
> - Ordenar desde Z hasta A
> - Ir a las opciones de la fila, filtros de valor, `Diez mejores...` y adaptamos para top 5.


## Actividad en solitario

Ahora se proponen un par de actividades para que practiques sin seguir una guía.

### Promedio de profit para cada sub categoria para cada semestre.

Se propone hacer una tabla, la cual es muy similar a la ya realizada anteriormente pero con otras columnas

> [!TIP]
> Al añadir la columna `Profit` a `Valores` vamos a ejecutar un cálculo `Promedio`

### Inclusión de gráficos

Se propone como práctica recomendada realizar en una nueva pestaña `Gráficos dinámicos` diferentes gráficos utilizando como fuente de datos las tablas dinamicas.

> [!NOTE]  
> Si modificamos los valores de una tabla dinamica con filtros el gráfico automaticamente se actualizara