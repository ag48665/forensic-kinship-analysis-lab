import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 4))

ax.axis("off")

ax.text(
    0.2,
    0.8,
    "Parent 1\nD3S1358: 13,17",
    ha="center",
    fontsize=12
)

ax.text(
    0.8,
    0.8,
    "Parent 2\nD3S1358: 12,15",
    ha="center",
    fontsize=12
)

ax.text(
    0.5,
    0.2,
    "Child\nD3S1358: 12,13",
    ha="center",
    fontsize=12
)

ax.arrow(
    0.3,
    0.72,
    0.15,
    -0.35,
    head_width=0.03,
    length_includes_head=True
)

ax.arrow(
    0.7,
    0.72,
    -0.15,
    -0.35,
    head_width=0.03,
    length_includes_head=True
)

plt.title("Parent-Child STR Inheritance")

plt.savefig(
    "reports/inheritance_diagram.png",
    dpi=300,
    bbox_inches="tight"
)

print("Diagram saved.")