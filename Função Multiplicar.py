def mult():
    multiplicados = (1, 2, 3, 4, 5)
    resultado = 1
    for num in multiplicados:
        resultado *= num
    return resultado

print (mult())


def par_impar(numero):
    return numero % 2 == 0
print(par_impar(2))
print(par_impar(3))