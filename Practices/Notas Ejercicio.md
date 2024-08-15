# Ejercicio de prueba

Primero hay que entender el ejercicio y los requerimientos necesarios para poder hacerlo,

Ahora solamente se va a hacer la descripcion de los pasos para poder llegar hasta el objetivo. 

### Relacion entre tablas

Lo primero que hay que ahcer es la relacion entre tablas, para ello es necesario

* Crear una nueva tabla con solamente los valores individuales de nuestra columna **product_category**, lo vamos a hacer mediante el uso del siguiente codigo 

``` Java
Individual Values = GROUPBY(SALES_DB, SALES_DB[product_category])
```

* Posteriormente tenemos que hacer la relacion como manda la regla, siempre buscando que sea de **UNO A MUCHOS**, para ello seleccionamos nuestra columna en la tabla y la arrastramos hasta nuestra tabla inicial, siempre revisando ue la relacion sea Uno a Muchos, y hacemos lo mismo con la otra tabla. 








