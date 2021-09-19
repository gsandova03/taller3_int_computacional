cantidad_alumnos = int( input( 'Cantidad de alumnos: ' ) )

total_muj = 0
cont_muj = 0
total_homb = 0
cont_homb = 0

for n in range( 1, cantidad_alumnos + 1 ):

  g = int( input( '1. para Hombre y 2. para mujer' ) )

  if( g == 1 ):
    cont_homb += 1
    edad = int( input('Edad: ') )
    total_homb += edad
  
  if( g == 2 ):
    cont_muj += 1
    edad = int( input('Edad: ') )
    total_muj += edad

promedio_homb = total_homb / cont_homb
promedio_muj = total_muj / cont_muj
promedio_curso = ( total_muj + total_homb ) / ( cont_homb + cont_muj )

print(f' Promedio general { promedio_curso }, prom hombres: { promedio_homb } y prom mujeres: { promedio_muj } ')
