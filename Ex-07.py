ponto_a = float(input('Informe a posição inicial do trecho: '))
ponto_b = float(input('Informe a posição final do trecho: '))
velocidade= int(input('Informe a velocidade do veículo em km/h: '))

tempo= (ponto_b - ponto_a) / velocidade

print (tempo)