def ganador():

  candidato_1 = 0
  candidato_2 = 0
  candidato_3 = 0

  for n in range(1, 10 + 1):
    voto = int( input('1. Candidato 2. Candidato y 3. Candidato: ') )
    if voto == 1 :
      candidato_1 += 1

    if voto == 2 :
      candidato_2 += 1

    if voto == 3 :
      candidato_3 += 1

  if candidato_1 > candidato_2 and candidato_1 > candidato_3: 
    print('El ganador es candidato 1')
  if candidato_2 > candidato_1 and candidato_2 > candidato_3: 
    print('El ganador es candidato 2')
  else:
    print('El ganador es candidato 3')

