import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("est16us.csv", delimiter=",", skiprows=1)

print("Questão 8")

print("")

print("Quantos estados estão abaixo da média da pobreza (Poverty Percent, All Ages)?")

reducedDf = df.iloc[1:, [2, 6]].copy()
meanPoverty = reducedDf["Poverty Percent, All Ages"].mean()

quantityBelowAverage = len(
    reducedDf[reducedDf["Poverty Percent, All Ages"] < meanPoverty]
)
quantityAboveAverage = len(
    reducedDf[reducedDf["Poverty Percent, All Ages"] > meanPoverty]
)

print("Quantidade de estados abaixo da média da pobreza:", quantityBelowAverage)
print("Quantidade de estados acima da média da pobreza:", quantityAboveAverage)
print("")

print("Gráfico para a questão 8: ")

sizes = [quantityBelowAverage, quantityAboveAverage]
labels = ["Abaixo da Média", "Acima da Média"]
colors = ["#2ecc71", "#e74c3c"]
explode = (0.05, 0.05)

plt.figure(figsize=(10, 7))
plt.pie(
    sizes,
    explode=explode,
    labels=labels,
    colors=colors,
    autopct="%1.1f%%",
    shadow=True,
    startangle=90,
    textprops={"fontsize": 12, "fontweight": "bold"},
)
plt.title(
    f"Estados Abaixo vs Acima da Média Nacional de Pobreza\n(Média: {meanPoverty:.2f}%)",
    fontsize=14,
    fontweight="bold",
)
plt.axis("equal")
plt.tight_layout()
plt.show()
