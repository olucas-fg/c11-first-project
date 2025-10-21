import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("est16us.csv", delimiter=",", skiprows=1)

print("Questão 4")

print("")

print(
    "Quais os 3 locais em que a disparidade entre o percentual de pobreza infantil (Poverty Percent, Age 0-17) e o percentual de pobreza geral (Poverty Percent, All Ages) é maior?"
)

disparityData = df.iloc[1:, [2, 6, 12]].copy()

disparityData["Disparity"] = (
    disparityData["Poverty Percent, Age 0-17"]
    - disparityData["Poverty Percent, All Ages"]
)

MostDisparity = disparityData[["Name", "Disparity"]].nlargest(3, ["Disparity"])
print(MostDisparity)
print("")

print("Gráfico para a questão 4")

graphData = disparityData.nlargest(3, "Disparity")

fig, ax = plt.subplots(figsize=(14, 6))
x = np.arange(len(graphData))
width = 0.25

bars1 = ax.bar(
    x - width,
    graphData["Poverty Percent, All Ages"],
    width,
    label="Pobreza Geral",
    color="blue",
)
bars2 = ax.bar(
    x,
    graphData["Poverty Percent, Age 0-17"],
    width,
    label="Pobreza Infantil (0-17)",
    color="purple",
)
bars3 = ax.bar(
    x + width,
    graphData["Disparity"],
    width,
    label="Disparity",
    color="darkred",
)

for i, v in enumerate(graphData["Poverty Percent, All Ages"]):
    ax.text(i - width, v + 0.5, f"{v:.1f}%", ha="center", va="bottom", fontsize=8)
for i, v in enumerate(graphData["Poverty Percent, Age 0-17"]):
    ax.text(i, v + 0.5, f"{v:.1f}%", ha="center", va="bottom", fontsize=8)
for i, v in enumerate(graphData["Disparity"]):
    ax.text(
        i + width,
        v + 0.3,
        f"+{v:.1f}%",
        ha="center",
        va="bottom",
        fontsize=8,
        fontweight="bold",
    )

ax.set_xlabel("Estado/Localidade")
ax.set_ylabel("Percentual (%)")
ax.set_title("Top 3 Locais com Maior Disparity entre Pobreza Infantil e Geral")
ax.set_xticks(x)
ax.set_xticklabels(graphData["Name"], rotation=45, ha="right")
ax.legend()

plt.tight_layout()
plt.show()
