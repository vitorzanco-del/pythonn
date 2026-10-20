
# O usuário vai digitar a idade 
idade = int(input("Digite a idade: "))


# vai verificar se a idade é menor que 0, se for vai mostrar a mensagem de idade inválida, se não for vai verificar se
#  a idade é menor ou igual a 12, se for vai mostrar a mensagem de criança, se não for vai verificar se a idade é menor ou igual a 17,
#  se for vai mostrar a mensagem de adolescente, se não for vai verificar se a idade é menor ou igual a 59, se for vai mostrar a mensagem
#  de adulto, se não for vai mostrar a mensagem de idoso
if idade < 0:
    print("Idade inválida")
elif idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")