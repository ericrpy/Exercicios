soma_preco = 0

medicamento = input("Medicamento: ")
preco = float(input("RS: "))

mais_barato = medicamento
menor_preco = preco

soma_preco += preco

for x in range(4):
    medicamento = input("Medicamento: ")
    preco = float(input("R$: "))
    if preco < menor_preco:
        menor_preco = preco
        mais_barato = medicamento
    soma_preco += preco
    
media = soma_preco / 5
print(f"{mais_barato} é o medicamento mais barato e custa R$ {menor_preco:.2f}.")
print(f"Média dos preços: R$ {media:.2f}.")