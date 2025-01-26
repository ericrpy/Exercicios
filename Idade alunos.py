idade = float(input("Idade do aluno: "))

'''Como não há nenhuma idade a ser comparada, neste momento, o primeiro
aluno tem a maior e a menor idade'''
menor = idade
maior = idade

soma_idade = 0
soma_idade += idade
cont = 1
while True:
    idade = float(input("Idade do aluno: "))
    if idade < 0:  # Quando idade menor que zero, laço será interrompido
        break

    if idade < menor:
        menor = idade
    elif idade > maior:
        maior = idade

    # Conta quantas idades foram informadas
    cont += 1
    # Acumula as idades informadas
    soma_idade += idade
    # cont e soma_estatura serão usadas para calcular a média

print(f"{maior}m é a maior idade.")
print(f"{menor}m é a menor idade.")
media = soma_idade / cont
print(f"Média das idade = {media}")