# criando a lista
#        1   1   2   3   4   5
#       -6   -5  -4  -3  -2  -1
lista = [10, 20, 30, 40, 50, 60]

# alterando o índice 2
lista[2] = 300

# deletando o índice 3
del lista[3]

print (lista)

# printando apenas o índice 2
print(lista[2])

# adicionando um índice no final da lista
lista.append(50)

# deletando o último índice da lista
lista.pop()

lista.append('BBB')

print(lista)

# inserindo o valor 5 no índice 0
lista.insert(0, 5)