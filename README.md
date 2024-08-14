# Notes of the project


## Projects
Dashboard de prueba

Dashboard con información ficticia



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

### Interesante - Cómo crear una medida de Media Movil usando DAX

Cómo hacer un análisis de media movil, Una Media movil se puede ver de diferentes formas, una es desde el punto de vista de control que puede ser un filtro, otra es desde estadística que se puede tomar como un suavizado
Lo que hace el filtro de Media movil básicamente es, por cada cierta cantidad de valores datos, va a devolver el promedio, esto sirve más ddentro de un visual que dentro de una tabla. Igualmente sirve bastante para hacer análisis de información de pronóstico sin tantos datos pero que de igual forma sean fieles a la estructura general de la información. 


``` Java
Media Movil 10 dias = 
VAR UltimosDias = CALCULATETABLE(
	DATESINPERIOD(
	Calendario[Fecha], 
	MAX( Calendario[Fecha] ), 
	-10, 	//Es el paso de tiempo en Dias
	DAY	//Aqui se especifica que es en días
	)
)
VAR Inicio = CALCULATE( MIN( Ventas[Fecha] ), REMOVEFILTERS )
RETURN IF(
	Inicio <= MINX( UltimosDias, Calendario[Fechas] ), 
	AVERAGEX( UltimosDias, [Cantidad] )
)
```



## Documentation structure

### Portada
* Title:
* Owner:
* Function:
* Date:
* Developer:

### Función - Cliente - Negocio
* Draft
* Source information (Each of data source, from Excel, SQL, Sharepoint)

| Source | Process | Special process | Owner | Final Storage | 
| --- | --- | --- | --- | --- |
| Product owner Onedrive Folder, Data.xlsx | Descriptio, how to upload the information | The Dashboard will be updated everyday at 8:00 hrs | Product Owner | Teams Folder |


* Questions the Dashboard will answer
* Brief Description and Purpose

### Technical stuff
* Data flow architecture
* Information needed

| Name | Source |
| --- | --- |
| Projects | Data.xlsx |
| --- | --- |
| Status | Data.slsx |
| --- | --- |
| Calendar | DAX measure |
| --- | --- |
| Average Filter | DAX Column |
| --- | --- |
| Saving Sorted | Python script |



* Steps
* Measures

| Name | Photo | DAX Code + Description  |
| --- | --- | --- | 
| Average Filter | * Photo | ``` DAX Code ``` : This takes the Speed of the team and creates an Average Filter for better visualisation  |



* Columns
* Visuals (all of them in a table with)

| Name | Type of Visual | Filters | Source information  |
| --- | --- | --- | --- |
| Quantity of projects in Progress | Card | Status = In Progress | Data.xlsx |


### Signs
* Project Manager
* Product Owner
* Other - Requester




## Resources

I have been taken most of the information from this Linkedin Learning course: 

[PowerBI: Modelado de datos con DAX por Ana Maria Bisbé York](https://www.linkedin.com/learning/power-bi-modelado-de-datos-con-dax)


## Some Images of the project


## Contact 

Eng. Ivan Duran

