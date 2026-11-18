# SISTEMA DE HOSPEDAGEM

# INICIO
print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")
print("Olá, seja bem-vindo(a) ao Hotel Pequena Larga")
print("≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡≡")

print("Faremos o seu cadastro")


# =========================
# VALIDACAO DE EMAIL
# =========================


while True:

    print("======================")
    email = input("Digite seu email: ").strip().lower()
    print("======================")

    partes = email.split("@")

    if email == "":
        print("Email vazio!")

    elif email.count("@") != 1:
        print("Tem que ter exatamente 1 @!")

    elif len(email) < 6:
        print("O seu email precisa ter pelo menos 6 caracteres!")

    elif len(email) > 40:
        print("O seu email precisa ter menos de 40 caracteres!")

    elif " " in email:
        print("Email não pode ter espaços!")

    elif partes[0] == "":
        print("Falta o nome antes do @!")

    elif partes[1] == "":
        print("Falta o domínio depois do @!")

    elif "." not in partes[1]:
        print("Falta o ponto depois do @!")

    else:
        dominio = partes[1].split(".")

        if dominio[0] == "":
            print("Você precisa colocar um domínio!")

        elif dominio[1] == "":
            print("Você precisa colocar o final do domínio!")

        else:
            print("Email válido!")
            break



# =========================
# VERIFICACAO DE NOME
# =========================

while True:

    nome = input("Qual o seu nome? ").strip()

    if nome == "":
        print("O seu nome não pode ficar em branco!")

    elif len(nome) < 3:
        print("O nome precisa ter pelo menos 3 caracteres!")

    elif any(letra.isdigit() for letra in nome):
        print("Seu nome não pode conter números!")

    else:
        print(f"Ok!, {nome}, cadastro concluído")
        break


# =========================
# VERIFICACAO DO DINHEIRO
# =========================

while True:

    try:

        dinheiro = float(input(f"Quantos R$ você tem, {nome}? "))

        if dinheiro >= 250:
            print(". . .")
            break

        else:
            print("Você não possui dinheiro suficiente!")

    except ValueError:
        print("Digite apenas números!")


# =========================
# TABELA DE PRECOS
# =========================

print("Tabela de preços:")
print("1 -> R$250.00")
print("2 -> R$500.00")
print("3 -> R$750.00")
print("4 -> R$1000.00")
print("5 ou mais -> Mais de R$1250.00")
print("7 dias é o máximo!")


# =========================
# ESCOLHA DA HOSPEDAGEM
# =========================

while True:

    try:

        print("Digite o número de dias que você gostaria de hospedar-se:")
        escolha = int(input())

        if escolha < 1:
            print("Você precisa escolher pelo menos 1 dia!")

        elif escolha > 7:
            print("O máximo permitido é 7 dias!")

        else:

            hospedagem = 250
            total = escolha * hospedagem

            if dinheiro < total:
                print("Você não possui dinheiro suficiente para essa hospedagem!")

            else:
                break

    except ValueError:
        print("Digite apenas números inteiros!")


# =========================
# PAGAMENTO INICIAL
# =========================

dinheiro = dinheiro - total


# =========================
# HOSPEDAGEM CONCLUIDA
# =========================

print("_____________________")

hospedagemm = [
    "Ok!",
    nome,
    "você está hospedado por",
    escolha,
    "dias"
]

Email = [email]

print(hospedagemm)

print(
    "Qualquer acontecimento, entraremos em contato por esse email:",
    Email
)

print(
    f"O seu dinheiro restante é de R${dinheiro:.2f}, "
    f"e você está hospedado por {escolha} dias"
)


# =========================
# CONTAGEM DE DIAS
# =========================

for dia_restante in range(escolha, 0, -1):

    dia_atual = escolha - dia_restante + 1

    print(
        f"Dia {dia_atual} de {escolha} "
        f"- Faltam {dia_restante} dia(s)"
    )


# =========================
# NOVA HOSPEDAGEM
# =========================

while True:

    print("____________________________")

    print("A SUA HOSPEDAGEM ACABOU!")
    print("Se quiser continuar, faça uma nova hospedagem.")

    print("Você quer se hospedar novamente?")

    desicao = input().strip().lower()

    if desicao == "nao" or desicao == "não":

        print("Obrigado por utilizar nosso hotel!")
        break

    elif desicao == "sim":

        # TABELA DE PRECOS
        print("Tabela de preços:")
        print("1 -> R$250.00")
        print("2 -> R$500.00")
        print("3 -> R$750.00")
        print("4 -> R$1000.00")
        print("5 ou mais -> Mais de R$1250.00")
        print("7 dias é o máximo!")


        # VERIFICACAO DOS DIAS
        while True:

            try:

                print(
                    "Digite o número de dias que você gostaria de hospedar-se:"
                )

                escolha = int(input())

                if escolha < 1:
                    print("Você precisa escolher pelo menos 1 dia!")

                elif escolha > 7:
                    print("O máximo permitido é 7 dias!")

                else:

                    hospedagem = 250
                    total = escolha * hospedagem

                    if dinheiro < total:
                        print("Você não possui dinheiro suficiente!")

                    else:
                        break

            except ValueError:
                print("Digite apenas números inteiros!")


        # ATUALIZACAO DO DINHEIRO
        dinheiro = dinheiro - total


        # CONFIRMACAO DA NOVA HOSPEDAGEM
        print("_____________________")

        hospedagemm = [
            "Ok!",
            nome,
            "você está hospedado por",
            escolha,
            "dias"
        ]

        print(hospedagemm)

        print(f"Valor da hospedagem: R${total:.2f}")

        print(f"Dinheiro restante: R${dinheiro:.2f}")


        # CONTAGEM DOS DIAS DA RENOVACAO
        for dia_restante in range(escolha, 0, -1):

            dia_atual = escolha - dia_restante + 1

            print(
                f"Dia {dia_atual} de {escolha} "
                f"- Faltam {dia_restante} dia(s)"
            )


    else:

        print("Digite apenas sim ou não!")


# =========================
# FIM DO SISTEMA
# =========================

print("____________________________")
print("Sistema de hospedagem encerrado.")
print(f"Obrigado pela preferência, {nome}!")
print(f"Saldo final: R${dinheiro:.2f}")
