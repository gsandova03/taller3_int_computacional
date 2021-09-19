
num_carros = int( input( 'Numero de carros: ' ) )

cant_amarillo = 0
cant_rosa = 0
cant_rojo = 0
cant_verde = 0 
cant_azul = 0 

for carro in range( 0, num_carros ):
  ultimo_num = int( input( "Ultimo numero de matricula: " ) )

  if( ultimo_num == 1 or ultimo_num == 2 ):
    cant_amarillo += 1
  if( ultimo_num == 3 or ultimo_num == 4 ):
    cant_rosa += 1
  if( ultimo_num == 5 or ultimo_num == 6 ):
    cant_rojo += 1
  if( ultimo_num == 7 or ultimo_num == 8 ):
    cant_verde += 1
  if( ultimo_num == 9 or ultimo_num == 0 ):
    cant_azul += 1

print( f' Amarillo: { cant_amarillo }, Rosa: { cant_rosa }, Rojo: { cant_rojo }, Verde: { cant_verde } y Azul: { cant_azul } ' )



