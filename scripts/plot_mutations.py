import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/mutation_counts.csv")

plt.figure(figsize=(12, 5))
plt.plot(df["alignment_position"], df["mutation_frequency"])
plt.xlabel("HA Alignment Position")
plt.ylabel("Mutation Frequency")
plt.title("Mutation Frequency Across Influenza A Hemagglutinin")
plt.tight_layout()

plt.savefig("figures/ha_mutation_frequency.png", dpi=300)
print("Saved figure to figures/ha_mutation_frequency.png")