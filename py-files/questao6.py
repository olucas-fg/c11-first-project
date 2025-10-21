import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("est16us.csv", delimiter=",", skiprows=1)

print("Questão 6")

print("")

print(
    "Quais estados têm alta renda mediana, mas também alta taxa de pobreza? (Cite os 5 mais discrepantes)"
)

discrepancyData = df.iloc[1:, [2, 21, 6]].copy()

discrepancyData = discrepancyData.dropna()

# Normalizar dados (escala 0-1)
# É necessário normalizar porque as variáveis estão em escalas diferentes:
# - Renda: dezenas de milhares
# - Pobreza: percentagem
# Com normalização (0-1), ambas as variáveis terão o mesmo peso na comparação

discrepancyData["Normalized Income"] = (
    discrepancyData["Median Household Income"]
    - discrepancyData["Median Household Income"].min()
) / (
    discrepancyData["Median Household Income"].max()
    - discrepancyData["Median Household Income"].min()
)

discrepancyData["Normalized Poverty"] = (
    discrepancyData["Poverty Percent, All Ages"]
    - discrepancyData["Poverty Percent, All Ages"].min()
) / (
    discrepancyData["Poverty Percent, All Ages"].max()
    - discrepancyData["Poverty Percent, All Ages"].min()
)

# Quanto menor o valor, mais discrepante (alta renda mas muita pobreza)
discrepancyData["Discrepancy"] = (
    discrepancyData["Normalized Income"] - discrepancyData["Normalized Poverty"]
)

MostDiscrepant = discrepancyData.nsmallest(5, "Discrepancy")
print(
    MostDiscrepant[
        ["Name", "Median Household Income", "Poverty Percent, All Ages", "Discrepancy"]
    ]
)
print("")

print("Gráfico para a questão 6")
plt.figure(figsize=(12, 8))

plt.scatter(
    discrepancyData["Median Household Income"],
    discrepancyData["Poverty Percent, All Ages"],
    alpha=0.5,
    s=50,
    color="gray",
    label="Outros estados",
)

plt.scatter(
    MostDiscrepant["Median Household Income"],
    MostDiscrepant["Poverty Percent, All Ages"],
    alpha=0.8,
    s=150,
    color="red",
    label="Top 5 discrepantes",
)

for idx, row in MostDiscrepant.iterrows():
    plt.annotate(
        row["Name"],
        (row["Median Household Income"], row["Poverty Percent, All Ages"]),
        xytext=(5, 5),
        textcoords="offset points",
        fontsize=9,
        fontweight="bold",
    )

plt.xlabel("Renda Domiciliar Mediana ($)", fontsize=12)
plt.ylabel("Percentual de Pobreza (%)", fontsize=12)
plt.title(
    "Estados com Alta Renda mas Alta Pobreza (Discrepancy)",
    fontsize=14,
    fontweight="bold",
)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
