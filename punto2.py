animal = int( input(' 1. para Elefante , 2. para Jirafas y 3. para Chimpances:  ') )

if( animal == 1 ):
  edad_total = 0
  elefante_total = 20
  for n in range( 1, elefante_total + 1 ):
    edad = int( input(f'Edad animal { n }: ') )
    edad_total += edad

  promedio = edad_total / elefante_total

  print(f'Promedio de edad de elefantes { promedio }')


if( animal == 2 ):
  edad_total = 0
  jirafas_total = 15
  for n in range( 1, jirafas_total + 1 ):
    edad = int( input(f'Edad animal { n }: ') )
    edad_total += edad

  promedio = edad_total / jirafas_total

  print(f'Promedio de edad de jirafas { promedio }')

if( animal == 3 ):
  edad_total = 0
  chimpance_total = 40
  for n in range( 1, chimpance_total + 1 ):
    edad = int( input(f'Edad animal { n }: ') )
    edad_total += edad

  promedio = edad_total / chimpance_total

  print(f'Promedio de edad de chimpances { promedio }')

else:
  print('Numero no valido')
