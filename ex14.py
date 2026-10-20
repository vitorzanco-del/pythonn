# aqui o usuario vai digitar a velocidade do carro e o programa vai guardar a velocidade
Velocidade = float(input("velocidade: "))
# aqui vai testar se a velocidade é maior que 80 km/h
if Velocidade > 80 :
    
    # aqui vai mostrar a mensagem de que o usuario passou do limite de velocidade
    print("Muita! Você passou de 15 km/h d limite.")

    #se o usuario passou do limite de velocidade o programa vai dar multa
else:
    print("velocidade dentro do limite . boa viagem! ")