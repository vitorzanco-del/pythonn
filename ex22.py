# O usuário vai digitar a temperatura do dia e o programa vai mostrar uma mensagem de acordo com a temperatura digitada
temperatura = float(input("Digite a temperatura do dia (°C): "))

# vai verificar se a temperatura é menor que 0, se for vai mostrar a mensagem de que está abaixo de zero e há risco 
# de geada, se não for vai verificar se a temperatura é menor que 10, se for vai mostrar a mensagem de que está muito frio e o usuário 
# deve caprichar no agasalho, se não for vai verificar se a temperatura é menor que 18, se for vai mostrar a mensagem de que está frio, 
# se não for vai verificar se a temperatura é menor que 25, se for vai mostrar a mensagem de que está agradável, se não for vai mostrar a 
# mensagem de que está calor
if temperatura < 0:
    print("Abaixo de zero — risco de geada!")
elif temperatura < 10:
    print("Muito frio — capriche no agasalho")
elif temperatura < 18:
    print("Frio")
elif temperatura < 25:
    print("Agradável")
else:
    print("Calor")