def peso_total( peso_ant ):
  total_peso = 0
  
  for peso in range( 1, 9 + 1 ):
    peso = float( input( f'Peso bascula { peso }: ' ) )

    total_peso += peso

  prom = total_peso / 10
  diferencia = prom - peso_ant

  if diferencia > 0:
    print('Subio')
  if diferencia < 0:
    print('Bajo')


for n in range( 1 ):
  peso_ant = float(input('Peso primera reunion: '))
  peso_total( peso_ant )