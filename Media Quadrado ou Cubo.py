numero1 = int(input("Digite um numero positivo: "))
numero2 = int(input("Digite um numero positivo: "))

print("1 - Media ponderada, com pesos 2 e 3 respectivamente")
print("2 - Quadrado da soma dos 2 números")
print("3 - Cubo do menor numero")
print("Escolha uma opção")

opcao = int(input("Opção desejada: "))

if opcao == 1:
    media = float(numero1+numero2) / 2
    print(f"Média Ponderada: {media}")
    
elif opcao == 2:
    quadrado_soma = (numero1 + numero2) ** 2
    print(f"Quadrado da soma: {quadrado_soma}")
    
elif opcao == 3:
    if numero1 > numero2:
        cubo_menor = numero2 ** 3
        print(f"Cubo do menor: {cubo_menor}")
    else:
        cubo_menor = numero1 ** 3
        print(f"Cubo do menor: {cubo_menor}")
        
else:
    print("Opção informada inválida")