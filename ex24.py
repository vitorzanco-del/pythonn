# aqui o usuario vai digitar o peso e a altura 
peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))

# aqui é o calculo do imc
imc = peso / (altura * altura)

# aqui vai verificar se o imc é menor que 18.5, se for vai mostrar a mensagem de abaixo do peso, se não for vai verificar se
# o imc é menor que 25, se for vai mostrar a mensagem de peso normal, se não for vai verificar se o imc é menor que 30, se for vai 
# mostrar a mensagem de sobrepeso, se não for vai mostrar a mensagem de obesidade
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

# vai mostrar o imc arredondado para duas casas decimais e a classificação do imc
print(f"IMC: {round(imc, 2)} — {classificacao}")