#o usuario vai digitar duas notas e o programa vai ler as notas digitadas
nota1 = float(input("Digite a primeira nota: "))

#o usuariovai ler a segunda nota
nota2 = float(input("Digite a segunda nota: "))
 
#aqui o calculo da media vai ser feito somando as duas notas e dividindo por 2
media = (nota1 + nota2) / 2
 
#vai verificar se a media é maior ou igual a 7.0, se for vai mostrar a mensagem de aprovado
if media >= 7.0:
    print("Média", media, "— Aprovado")

#vai verificar se a media é maior ou igual a 5.0, se for vai mostrar a mensagem de recuperação
elif media >= 5.0:
    print("Média", media, "— Recuperação")
    
#se a media for menor que 5.0 vai mostrar a mensagem de reprovado
else:
    print("Média", media, "— Reprovado")