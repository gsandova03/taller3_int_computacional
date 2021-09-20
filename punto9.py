def cominsion():
  for n in range( 1, 100 + 1 ):
    venta = float( input(f'Ventas realizadas empleado { n }: ') )

    if venta <= 200000000:
      comision = venta * 0.10
      print( f'Comision por ventas empleado {n}, { comision }' )

    if venta >= 200000000 and venta <= 400000000:
      comision = venta * 0.15
      print( f'Comision por ventas empleado {n}, { comision }' )

    if venta >= 400000000 and venta <= 800000000:
      comision = venta * 0.20
      print( f'Comision por ventas empleado {n}, { comision }' )

    if venta >= 800000000 and venta <= 1600000000:
      comision = venta * 0.25
      print( f'Comision por ventas empleado {n}, { comision }' )

    if venta > 1600000000:
      comision = venta * 0.30
      print( f'Comision por ventas empleado {n}, { comision }' )



cominsion()