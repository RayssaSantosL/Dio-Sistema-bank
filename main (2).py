#menu formatado linha por linha 
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair 

=> """


#variaveis

saldo = 0
limite = 500
extrato = ""
numero_saques = 0 
LIMITE_SAQUES = 5 #limite saques diários (valor alterado/ diferente do da aula)


#SISTEMA

while True:
  #DEPÓSITO 
  opcao = input(menu)
  if opcao == "d":
    valor = float(input("Informe valor do déposito: "))
    if valor > 0:
      saldo += valor
      extrato += f"Déposito: R${valor:.2f}\n"
    else: 
      print ("Operação falhou. O valor informado é inválido.")

  #SAQUE 
  elif opcao == "s":
    valor = float(input("Informe valor do saque: "))
    # se o saque for maior que o saldo
    excedeu_saldo = valor > saldo

  #se o valor for maior que o  limite permitido (500)
    excedeu_limite = valor > limite

  #se passar da quantidade de saques permitida (3)
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
      print("Operação falhou. Você não tem saldo suficiente para concluir a operação.")

    elif excedeu_limite:
      print("Operação falhou. O valor do saque excede o limite.")

    elif excedeu_saques:
      print("Operação falhou. Número máximo de saques excedido.")

    elif valor > 0:
      saldo -= valor
      extrato += f"Saque: R${valor:.2f}\n"
      numero_saques += 1

    else: 
      print ("Operação falhou! O  valor informado é inválido.")

  #EXTRATO
  elif opcao ==  "e":
    print("\n============EXTRATO============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=================================")


  #SAIR 
  elif opcao == "q":
    break
  else: 
    print("Operação inválida, por favor selecione novamente a operação desejada.")
    