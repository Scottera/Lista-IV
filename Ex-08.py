clisempendencia = int(input('Informe a quantidade de clientes sem pendências:'))
cliemdia = int(input('Informe a quantidade de clientes com as parcelas em dia:'))
cliematraso = int(input('Informe a quantidade de clientes com parcelas em atraso:'))

totaldeclientes = cliemdia + cliematraso + clisempendencia

print('O Total de clientes é:', totaldeclientes)

totalsempendencia = (clisempendencia/totaldeclientes) * 100
totalemdia = (cliemdia/totaldeclientes) * 100
totalematraso = (cliematraso/totaldeclientes) * 100

print (f'O total de clientes sem pendências é de: {totalsempendencia:.2f}%')
print (f'O total de clientes com parcelas em dia é de: {totalemdia:.2f}%')
print (f'O total de clientes com parcelas em atraso é de: {totalematraso:.2f}%')
