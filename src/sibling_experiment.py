from kinship_simulator import (
    generate_profile,
    generate_child,
    count_shared_alleles
)

import pandas as pd


results = []

for _ in range(1000):

    parent1 = generate_profile()
    parent2 = generate_profile()

    sibling1 = generate_child(
        parent1,
        parent2
    )

    sibling2 = generate_child(
        parent1,
        parent2
    )

    unrelated = generate_profile()

    sibling_shared = count_shared_alleles(
        sibling1,
        sibling2
    )

    unrelated_shared = count_shared_alleles(
        sibling1,
        unrelated
    )

    results.append({
        "siblings": sibling_shared,
        "unrelated": unrelated_shared
    })

df = pd.DataFrame(results)

print(
    "Average sibling shared alleles:",
    df["siblings"].mean()
)

print(
    "Average unrelated shared alleles:",
    df["unrelated"].mean()
)

df.to_csv(
    "reports/sibling_results.csv",
    index=False
)