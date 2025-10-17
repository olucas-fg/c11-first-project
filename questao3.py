import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("est16us.csv", delimiter=",", skiprows=1)

print("Questão 3")

print("")

print(
    "Quais são os 5 locais com o maior percentual de pobreza na primeira infância (Poverty Percent, Age 0-4)?"
)

stateAndInfancyPoverty = df.iloc[1:, [2, 27]]
MostInfancyPoverty = stateAndInfancyPoverty.nlargest(5, "Poverty Percent, Age 0-4")
print(MostInfancyPoverty)

print("Gráfico para a questão 3")
plt.figure(figsize=(10, 6))
bars = plt.bar(
    MostInfancyPoverty["Name"],
    MostInfancyPoverty["Poverty Percent, Age 0-4"],
    color="darkorange",
)
plt.xlabel("Estado/Localidade")
plt.ylabel("Percentual de Pobreza (%)")
plt.title("Top 5 Locais com Maior Percentual de Pobreza Infantil (0-4 anos)")

for i, (name, value) in enumerate(
    zip(MostInfancyPoverty["Name"], MostInfancyPoverty["Poverty Percent, Age 0-4"])
):
    plt.text(
        i,
        value + 0.5,
        f"{value:.1f}%",
        ha="center",
        va="bottom",
        fontweight="bold",
        fontsize=10,
    )

plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
