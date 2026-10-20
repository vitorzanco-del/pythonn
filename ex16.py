#aqui o usuario vai digitar o saldo da conta e o valor do saque e o programa vai guardar os valores
saldo = float(input("Digite o saldo da conta: R$ "))
# aqui vai ler o valor do saque que o usuario quer fazer
saque = float(input("Digite o valor do saque: R$ "))
 
# aqui vai testar se o saldo é maior ou igual ao valor do saque 
if saque <= saldo:
    # aqui vai calcular o novo saldo subtraindo o valor do saque do saldo atual
    novo_saldo = saldo - saque
    # aqui vai mostrar a mensagem de que o saque foi realizado e o novo saldo
    print("Saque realizado. Novo saldo: R$", novo_saldo)

else:
    # senao vai mostrar a mensagem de que o saldo é insuficiente
    print("Saldo insuficiente")