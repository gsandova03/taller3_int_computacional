def total_compra():
  articulos = []
  total_compra = 0

  for n in range( 1, 5+1 ):
    precio = float( input(f'Precio articulo { n }: ') )
    articulos.append( precio )

  for articulo in articulos:
    cantidad = int( input(f'Cantidad del articulo { articulo }: ') )
    total = articulo * cantidad
    total_compra += total 
  
  print( total_compra )

total_compra()