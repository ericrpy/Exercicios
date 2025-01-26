valor = float(input("Valor total da venda: "))
print("1 - A vista")
print("2 - Débito")
print("3 - Crédito")
op1 = int(input("Digite a forma de pagamento: "))

if op1 == 1:
    valor = valor * 0.85
    print(f"Valor final da venda: {valor}")
    
elif op1 == 2:
    valor = valor * 0.90
    print(f"Valor final da venda: {valor}")
    
elif op1 == 3:
    valor = valor * 0.95
    print(f"Valor final da venda: {valor}")
    
else:
    print("Opção inválida")