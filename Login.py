login1 = "procopio"
senha1 = "12345"

usuario2 = "paiva"
senha2 = "54321"

loginu1 = str(input("Digite usuário: "))
senhau1 = str(input("Digite a seha: "))

if loginu1 == login1 and senha1 == senhau1 or usuario2 == loginu1 and senha2 == senhau1:
    print("Login efetuado com sucesso")

else:
    print("Usuário e senha não conferem")