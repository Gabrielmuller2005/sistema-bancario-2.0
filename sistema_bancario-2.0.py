def deposito (saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += (f"Depósito: R$ {valor:.2f}\n")
        print("Depósito realizado com sucesso!")
    
    else:
        print("A operação falhou! O valor informado é inválido.")

    return saldo, extrato


def saque (*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saldo:
        print("A operação falhou! Você não tem saldo suficiente.")
    
    elif excedeu_limite:
        print("A operação falhou! O valor excede o limite de saque.")

    elif excedeu_saques:
        print("A operação falhou! Você excedeu o limite de saque diário.")

    elif valor > 0:
        saldo -= valor
        extrato += (f"Saque: R$ {valor:.2f}\n")
        numero_saques += 1
        print("\nSaque realizado com sucesso!")
    
    else:
        print("A operação falhou! Valor inválido.")
    
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print(f"\nSeu saldo atual é de R$ {saldo:.2f}")
    print(f"\n {extrato}")
    
    return saldo, extrato

def criar_usuario(usuarios):
    cpf = input("Informe seu CPF (Somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n!!! Já existe um usuário com este CPF !!!")
        return
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe seu endereço (Rua, n° - Bairro - Cidade/UF): ")
    
    usuarios.append({ "cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco})

    print("======== Usuário criado com sucesso! ========")


def filtrar_usuario(cpf, usuarios):
    usuario_filtrado = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n==== Conta criada com sucesso! ====")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n!!! Usuário não encontrado! Processo de criação de conta encerrado. !!!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\n
            Agência: {conta["agencia"]}
            C/C: {conta["numero_conta"]}
            Titular: {conta["usuario"]["nome"]}
"""
        print("="*100)
        print(linha)



def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"
    saldo = 0
    limite_por_saque = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        print("""\n\n======= SISTEMA BANCÁRIO =======
            
    [1] DEPÓSITO
    [2] SAQUE
    [3] EXTRATO
    [4] NOVO USUÁRIO
    [5] NOVA CONTA
    [6] LISTAR CONTAS
    [0] SAIR     """)
        opcao = int(input("\nInforme a opção desejada: "))

        if opcao == 1:
            valor = float(input("Informe o valor que deseja depositar: R$ "))
            saldo, extrato = deposito(saldo, valor, extrato)

        elif opcao == 2:
            valor = float(input("Informe o valor que deseja sacar: R$ "))
            saldo, extrato, numero_saques = saque(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite_por_saque,
                numero_saques = numero_saques,
                limite_saques =  LIMITE_SAQUE,
            )
        
        elif opcao == 3:
            print("======== EXTRATO ========")
            saldo, extrato = exibir_extrato(saldo, extrato = extrato)
        
        elif opcao == 4:
            criar_usuario(usuarios)
        
        elif opcao == 5:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == 6:
            listar_contas(contas)
        
        elif opcao == 0:
            break

        else:
            print("Opção inválida! Tente novamente.")

main()




        



