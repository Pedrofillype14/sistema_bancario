def sacar(saldo, valor):
  """
  Função para realizar saque em conta bancária.

  Args:
    saldo: Saldo atual da conta.
    valor: Valor a ser sacado.

  Returns:
    Novo saldo da conta após o saque.
  """
  if valor > saldo:
    print("Saldo insuficiente para saque.")
    return saldo
  else:
    saldo -= valor
    print(f"Saque de R${valor:.2f} realizado com sucesso.")
    print(f"Novo saldo: R${saldo:.2f}")
    return saldo

def depositar(saldo, valor):
  """
  Função para realizar depósito em conta bancária.

  Args:
    saldo: Saldo atual da conta.
    valor: Valor a ser depositado.

  Returns:
    Novo saldo da conta após o depósito.
  """
  saldo += valor
  print(f"Depósito de R${valor:.2f} realizado com sucesso.")
  print(f"Novo saldo: R${saldo:.2f}")
  return saldo

def visualizar_extrato(saldo, extrato):
  """
  Função para visualizar o extrato da conta bancária.

  Args:
    saldo: Saldo atual da conta.
    extrato: Lista de transações (depósitos e saques).
  """
  print("### Extrato Bancário")
  print(f"Saldo atual: R${saldo:.2f}")
  print("-" * 20)
  for transacao in extrato:
    print(f"{transacao['data']}: {transacao['tipo']}: R${transacao['valor']:.2f}")
  print("-" * 20)

# Inicialização de variáveis
saldo = 1000.00
extrato = []

# Loop principal do sistema bancário
while True:
  # Menu de opções
  print("""
  **Sistema Bancário**

  Escolha uma opção:

  1. Sacar
  2. Depositar
  3. Visualizar Extrato
  4. Sair
  """)

  opcao = int(input("Digite a opção desejada: "))

  # Validação da opção
  if opcao not in range(1, 5):
    print("Opção inválida. Digite um número entre 1 e 4.")
    continue

  # Execução da opção escolhida
  if opcao == 1:
    valor = float(input("Digite o valor a ser sacado: "))
    saldo = sacar(saldo, valor)

  elif opcao == 2:
    valor = float(input("Digite o valor a ser depositado: "))
    saldo = depositar(saldo, valor)

  elif opcao == 3:
    visualizar_extrato(saldo, extrato)

  else:
    print("Obrigado por utilizar o Sistema Bancário!")
    break