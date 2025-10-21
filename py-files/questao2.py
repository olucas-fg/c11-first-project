import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("est16us.csv", delimiter=",", skiprows=1)

print("Questão 2")

print("")

print(
    "Quais são os 10 locais com a maior Renda Domiciliar Mediana (Median Household Income)"
)

statesAndMedianHouseIncome = df.iloc[1:, [2, 21]]
MostMedianHouseIncome = statesAndMedianHouseIncome.nlargest(
    10, "Median Household Income"
)
print(MostMedianHouseIncome)

print("")

print("Gráfico para a questão 2:")

plt.figure(figsize=(10, 6))
bars = plt.barh(
    MostMedianHouseIncome["Name"],
    MostMedianHouseIncome["Median Household Income"],
    color="darkgreen",
)
plt.xlabel("Renda Domiciliar Mediana ($)")
plt.ylabel("Estado/Localidade")
plt.title("Top 10 Locais com Maior Renda Domiciliar Mediana (EUA)")

for i, (name, value) in enumerate(
    zip(MostMedianHouseIncome["Name"], MostMedianHouseIncome["Median Household Income"])
):
    plt.text(
        value / 2,
        i,
        f"${value:,.0f}",
        va="center",
        ha="center",
        color="white",
        fontweight="bold",
        fontsize=9,
    )

plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
