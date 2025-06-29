qntd100 = int(input("Digite a quantidade de cédulas de R%100,00: "))
qntd50 = int(input("Digite a quantidade de cédulas de R%50,00: "))
qntd20 = int(input("Digite a quantidade de cédulas de R$20,00: "))
qntd10 = int(input("Digite a quantidade de cédulas de R$10,00: "))
saldo = int(input("Digite o seu saldo: "))

while True:
    saque = int(input("Digite o valor do saque: "))
    if saque > saldo:
        print("Ops, algo deu errado!\nSaldo insuficiente.\n")
        continue
    resto = saque
    cd100 = resto//100
    resto = resto%100
    cd50 = resto//50
    resto = resto%50
    cd20 = resto//20
    resto = resto%20
    cd10 = resto//10
    resto = resto%10
    if resto == 0 and  cd100<=qntd100 and cd50<=qntd50 and cd20<=qntd20 and cd10<=qntd10:
        print(f"Transação concluída!\nVocê receberá {cd100} notas de R$100,00; {cd50} notas de R$50,00; {cd20} notas de R$20,00; {cd10} notas de R$10,00.")
        qntd100 = qntd100 - cd100
        qntd50 = qntd50 - cd50
        qntd20 = qntd20 - cd20
        qntd10 = qntd10 - cd10
        print(f"Cédulas disponíveis:\nR$100,00 = {qntd100}.\nR$50,00 = {qntd50}.\nR$20,00 = {qntd20}.\nR$10,00 = {qntd10}.\n")
        saldo=saldo-saque
        print(f"Saldo atual: {saldo}\n")
    else:
        print("Ops, algo deu errado!\nValor para saque inválido.\n")
    continuar = int(input("Continuar sacando? (1 para continuar)"))
    if continuar !=1:
            break