from kinship_simulator import (
    generate_profile,
    generate_child
)

from kinship_likelihood import (
    simple_parent_child_lr
)

import pandas as pd


results = []

for _ in range(1000):

    parent1 = generate_profile()
    parent2 = generate_profile()

    child = generate_child(
        parent1,
        parent2
    )

    unrelated = generate_profile()

    true_lr = simple_parent_child_lr(
        parent1,
        child
    )

    unrelated_lr = simple_parent_child_lr(
        unrelated,
        child
    )

    results.append({
        "true_parent_lr": true_lr,
        "unrelated_lr": unrelated_lr
    })

df = pd.DataFrame(results)

print(
    "Average true parent LR:",
    df["true_parent_lr"].mean()
)

print(
    "Average unrelated LR:",
    df["unrelated_lr"].mean()
)

df.to_csv(
    "reports/kinship_results.csv",
    index=False
)