
menu = '''
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> '''

saldo = 1200
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
tchau = "\U0001F44B"
abraço = "\U0001F917"

print("Bem-vindo ao Banco Digital InnovationOne!\n")

sair = False

while not sair:

  print("\nQual operação você deseja fazer? ")
  opcao = input(menu)

  if opcao == "1":
    valor_deposito = float(input("\nQuanto deseja depositar? "))
    saldo += valor_deposito
    extrato = extrato + [f"Depósito: R${valor_deposito:.2f}"]


  elif opcao == "2":
    valor_saque = float(input("\nQuanto deseja sacar? "))

    if numero_saques >= LIMITE_SAQUES:
        print("Limite de saques diários excedido. ")
    elif valor_saque > limite:
        print("Valor excede o limite por saque. ")
    elif saldo < valor_saque:
        print("Saque negado! Seu saldo é insuficiente. ")
    else:
      saldo -= valor_saque
      extrato = extrato + [f"Sacado: R${valor_saque:.2f}"]
      numero_saques += 1


  elif opcao == "3":
    if not extrato:
      print("Não foram realizadas movimentações.")
    else:
      print("Extrato: ")
      for operacao in extrato:
        print(operacao)
      print(f"Saldo: R${saldo:.2f}")


  elif opcao == "4":
    print(f"\nBanco Digital InnovationOne: Mais do que um banco, somos uma família!{abraço}\n Até logo! {tchau}")
    sair = True


  realizar_outra_operacao = input("\nDeseja realizar outra operação? (S/N) ")
  if realizar_outra_operacao.upper() == "N":
        print(f"\nBanco Digital InnovationOne: Mais do que um banco, somos uma família!{abraço}\n Até logo! {tchau}")
        sair = True

