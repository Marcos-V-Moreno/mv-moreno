def verificar_par_impar():
  """Verifica se um número é par ou ímpar.

  Solicita ao usuário um número inteiro e informa se ele é par ou ímpar.
  Caso o usuário não digite um número inteiro, informa que o valor digitado não é válido.
  """

  while True:
    try:
      numero = int(input("Digite um número inteiro: "))
      if numero % 2 == 0:
        print(f"O número {numero} é par.")
      else:
        print(f"O número {numero} é ímpar.")
      break  # Sai do loop se o número for válido
    except ValueError:
      print("Você não digitou um número inteiro. Tente novamente.")

verificar_par_impar()

def saudar():
    """
    Pergunta a hora ao usuário e exibe a saudação apropriada.
    """

    while True:
        try:
            hora = int(input("Digite a hora (0-23): "))
            if 0 <= hora <= 23:
                if 0 <= hora <= 11:
                    print("Bom dia!")
                elif 12 <= hora <= 17:
                    print("Boa tarde!")
                else:
                    print("Boa noite!")
                break  # Sai do loop se a hora for válida
            else:
                print("Hora inválida. Digite um número entre 0 e 23.")
        except ValueError:
            print("Você não digitou um número válido. Tente novamente.")

saudar()

def classificar_nome():
  """Pede o primeiro nome do usuário e classifica seu tamanho."""

  nome = input("Digite seu primeiro nome: ")
  tamanho_nome = len(nome)

  if tamanho_nome <= 4:
    print("Seu nome é curto.")
  elif 5 <= tamanho_nome <= 6:
    print("Seu nome é normal.")
  else:
    print("Seu nome é muito grande.")


classificar_nome()