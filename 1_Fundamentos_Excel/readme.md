# FUNDAMENTOS EXCEL

## INTRODUCCIÓN

En esta primera clase vamos a realizar una simple práctica.
La idea es aprender conceptos básicos de excel, utilizando datos en bruto y trabajando en ellos.

> [!NOTE]  
> En esta clase trabajamos con un set de datos ya creado Employee_Data.csv el cual se encuentra aqui mismo.
> Podés realizar la práctica en Excel de forma local, o con Google Sheets desde drive.
> El archivo Clase_1.xlsx el resultado final, siempre puedes descargarlo y consultar como deberia quedarte.


## ACTIVIDAD TRANSFORMACIÓN DATASET

¡Es hora de ponernos manos a la obra! 

### Cargar datos

Lo primero que tenemos que hacer es importar el set de datos llamado Employee_Data.csv con Excel. 

> Datos -> Obtener datos de texto/csv -> Seleccionamos el archivo -> Cargar

Podemos asignarle un color verde a la pestaña de la hoja.

### Formatear columna salarios

Despues de analizar la columna de salarios vemos que hay un problema. Ya que tenemos un signo $ que impide poder realizar calculos.

> Seleccionamos la columna -> Buscar y seleccionar -> Reemplazar -> Buscar "$" -> Reemplazamos con nada -> Reemplazar todos

### Crear columna con nombre completo

Vamos a practicar trabajar con columnas con datos del tipo texto. Necesitamos tener el nombre y apellido en una sola celda.

Insertamos una nueva columna y la renombramos como Full Name.

```
=CONCATENAR([@[First Name]];" ";[@[Last Name]])
```

### Subdividir la fecha de ingreso

A la columna hire date la indicamos como fecha corta.

Tenemos una columna hire date con formato dd/mm/yyyy; vamos a crear 3 nuevas columnas Year, Month y Day.

Las formulas que utilizamos respectivamente son

```sh
=AÑO() # Con Excel en Ingles usamos =YEAR()
=MES() # Con Excel en Ingles usamos =MONTH()
=DIA() # Con Excel en Ingles usamos =DAY()
```

> [!WARNING]  
> ¿Que tipo de problemas Excel puede acarrear que dependa del idioma la instruccion?

### Calculo salario total anual

Veamos cuanto dinero van a cobrar los empleados anualmente despues de recibir sus bonos.

Lo primero es eliminar la coma que aparece en cada valor de Annual Salary ya que esta separando mal, porque estamos en miles y lo marca como decimales.

> Seleccionamos la columna -> Buscar y seleccionar -> Reemplazar -> Buscar "," -> Reemplazamos con nada -> Reemplazar todos

Insertamos una nueva columna, la renombramos a Total Salary, y realizamos el calculo como este.

```sh
=[@[Annual Salary]] * (1 + [@[Bonus %]]) #De forma matematica seria A1 * (1 + B1)
```

### Años para jubilarse

¿Cuando años le quedan para poder jubilarse a cada empleado?

Tomando 65 como la edad de jubilacion, en una nueva hoja llamada Constantes (podemos ponerle un color amarillo a su pestaña). Le damos nombre a la columna como Retirement Age y le asignamos 65 abajo. Podemos darle formato como tabla agregando naranja como tono

De vuelta en la hoja employee_data insertamos una nueva columna Retirement Years y calculamos la resta usando una formula parecida a.

```
=Constantes!$A$2-[@Age]
```

> [!WARNING]  
> Para evitar que de error al aplicar la formula a todas las filas, hay que fijar con $$ a la constante en nuestra formula.

## ACTIVIDAD CREACIÓN REPORTE

Vamos a crear un reporte para poder ver información importante a simple viste utilizando nuevas formulas. 
Creamos una nueva hoja, la renombramos y le asignamos un color azul a su pestaña.

### Cantidad de empleados totales

Calculemos cuantos empleados hay en la base de datos.

Asignamos a una columna que llamaremos Cantidad Empleados, y para su calculo usamos.

```
=CONTARA(Employee_Data!A:A)-1
```

> [!TIP]
> Como no queremos que tenga en cuenta el cabecero restamos 1.

### Cantidad de empleados en activo

Calculemos cuantos empleados hay en activo (los que tienen exited date ya no trabajan en la empresa).

Para ello solamente tenemos que hacer un calculo, restar a la cantidad de empleados totales la cantidad de veces que aparece un registro en exited date.

```
=([@[Cantidad Empleados]] - CONTARA(Employee_Data!U:U)-1)
```

### Edad media empleados

Veamos cual es la edad media de los empleados. 

> [!NOTE]
> Recordemos que media puede ser descrita como promedio.

En reporte insertamos una nueva columna llamada Edad Promedio, para su calculo usamos algo parecido a.

```
=PROMEDIO(Employee_Data!F:F)
```

### Empleados departamento IT

En nuestro reporte tenemos que indicar cuantos empleados del departamento IT hay.

Insertamos una columna y la llamamos IT Employee, abajo para su calculo usamos una formula similar a.

```
=CONTAR.SI(Employee_Data!I:I;"IT")
```

### Empleados Estadounidenses del departamento Sales

Queremos saber la cantidad de empleados en USA del sector Sales que se han contratado.

Para esto aplicamos un CONTAR.SI pero usando su variante CONJUNTO ya 2 condiciones las que necesitan cumplirse, en el ejemplo vemos que quedaria asi.

```
=CONTAR.SI.CONJUNTO(Employee_Data!I:I;"Sales";Employee_Data!S:S;"United States")
```

### Presupuesto salarios en finanzas

¿Cuanto es el presupuesto minimo que debe tener el área de finanzas para salarios?

Necesitamos la funcion SUMAR.SI ya que necesitamos realizar una suma pero a su vez que esta solo se aplique a los valores que cumplan una condicion.

```
=SUMAR.SI(Employee_Data!I:I;"Finance";Employee_Data!R:R)
```