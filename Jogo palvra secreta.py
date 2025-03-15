palavra = input("Digite a palavra secreta: ").lower()
tentativas = set()
contador = 0

while True:
    tentativa = input("Digite uma letra: ").lower()
    contador += 1

    if len(tentativa) != 1:
        print("Digite apenas uma letra!")
        continue     
    
# adiciona a letra ao conjunto de tentativas
    if tentativa not in tentativas:
        tentativas.add(tentativa)
        
    
    resultado = "".join(letra if letra in tentativas else "*" for letra in palavra)
    print(resultado)
    

# se todas as letras forem descobertas encerra o jogo
    if "*" not in resultado:
        print("Parabéns! Você descobriu a palavra!")
        print(f"Número de tentativas: {contador}")
        break