# exemplo de uso dos sets

letras = set()

while True:
    letra = input("Digite: ")
    letras.add(letra.lower())

    if 'l' in letras:
        print('PARABENS')
        break

    print(letras)
