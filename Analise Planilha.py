import pandas as pd

df = pd.read_csv("C:\\Users\\erirodrigues\\Desktop\\dados_ciencia_robusto.csv")

# print(df.head())

# rint(df['Departamento'])

contagem_ti = df["Departamento"].astype(str).str.contains("TI", case=False, na=False).sum()
print(f"Número de ocorrências de 'TI' na coluna 'Departamento': {contagem_ti}")

media_salarios = df["Salario"].median()
print(f"A media dos salários é: {media_salarios}")

# Filtrar os dados onde o Departamento é "TI"
promocoes_ti = df[df["Departamento"] == "TI"][["Departamento", "Promocoes_Recebidas"]]

# Exibir os resultados
print(promocoes_ti)

