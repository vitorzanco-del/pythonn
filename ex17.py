# aqui o usuario vai digitar o numeore o programa vai lê o número digitado
numero = float(input("Digite um número: "))
 
# aqui vai testar se o numero é maior que zero
if numero > 0:
    # se for positivo vai dar a mensagem de positivo
    print("Positivo")

# aqui vai testar se o numero é menor que zero
elif numero < 0:
    print("Negativo")

# se o numero for igual a zero vai dar a mensagem de zero
else:
    print("Zero")
 