print("1 - Programador de Sistemas")
print("2 - Analista de Sistemas")
print("3 - Analista de banco de Dados")

cargo = int(input("Qual cargo: "))
salario = float(input("Salário: "))

if cargo == 1:
    salario = salario * 1.3
    print(f"Salario com aumento: {salario}")

elif cargo == 2:
    salario = salario * 1.2
    print(f"Salario com aumento: {salario}")
    
elif cargo == 3:
    salario = salario * 1.15
    print(f"Salario com aumento: {salario}")
    
else:
    print("Opção inválida")

