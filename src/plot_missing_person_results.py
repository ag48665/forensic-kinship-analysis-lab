import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "reports/missing_person_results.csv"
)

means = {
    "True Relative":
        df["true_relative_lr"].mean(),
    "Unrelated":
        df["unrelated_lr"].mean()
}

plt.figure(figsize=(8, 5))

plt.bar(
    means.keys(),
    means.values()
)

plt.ylabel("Average LR")
plt.title(
    "Missing Person Identification"
)

plt.tight_layout()

plt.savefig(
    "reports/missing_person_experiment.png",
    dpi=300
)

print("Plot saved.")