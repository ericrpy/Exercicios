est1 = float(input("Estatura 1: "))
est2 = float(input("Estatura 2: "))
est3 = float(input("Estatura 3: "))

if est1 == est2 or est1 == est3 or est2 == est3:
    print("Há pelo menos duas estaturas iguais")
    
elif est1 > est2 and est1 > est3:
    print(f"Estatura 1 é a maior: {est1}")
    
elif est2 > est1 and est2 > est3:
    print(f"Estatura 2 é maior: {est2}")
    
else:
    print(f"Estatura 3 é maior: {est3}")