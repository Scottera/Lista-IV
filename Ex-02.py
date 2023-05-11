# Considere que para um consórcio sabe-se o número total de prestações, a quantidade de
# prestações pagas e o valor da prestação. Escreva um programa que determine o valor total pago
# pelo consorciado e o saldo devedor.

prestacoes= int(input('Informe o total de prestações: '))
valorprestacao = float(input('O valor de cada prestação é: '))
prestpagas = int(input('Informe quantas prestações já foram pagas: '))

totalpagoprestacoes = prestpagas * valorprestacao
prestrestantes = prestacoes - prestpagas
saldodevedor = prestrestantes * valorprestacao

print(f'O Valor total em que já foi pago referente às prestações é de R$: {totalpagoprestacoes:.2f} e o saldo que tenho à pagar ainda é: {saldodevedor:.2f}')


