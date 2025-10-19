import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("est16us.csv", delimiter=",", skiprows=1)

print("Questão 9")

print("")

print("Quais estados estão acima da renda domiciliar mediana?")

reducedDf = df.iloc[1:, [2, 21]].copy()
meanEUAHouseHoldIncome = reducedDf["Median Household Income"].mean()

statesAboveAverageIncome = reducedDf[
    reducedDf["Median Household Income"] > meanEUAHouseHoldIncome
]

print("Estados com renda domiciliar mediana acima da média dos EUA:")
for i in statesAboveAverageIncome["Name"]:
    print("-", i)

print("Gráfico para a questão 9")

statesAboveData = statesAboveAverageIncome.sort_values(
    "Median Household Income", ascending=True
)

plt.figure(figsize=(12, 8))
bars = plt.barh(
    statesAboveData["Name"], statesAboveData["Median Household Income"], color="#27ae60"
)
plt.xlabel("Renda Domiciliar Mediana ($)")
plt.ylabel("Estado")
plt.title(
    f"Estados com Renda Acima da Média Nacional (${meanEUAHouseHoldIncome:,.0f})",
    fontsize=13,
    fontweight="bold",
)

plt.axvline(
    x=meanEUAHouseHoldIncome,
    color="red",
    linestyle="--",
    linewidth=2,
    label=f"Média Nacional: ${meanEUAHouseHoldIncome:,.0f}",
)

for i, (name, value) in enumerate(
    zip(statesAboveData["Name"], statesAboveData["Median Household Income"])
):
    plt.text(value + 500, i, f"${value:,.0f}", va="center", fontsize=8)

plt.legend()
plt.tight_layout()
plt.show()
