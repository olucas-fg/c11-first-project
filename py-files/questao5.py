import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("est16us.csv", delimiter=",", skiprows=1)

print("Questão 5")

print("")

print(
    "Qual a porcentagem dos estados em que a taxa de pobreza em crianças de 0 a 4 anos é mais alta que a de 5 a 17 anos?"
)

taxData = df.iloc[1:, [2, 18, 27]].copy()

taxData["High Poverty Babies"] = (
    taxData["Poverty Percent, Age 0-4"]
    > taxData["Poverty Percent, Age 5-17 in Families"]
)

highPovertyBabyStates = taxData["Name"][taxData["High Poverty Babies"] == True]
highSize = len(highPovertyBabyStates)

print(f"Existem {highSize} estados com pobreza de bebes alta:")
for state in highPovertyBabyStates:
    print(f"- {state}")

highPovertyInfantyStates = taxData["Name"][taxData["High Poverty Babies"] == False]
fiveToSeventeenSize = len(highPovertyInfantyStates)

print(f"Existem {fiveToSeventeenSize} estados com pobreza na infância mais alta:")
for state in highPovertyInfantyStates:
    print(f"- {state}")

print("")
print("Gráfico para a questão 5")

sizes = [highSize, fiveToSeventeenSize]
labels = ["Pobreza 0-4 anos maior", "Pobreza 5-17 anos maior"]
colors = ["red", "blue"]

plt.figure(figsize=(10, 7))
plt.pie(
    sizes,
    labels=labels,
    colors=colors,
    autopct="%1.1f%%",
    shadow=True,
    startangle=90,
    textprops={"fontsize": 12, "fontweight": "bold"},
)
plt.title(
    f"Distribuição de Estados por Faixa Etária com Maior Pobreza Infantil\n(Total: {highSize + fiveToSeventeenSize} estados)",
    fontsize=14,
    fontweight="bold",
)
plt.axis("equal")
plt.tight_layout()
plt.show()
