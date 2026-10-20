# aqui é a variável senha_correta q esta a senha "correta"
senha_correta = "senai2026"
 
# aqui vai ler para verificar se a senha digitada pelo usuario é a mesma que a senha_correta
senha = input("Digite a senha: ")
 
#aqui vai comparar se a senha digitada pelo usuario é a mesma que a senha_correta
if senha == senha_correta:
    # se a senha for correta vai mostrar a mensagem de acesso liberado
    print("Acesso liberado")
# Caso o restante da der senha errada
else:
    # vai mostrar a mensagem de acesso negado
    print("Acesso negado")