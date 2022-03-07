import random as rd 

print('iniciando o jogo de dados...')
dado1 = rd.randrange(1,6)
dado2 = rd.randrange(1,6)

soma = (dado1 + dado2)

print(f'o primeiro dado gerou o resultado {dado1}, já o segundo dado gerou o resultado {dado2}, resultando assim {soma}')

