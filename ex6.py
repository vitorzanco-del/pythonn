#Exercício 6 — Compra na cantina 
#Leia o preço de um lanche, a quantidade comprada e 
# o valor que o cliente pagou. Mostre o total da compra 
# e o troco.Considere que o valor pago é sempre suficiente. 
#Entrada: preço 4.50, quantidade 3, valor pago 
#20.00 
#saida esperadaTotal: R$ 13.5 Troco: R$ 6.5 
preco = float(input ("preco do lanche : "))
quantidade = int(input("quantidade: "))
pago = float (input ("valor pago : "))
#preco * quantidade 
total = preco * quantidade
troco = pago - total

print ("total: R$", total)
print("troco:R$", troco)