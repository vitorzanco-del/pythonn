#ex 5 : — Minutos em horas Leia uma quantidade
#  e mostre quantas horas e quantos
#  minutos ela representa.
# entrada:#135 	saida esperada : 2 hora(s) e 15 minuto(s)  
#Dica: use a divisão inteira para as horas e o resto da 
# divisão (%) para os minutos. 
print ("escreva a qunatidade de minutos ")

minutos_totais = 135

# Cálculos
horas = minutos_totais // 60
minutos_restantes = minutos_totais % 60


print(f"{horas} hora(s) e {minutos_restantes} minuto(s)")