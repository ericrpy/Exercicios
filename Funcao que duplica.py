#def duplicar (numero):
#    return numero * 2
#
#v = duplicar(10)
#print (v)
#
## OU
#print(duplicar(2))




def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)



