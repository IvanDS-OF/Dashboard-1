# Title of the repo


## Projects


## Interesting use of DAX in the projects

### Trabajo con Variables
Es posible hacer medidas en donde tengamos dentro a variables. Es necesario tener en cuenta las palabras claves VAR y RETURN
Ejemplo: 

``` DAX
Differencia importe con variables = 
    VAR vImporte = SUMX( Ventas, Ventas[Cantidades] * Ventas[Precios] ) 
    VAR vImporteCat = SUMX( Ventas, Ventas[Cantidades] * RELATED(Producto[Precio Catalogo]) )
RETURN
    vImporteCat - vImporte
```

### Como crear un calendario para los filtros

``` DAX
CalendarioDAX = 
ADDCOLUMNS(
	CALENDAR(
	DATE (2021, 1, 1),
	DATE (2022, 12, 31)
	),
"AñoDAX", YEAR([Date]),
"MesDAX", FORMAT([Date], "mmmm"), 
"DiaDAX", FORMAT([Date], "dddd")
)
```

### Filtros con CALCULATE
``` DAX
CALCULATE(
	[Cantidad clientes],
	CROSSFILTER(Ventas[IdCliente], Clientes[IdClientes], BOTH)
)
```





## Documentation structure



## Resources


## Some Images of the project


## Contact 

Eng. Ivan Duran

