lista_compras = []

while True:
    
    print("Selecione uma opção: ")
    selecao = str(input("[i]nserir [a]pagar [l]istar: [s]air \n"))

    if selecao == 'i':
        produto = str(input("Digite o produto para adicionar na lista: "))
        lista_compras.append(produto)
        print(lista_compras)

    elif selecao == 'a':
        produto = input("Digite o produto a ser apagado: ")
        lista_compras.remove(produto)
        print(lista_compras)

    elif selecao == 'l':
        print(lista_compras)
        
    elif selecao == 's':
        break

    else:
        print("Digite [i] [a] [l] ou [s]")
