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

    missing_person = generate_child(
        parent1,
        parent2
    )

    unrelated = generate_profile()

    true_lr = simple_parent_child_lr(
        parent1,
        missing_person
    )

    false_lr = simple_parent_child_lr(
        unrelated,
        missing_person
    )

    results.append({
        "true_relative_lr": true_lr,
        "unrelated_lr": false_lr
    })

df = pd.DataFrame(results)

print(
    "Average true relative LR:",
    df["true_relative_lr"].mean()
)

print(
    "Average unrelated LR:",
    df["unrelated_lr"].mean()
)

df.to_csv(
    "reports/missing_person_results.csv",
    index=False
)