# o usuario  vai digitar dois números e o programa vai ler os números digitados 
a = int(input("Digite o primeiro número: "))
#vai fazer a mesca coisa com o segundo numero
b = int(input("Digite o segundo número: "))
 
# vai verificar se os números são iguais, se não forem vai verificar qual é o maior
if a == b:
    #vai mostrar a mensagem de que os números são iguais
    print("Os números são iguais")
# vai verificar se o primeiro número é maior que o segundo
elif a > b:
    # se o primeiro número for maior vai mostrar a mensagem de que o primeiro número é maior
    print("O maior é", a)
    
# se o segundo número for maior vai mostrar a mensagem de que o segundo número é maior
else:
    print("O maior é", b)