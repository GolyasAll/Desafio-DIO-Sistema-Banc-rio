menu = """

[D] Depósitar
[S] Sacar
[E] Extrato
[Q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao.lower() == "d":
        valor = float(input("Digite o valor a ser depositado: "))
        if valor > 0:
            print("Operação realizada com Sucesso!\n Depositando...")
            saldo += valor
            extrato += f"Depósito +: R$ {valor:.2f}\n"
        else:
            print("Valor inválido.")

    elif opcao.lower() == "s":
        valor = float(input("Digite o valor que deseja sacar:"))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação Falhou!\n Seu saldo é insuficiênte para esta operação.")

        elif excedeu_limite:
            print("Operação Falhou!\n Você excedeu o limite diário para saques.")

        elif excedeu_saques:
            print("Operação Falhou!\n Você excedeu o limite de saques diários.")

        elif valor > 0:
            saldo -= valor
            print("Operação realizada com Sucesso!\n Sacando...")
            extrato += f"Saque -: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Valor inválido para saque.")

    elif opcao == "e":
        print("\nExtrato:")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo : R$ {saldo:.2f}")
        print("-" * 50)

    elif opcao == "q":
        break

    else:
        print("Operação inválida.")

print("Agratos, volte sempre! :)")
