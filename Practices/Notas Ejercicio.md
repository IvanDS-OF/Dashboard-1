# Ejercicio de prueba

### Primera parte - Crear la tabla con los valores juntos y una columna de diferenciación

Primero hay que entender el ejercicio y los requerimientos necesarios para poder hacerlo,

Ahora solamente se va a hacer la descripcion de los pasos para poder llegar hasta el objetivo. 

### Relacion entre tablas

Lo primero que hay que ahcer es la relacion entre tablas, para ello es necesario

* Crear una nueva tabla con solamente los valores individuales de nuestra columna **product_category**, lo vamos a hacer mediante el uso del siguiente codigo 

``` Java
Individual Values = GROUPBY(SALES_DB, SALES_DB[product_category])
```

* Posteriormente tenemos que hacer la relacion como manda la regla, siempre buscando que sea de **UNO A MUCHOS**, para ello seleccionamos nuestra columna en la tabla y la arrastramos hasta nuestra tabla inicial, siempre revisando ue la relacion sea Uno a Muchos, y hacemos lo mismo con la otra tabla. 

* Luego ya en nuestro reporte creamos una **Tabla** y le colocamos los valores contenidos en nuestra nueva tabla, que es el Product_Category pero de la nueva tabla, y añadimos igualmente la columna **price** de las dos bases de datos

* Para obtener el valor ooleano entre la diferencia de ls precios tenemos que crear una nueva Medida dentro de la base de datos nueva creada, tiene que estar aquí dentro poor que va a tomar valores de las otras dos tablas. El codigo es el siguiente: 

``` Java
Diferencia = IF( SUM(SALES_DB[price]) <> SUM(SALES_MANUAL[price]) , FALSE(), TRUE())
```

### Segunda parte - Crear un Drop Drill de la información que encontremos diferente

* Primero tenemos que crear una nueva pagina en donde vamos a insertar una nueva **tabla**

* Para generar correctamente la información tendremos que, desde la vista **Table view** crear una nueva columna en la Tabla **SALES_DB**, la columna tiene que servir para que por cada valor en *transaction_id*, busque en la tabla **SALES_MANUAL** y me traiga el precio correspondiente al valor encontrado en *transaction_id*,el código que usamos es el siguiente:

``` Java
Price Manual = LOOKUPVALUE( SALES_MANUAL[price], SALES_MANUAL[transaction_id], SALES_DB[transaction_id] )
```

| LOOKUPVALUE | Tabla en donde va a buscar | El valor que va a tener de referencia en donde va a ir a buscar | El valor de referencia de la tabla en donde estamos |

* Al final, solamente agregamos otra columna que nos va a dar si los valores en las fias de *price* y *Price Manual* sin iguales o diferentes, pero nos tiene que regresar un valor Booleano, para ello ocupamos el siguiente codigo. 

``` Java
Diferencia Precios = SALES_DB[price] <> SALES_DB[Price Manual]
```

* Dentro de nuestra nueva pagina, en la tabla creada, agregamos la columna *product_category* que iene de la tabla creada en el paso 1, *transaction_id* que viene de la tabla en donde hicimos los movimientos de creación en este caso será **SALES_dB**, *price* que viene de **SALES_DB** y finalmente la nueva columna creada *Price Manual*.

* Luego, en el apartado e los filtros, vamos a mandar a llamar a nuestra columna **Diferencia Precios** y solamente vamos a seleccionar los **TRUE()**

### Creacion del DropDrill

* Desde nuestra 2da pagina, en el aprtado de **Visualiztions** colocamos nuestra columna de la nueva tabla llamada *product_category*.

* Finalmente solo hacemos la prueba de que funcione dando click secundario a nuestra tabla erada en la pagina 1. 
































































