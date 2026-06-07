def parent_child_compatible(parent, child):
    for marker in parent:
        parent_alleles = set(parent[marker])
        child_alleles = set(child[marker])

        if len(parent_alleles.intersection(child_alleles)) == 0:
            return False

    return True


def simple_parent_child_lr(parent, child):
    compatible_markers = 0
    incompatible_markers = 0

    for marker in parent:
        parent_alleles = set(parent[marker])
        child_alleles = set(child[marker])

        if len(parent_alleles.intersection(child_alleles)) > 0:
            compatible_markers += 1
        else:
            incompatible_markers += 1

    return (compatible_markers + 1) / (incompatible_markers + 1)