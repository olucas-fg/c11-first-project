import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("est16us.csv", delimiter=",", skiprows=1)
df2 = pd.read_csv("us_states_fips_regions.csv", delimiter=",")

print("Questão 7")

print("")

print(
    "Existe algum padrão regional (por região dos EUA, por exemplo) na distribuição da pobreza"
)

reducedDf = df.iloc[1:, [2, 6]]

namesMostPoverty = reducedDf.nlargest(10, "Poverty Percent, All Ages")["Name"]
print(namesMostPoverty)
print("")

namesAndRegions = df2.loc[:, ["State Name", "Region"]]
print(namesAndRegions)
print("")

# .isin(namesMostPoverty): verifica se o nome do estado está na lista dos 10 mais pobres
regionsOfPoorest = namesAndRegions[namesAndRegions["State Name"].isin(namesMostPoverty)]
print(regionsOfPoorest)
print("")

print("Gráfico para a questão 7")
regionCounts = regionsOfPoorest["Region"].value_counts()

plt.figure(figsize=(10, 6))
bars = plt.barh(regionCounts.index, regionCounts.values, color=["red", "orange"])
plt.xlabel("Número de Estados no Top 10 de Pobreza")
plt.ylabel("Região")
plt.title("Distribuição Regional dos 10 Estados Mais Pobres dos EUA")

plt.tight_layout()
plt.show()
