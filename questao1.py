import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("est16us.csv", delimiter=",", skiprows=1)
print("Questão 1")

print("")

print(
    "Quais são os 10 locais (condados/cidades) com o maior percentual de pobreza geral dos Estados Unidos? (Poverty Percent, All Ages)"
)

print("")

statesAndPercentyPoverty = df.iloc[1:, [2, 6]]
MostPoverty = statesAndPercentyPoverty.nlargest(10, "Poverty Percent, All Ages")
print(MostPoverty)

print("")

print("Gráfico para a questão 1:")

plt.figure(figsize=(10, 6))
plt.barh(MostPoverty["Name"], MostPoverty["Poverty Percent, All Ages"], color="darkred")
plt.xlabel("Percentual de Pobreza (%)")
plt.ylabel("Estado/Localidade")
plt.title("Top 10 Locais com Maior Percentual de Pobreza (EUA)")
for i, (name, value) in enumerate(
    zip(MostPoverty["Name"], MostPoverty["Poverty Percent, All Ages"])
):
    plt.text(
        value / 2,
        i,
        f"{value:.1f}%",
        va="center",
        ha="center",
        color="white",
        fontweight="bold",
        fontsize=10,
    )
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
