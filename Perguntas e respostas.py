perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Qual a capital do Brasil?',
        'Opções': ['Rio de Janeiro', 'Brasília', 'São Paulo', 'Salvador'],
        'Resposta': 'Brasília',
    }
]

# Contador de acertos
acertos = 0

for i, pergunta in enumerate(perguntas):
    print(f"\nPergunta {i+1}: {pergunta['Pergunta']}")
    
    for j, opcao in enumerate(pergunta['Opções'], 1):
        print(f"{j}. {opcao}")
    
    try:
        escolha = int(input("Digite o número da resposta correta: "))
        resposta_usuario = pergunta['Opções'][escolha - 1]
        
        if resposta_usuario == pergunta['Resposta']:
            print("✅ Correto!")
            acertos += 1
        else:
            print(f"❌ Errado! A resposta certa era: {pergunta['Resposta']}")
    except (ValueError, IndexError):
        print("❗ Entrada inválida. Pulando para a próxima pergunta.")

print(f"\nVocê acertou {acertos} de {len(perguntas)} perguntas.")
