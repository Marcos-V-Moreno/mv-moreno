"""
Calculo do primeiro dígito do CPF
CPF: 37050557803
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  3   7  0  5  0  5  5  7  8
   30  63 0  35 0  25 20 21 16

Somar todos os resultados: 
210
Multiplicar o resultado anterior por 10
210 * 10 = 2100
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 9
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 0
"""

#cpf_enviado_usuario = '21569125805'
#nove_digitos = cpf_enviado_usuario [:9]

#print(nove_digitos)

import random
import sys

for _ in range (100):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))


    contador_regressivo_1 = 10

    resultado_digito_1 = 0
    for digito_1 in nove_digitos:
        resultado_digito_1 += int(digito_1) * contador_regressivo_1
        contador_regressivo_1 -= 1
    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11

    resultado_digito_2 = 0
    for digito in dez_digitos:
        resultado_digito_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

    print (cpf_gerado_pelo_calculo)