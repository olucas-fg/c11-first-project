import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("est16us.csv", delimiter=",", skiprows=1)

print("Questão 10")

print("")

print(
    "Quais estados têm maior incerteza nas estimativas de pobreza (maior diferença entre limites superior e inferior do CI 90%)?"
)

print("")

uncertaintyData = df.iloc[1:, [2, 7, 8]].copy()
print(uncertaintyData.head())

uncertaintyData["Uncertainty"] = uncertaintyData.iloc[:, 2] - uncertaintyData.iloc[:, 1]

# Top 5 estados com maior incerteza
MostUncertain = uncertaintyData.nlargest(5, "Uncertainty")
print("Top 5 estados com maior incerteza:")
print(MostUncertain)
print("")

print("Gráfico para a questão 10")

plt.figure(figsize=(10, 6))
plt.barh(MostUncertain["Name"], MostUncertain["Uncertainty"], color="#e74c3c")
plt.xlabel("Incerteza (diferença entre limites do CI 90%)")
plt.ylabel("Estado")
plt.title("Top 5 Estados com Maior Incerteza nas Estimativas de Pobreza")

for i, (name, value) in enumerate(
    zip(MostUncertain["Name"], MostUncertain["Uncertainty"])
):
    plt.text(
        value / 2,
        i,
        f"{value:.2f}%",
        va="center",
        ha="center",
        color="white",
        fontweight="bold",
        fontsize=10,
    )

plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
