saldo = 0

while True:
    print("===Menu====")
    print("1- Depositar")
    print("2- Sacar")
    print("3- Ver saldo")
    print("0- Sair")

    opcao = int(input("Escolha uma opção"))

    if opcao == 1:
        valor = float(input("Valor do deposito: "))
        saldo += valor
        print("Depósito realizado! Saldo atual:", saldo)

    elif opcao == 2:
        valor = float(input("Valor do saque: "))
        if valor <=saldo:
            saldo -= valor 
            print("Saque realizado! Saldo atual", saldo)
        else:
            print("saldo insuficiente!")

    elif opcao == 3:
        print("Saldo atual: ",saldo)

    elif opcao == 0:
        print("Saindo do sistema... ")

    else:
        print("Opção inválida, tente novamente.")