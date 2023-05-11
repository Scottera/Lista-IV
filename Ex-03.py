# Sabe-se que para iluminar de maneira correta os cômodos de uma casa, para cada metro
# quadrado de área deve-se usar 18 watts de potência. Desenvolva um programa que receba as
# dimensões de dois lados de uma casa (em metros), calcule a área da casa (A = lado * lado), e
# mostre quantos watts serão necessários para iluminar corretamente esta casa.

ladoa = float(input('Informe o total de metros do Lado A:'))
ladob = float(input('Informe o total de metros do Lado B:'))

area= ladoa * ladob
totalwatts = area * 18

print(f'Para iluminar uma casa de {area:.0f}²m, são necessários {totalwatts:.2f} watts.')


