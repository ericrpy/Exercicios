numero1 = int(input("Informe o numero 1: "))
numero2 = int(input("Informe o numero 2: "))

if numero1 < numero2:
    soma = sum(range(numero1, numero2 +1))
    print(f"A soma dos números inteiros de {numero1} a {numero2} é: {soma}")
else:
    print("Erro: O valor de 'Numero 1' deve ser menor que 'Numero 2'.")

    