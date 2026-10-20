# aqui o usuario vai digitar o valor da compra e o programa vai guardar o valor
valor = float(input("valor da compra"))
# aqui vai testar se o valor da compra é maior ou igual a 100
if valor>=100:
 #aqui vai verificar se o valor da compra é maior ou igual a 100 se for da desconto
 valor = valor * 0.9
# aqui vai mostrar o valor
print("valor final : R$", valor)
