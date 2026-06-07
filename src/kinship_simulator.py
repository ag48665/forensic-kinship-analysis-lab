import random


STR_MARKERS = {
    "D3S1358": [12, 13, 14, 15, 16, 17, 18],
    "vWA": [14, 15, 16, 17, 18, 19, 20, 21],
    "FGA": [18, 19, 20, 21, 22, 23, 24, 25, 26],
    "TH01": [6, 7, 8, 9, 10],
    "D8S1179": [10, 11, 12, 13, 14, 15],
    "D21S11": [27, 28, 29, 30, 31, 32],
}


def generate_profile():
    profile = {}

    for marker, alleles in STR_MARKERS.items():
        profile[marker] = sorted([
            random.choice(alleles),
            random.choice(alleles)
        ])

    return profile


def generate_child(parent1, parent2):
    child = {}

    for marker in parent1:
        allele_from_parent1 = random.choice(parent1[marker])
        allele_from_parent2 = random.choice(parent2[marker])

        child[marker] = sorted([
            allele_from_parent1,
            allele_from_parent2
        ])

    return child


def count_shared_alleles(profile1, profile2):
    shared = 0

    for marker in profile1:
        shared += len(
            set(profile1[marker]).intersection(set(profile2[marker]))
        )

    return shared


if __name__ == "__main__":
    parent1 = generate_profile()
    parent2 = generate_profile()

    child = generate_child(parent1, parent2)
    unrelated = generate_profile()

    print("\nPARENT 1")
    print(parent1)

    print("\nPARENT 2")
    print(parent2)

    print("\nCHILD")
    print(child)

    print("\nUNRELATED INDIVIDUAL")
    print(unrelated)

    print("\nSHARED ALLELES")
    print("Parent-child:", count_shared_alleles(parent1, child))
    print("Unrelated-child:", count_shared_alleles(unrelated, child))