# aqui o  usuario vai digitar o dividendo o programa vai guardar o numeoro
dividendo = float(input("Digite o dividendo: "))

# aqui o usuario vai digitar o divisor o programa vai guardar o numero
divisor = float(input("Digite o divisor: "))
 
# aqui vai testar se o divisor é zero
if divisor == 0:
    # aqui vai mostrar a mensagem de erro caso o divisor seja zero
    print("Erro: não existe divisão por zero")
# se o usuario digitar um divisor diferente de zero o programa vai calcular a divisão
else:
    # aqui é o calcula o resultado da divisão
    resultado = dividendo / divisor
    # aqui vai mostar o resultado para o usuario
    print("Resultado:", resultado)