"""
Cálculo do primeoro dígito do CPF (depois do traço)

CPF: 745.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF multiplicando cada um dos valores por uma contaem regressiva começando de 10

746.824.890-70

10   9   8   7   6   5   4   3   2
7    4   6   8   2   4   8   9   0
70   36  48  56  12  20  32  27  0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301

Multiplicar o resultado por 10
301 * 10 = 3010

Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7

Se o resultado anterior é maior que 9 = 0
Senão é o valor da conta

O primeiro dígito do cpf é 7
"""

cpf1 = '74682489070'

nove_digitos = cpf1[:9]
contador_regressivo1 = 10

resultado1 = 0
for digito1 in nove_digitos:
    resultado1 += int(digito1) * contador_regressivo1
    contador_regressivo1 -= 1
    
digito1 = (resultado1 * 10) % 11
digito1 = digito1 if digito1 <= 9 else 0
print(digito1)

#--------------------------------------------------------------#
# Calculando o segundo dígito, incuindo o último dígito gerado, e a contagem regressiva inciada por 11

cpf2 = '746.824.890-70' \
    .replace('.', '') \
    .replace('-', '')

dez_digitos = cpf2[:9] + '7'
contador_regressivo2 = 11

resultado2 = 0
for digito2 in dez_digitos:
    resultado2 += int(digito2) * contador_regressivo2
    contador_regressivo2 -= 1
    
digito2 = (resultado2 * 10) % 11
digito2 = digito2 if digito2 <= 9 else 0
print(digito2)

cpf_gerado = f'{nove_digitos}{digito1}{digito2}'

if cpf1 == cpf_gerado:
    print('CPF Válido')
else:
    print('CPF inválido')