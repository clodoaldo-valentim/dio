# Inicialização das variáveis
saldo = 0.0
depositos = []
saques = []
saques_diarios = 0

def deposito(valor):
    global saldo, depositos
    if valor > 0:
        saldo += valor
        depositos.append(f"Depósito de R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor de depósito inválido. Por favor, tente novamente.")

def saque(valor):
    global saldo, saques, saques_diarios
    if saques_diarios < 3 and valor <= 500.00 and valor <= saldo:
        saldo -= valor
        saques.append(f"Saque de R$ {valor:.2f}")
        saques_diarios += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    elif saques_diarios >= 3:
        print("Você já realizou 3 saques diários. Por favor, tente novamente amanhã.")
    elif valor > saldo:
        print("Saldo insuficiente. Por favor, tente novamente.")
    else:
        print("Valor de saque inválido. Por favor, tente novamente.")

def extrato():
    global depositos, saques, saldo
    if not depositos and not saques:
        print("Não foram realizadas movimentações.")
    else:
        print("Extrato da conta:")
        for movimento in depositos + saques:
            print(movimento)
        print(f"Saldo atual: R$ {saldo:.2f}")

# Menu do sistema
while True:
    print("Menu:")
    print("1. Depósito")
    print("2. Saque")
    print("3. Extrato")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        deposito(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        saque(valor)
    elif opcao == "3":
        extrato()
    elif opcao == "4":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")