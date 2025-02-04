"""
Iterando strings com while
"""
#       012345678910

"""nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
print(nome[3])

nova_string = ''
nova_string += '*L*u*i*z* *O*t*á*v*i*o'"""

nome = 'Luiz Otávio'
indice = 0
nome_novo =''

while indice < len(nome):
    letra = nome[indice]
    nome_novo += f'&{letra}'
    indice += 1
    
nome_novo += '&'
print(nome_novo)
    