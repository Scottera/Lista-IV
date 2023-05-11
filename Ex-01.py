# 1) Desenvolva um programa que receba do usuário um valor numérico inteiro x e retorne como
# saída o resultado da seguinte fórmula: x² + 10x - 5

x = int(input('Informe o valor para X: '))
total = (x * x) + 10 * x -5

print (f'O resultado da equação descrita no exercício é: {total:.2f}')