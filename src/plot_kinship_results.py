import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("reports/kinship_results.csv")

means = {
    "True parent": df["true_parent_lr"].mean(),
    "Unrelated": df["unrelated_lr"].mean()
}

plt.figure(figsize=(8, 5))

plt.bar(
    means.keys(),
    means.values()
)

plt.ylabel("Average LR")
plt.title("Parent-child vs unrelated likelihood ratios")

plt.tight_layout()

plt.savefig(
    "reports/kinship_experiment.png",
    dpi=300
)

print("Plot saved.")