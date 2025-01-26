erros = 0
while erros < 3:
    senha = int(input("Senha: "))
    if senha == 123456:
        print("Ola, você, Seja bem vindo ao nosso banco!")
        break
    else:
        erros +=1
        if erros < 3:
            print(f"Senha incorreta! Voce ainda tem {3 - erros} tentativas")
        else:
            print("Sua senha foi bloqueada! Vá até algum caixa")
            break