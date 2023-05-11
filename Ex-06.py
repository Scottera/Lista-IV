0

totaldaconta = float(input('Informe o valor da conta:'))
valorfornecido = float(input('Informe o valor fornecido pelo usuário:'))
troco = valorfornecido - totaldaconta

print(f'O valor do troco é de {troco:.2f}')

trocoCom100=int(troco/100)
print(f'O número de cédulas de R$ 100,00 fornecidas para o troco são: {trocoCom100} cédulas')

troco = troco - (trocoCom100*100)
trocoCom10=int(troco / 10)
print(f'O número de cédulas de R$ 10,00 fornecidas para o troco são: {trocoCom10} cédulas')

trocoCom1= int(troco - (trocoCom10*10))
print(f'O número de cédulas de R$ 1,00 fornecidas para o troco são: {trocoCom1} cédulas')





