num_obreros = int( input('Numeros de obreros: ') )
salarios = []

for n in range( 1, num_obreros + 1 ):
  horas = int( input('Horas trabajadas: ') )

  if( horas <= 40 ):
    pago = horas * 20

    salarios.append( pago )
  elif( horas > 40 ):
    pago = 40 * 20
    horas_extra = horas - 40
    pago_extra =int( horas_extra * 25 )

    pago_total = pago + pago_extra
    salarios.append( pago_total )

print( salarios )
