# O usuário vai digitar um número de 1 a 7 e o programa vai mostrar o dia da semana correspondente
dia = int(input("Digite um número de 1 a 7: "))

# vai verificar qual é o dia da semana ao número digitado para ver se é domingo, 
# segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira ou sábado de acordo com o número digitado pelo usuário
if dia == 1:
    print("domingo")
elif dia == 2:
    print("Segunda-feira")
elif dia == 3:
    print("Terça-feira")
elif dia == 4:
    print("Quarta-feira")
elif dia == 5:
    print("Quinta-feira")
elif dia == 6:
    print("Sexta-feira")
elif dia == 7:
    print("sábado")
else:
    print("Dia inválido")