def descuentos( valor_boleto ):
  num_clientes = 10
  total_perdida_desc = 0
  for n in range( num_clientes ):
    edad = int( input('Edad cliente: ') )

    if edad >= 5 and edad <= 14:
      desc = valor_boleto * 0.35
      total_perdida_desc += desc

    if edad >= 15 and edad <= 19:
      desc = valor_boleto * 0.25
      total_perdida_desc += desc

    if edad >= 20 and edad <= 45:
      desc = valor_boleto * 0.10
      total_perdida_desc += desc

    if edad >= 46 and edad <= 65:
      desc = valor_boleto * 0.25
      total_perdida_desc += desc

    if edad >= 66:
      desc = valor_boleto * 0.35
      total_perdida_desc += desc

  print(f'Perdidas en descuentos { total_perdida_desc }')




valor_boleto = float( input('Valor boleto: ') )
descuentos( valor_boleto )