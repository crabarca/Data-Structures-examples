## Tips
ls

*Punteros*


char text = 'mama'


char *puntero; // crea un puntero de tipo char

puntero = &text; // guarda la direccion de memoria de text en el puntero. OJO: se guarda segun el largo del tipo de datos que estemos usando


#### MALLOC
puntero = (int *)malloc(sizeof(int)*4); // Devuelve un puntero de tipo int, a la primera posicion.

- malloc inicializa el array vacio, calloc lo inicializa con 0s

- 