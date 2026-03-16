saldo = 0

while True:
    print("\n=== SISTEMA BANCÁRIO ===")
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print(f"Seu saldo é: R${saldo}")

    elif opcao == "2":
        valor = float(input("Digite o valor para depositar: "))
        saldo += valor
        print(f"Depósito realizado! Novo saldo: R${saldo}")

    elif opcao == "3":
        valor = float(input("Digite o valor para sacar: "))
        if valor <= saldo:
            saldo -= valor
            print(f"Saque realizado! Novo saldo: R${saldo}")
        else:
            print("Saldo insuficiente!")

    elif opcao == "4":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!")