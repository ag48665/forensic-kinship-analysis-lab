import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("reports/sibling_results.csv")

means = {
    "Siblings": df["siblings"].mean(),
    "Unrelated": df["unrelated"].mean()
}

plt.figure(figsize=(8, 5))

plt.bar(
    means.keys(),
    means.values()
)

plt.ylabel("Average shared alleles")
plt.title("Sibling vs unrelated shared STR alleles")

plt.tight_layout()

plt.savefig(
    "reports/sibling_experiment.png",
    dpi=300
)

print("Plot saved.")