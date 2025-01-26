termo1 = int(input("Digite o primeiro termo: "))
quantidade = int(input("Quantidade de termos: "))
razao = int(input("Digite a razão: "))

pa = []

for n in range(quantidade):
    termo = termo1 + n * razao
    pa.append(termo)
    
print("A Progressão Aritmética gerada é:")
print(pa)