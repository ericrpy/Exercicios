a = 18
b = 0

try:
    c = a/b
    print(f'Resultado', c)

except ZeroDivisionError: # trata apenas o erro ZeroDivisionError
    print('Dividiu por zero')

except Exception: # trata qualquer tipo de erro
    print('Erro desconhecido')

finally: # sempre será executado
    print('FINALIZANDO')