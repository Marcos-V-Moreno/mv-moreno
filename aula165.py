from datetime import date, timedelta

# Dados do empréstimo
valor_emprestimo = 1000000
data_emprestimo = date(2020, 12, 20)
anos_pagamento = 5

# Calcula a data final do empréstimo
data_final_emprestimo = date(data_emprestimo.year + anos_pagamento, data_emprestimo.month, data_emprestimo.day)

# Calcula o valor de cada parcela
valor_parcela = valor_emprestimo / (anos_pagamento * 12)

# Exibe as datas de vencimento e o valor de cada parcela
print("Data do empréstimo:", data_emprestimo)
print("Data final do empréstimo:", data_final_emprestimo)
print("\nDatas de vencimento e valor das parcelas:")

data_vencimento = data_emprestimo

for _ in range(anos_pagamento * 12):
    print(data_vencimento.strftime("%d/%m/%Y"), "- R$", valor_parcela)
    data_vencimento += timedelta(days=30)  # Adiciona 30 dias para a próxima data de vencimento
    # Ajusta o dia do mês para o dia 20, se necessário
    if data_vencimento.day != 20:
        data_vencimento = data_vencimento.replace(day=20)

