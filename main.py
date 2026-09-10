import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, Rectangle
RGG
# 1. CREATE MANDELBROT FRACTAL

def make_fractal(width=500, height=700, max_iter=120):
    # Fractal area
    x = np.linspace(-2.2, 0.8, width)
    y = np.linspace(-1.7, 1.7, height)

    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y

    Z = np.zeros_like(C)
    result = np.zeros(C.shape)

    # Main Mandelbrot loop
    for i in range(max_iter):
        Z = Z * Z + C

        inside = np.abs(Z) <= 2

        # Save iteration number
        result[inside] = i

    # Normalize
    result = result / max_iter

    # -------------------------
    # Fractal color design
    # -------------------------

    # Start with dark shades
    r = 0.03 + result * 0.25
    g = 0.04 + result * 0.20
    b = 0.06 + result * 0.15

    # Navy parts
    navy = (result > 0.12) & (result < 0.35)

    r[navy] = 0.02
    g[navy] = 0.08
    b[navy] = 0.20

    # Gold parts
    gold = result > 0.35

    r[gold] = 0.65 + result[gold] * 0.30
    g[gold] = 0.35 + result[gold] * 0.35
    b[gold] = 0.08 + result[gold] * 0.12

    # Very dark Mandelbrot center
    center = result < 0.05

    r[center] = 0.015
    g[center] = 0.018
    b[center] = 0.025

    return np.dstack((r, g, b))


# Create the fractal
fractal = make_fractal()


# =========================================================
# 2. MAKE A T-SHIRT SHAPE
# =========================================================

def draw_shirt(ax, angle=0):
    # Cream shirt color
    shirt_color = "#F3E7CF"

    # Dark outline
    edge_color = "#D7C8AE"

    # Shirt body
    body = Polygon(
        [
            (-1.8, 3.8),
            (-1.25, 4.5),
            (-0.65, 4.8),
            (0.65, 4.8),
            (1.25, 4.5),
            (1.8, 3.8),
            (1.25, 3.45),
            (0.95, 3.8),
            (0.95, 0.3),
            (-0.95, 0.3),
            (-0.95, 3.8),
            (-1.25, 3.45)
        ],
        closed=True,
        facecolor=shirt_color,
        edgecolor=edge_color,
        linewidth=2
    )

    ax.add_patch(body)

    # Sleeves
    left_sleeve = Polygon(
        [
            (-1.25, 4.5),
            (-1.8, 3.8),
            (-1.25, 3.45),
            (-0.85, 4.0)
        ],
        closed=True,
        facecolor=shirt_color,
        edgecolor=edge_color,
        linewidth=2
    )

    right_sleeve = Polygon(
        [
            (1.25, 4.5),
            (1.8, 3.8),
            (1.25, 3.45),
            (0.85, 4.0)
        ],
        closed=True,
        facecolor=shirt_color,
        edgecolor=edge_color,
        linewidth=2
    )

    ax.add_patch(left_sleeve)
    ax.add_patch(right_sleeve)

    # Neck opening
    neck = Circle(
        (0, 4.55),
        0.42,
        facecolor="#E4D6BD",
        edgecolor=edge_color,
        linewidth=2
    )

    ax.add_patch(neck)

    # Add fractal only on front
    if angle == 0:
        # Make a narrow vertical fractal strip
        ax.imshow(
            fractal,
            extent=[-0.75, 0.75, 0.7, 4.3],
            origin="lower",
            aspect="auto",
            alpha=0.92,
            zorder=3
        )

        # Cream-colored mask around fractal to make it look narrower
        ax.add_patch(
            Rectangle(
                (-0.9, 0),
                0.15,
                5,
                facecolor=shirt_color,
                edgecolor="none",
                zorder=4
            )
        )

        ax.add_patch(
            Rectangle(
                (0.75, 0),
                0.15,
                5,
                facecolor=shirt_color,
                edgecolor="none",
                zorder=4
            )
        )

    # Shirt details
    ax.plot(
        [-0.95, 0.95],
        [0.3, 0.3],
        color=edge_color,
        linewidth=2
    )

    ax.set_xlim(-2.2, 2.2)
    ax.set_ylim(0, 5.2)
    ax.set_aspect("equal")
    ax.axis("off")


# =========================================================
# 3. MAKE THE COMPLETE 360-DEGREE DESIGN
# =========================================================

fig, axes = plt.subplots(
    1,
    4,
    figsize=(16, 7)
)

# Background
fig.patch.set_facecolor("#EAE4DA")

views = [
    ("Front View", 0),
    ("Side Profile", 90),
    ("Back View", 180),
    ("Side Profile", 270)
]

for ax, (title, angle) in zip(axes, views):

    # Background for each panel
    ax.set_facecolor("#EAE4DA")

    # Draw shirt
    draw_shirt(ax, angle)

    # View title
    ax.text(
        0,
        -0.25,
        title,
        ha="center",
        va="top",
        fontsize=13,
        fontweight="bold"
    )

    # Angle
    ax.text(
        0,
        -0.55,
        f"{angle}°",
        ha="center",
        va="top",
        fontsize=11
    )



# 4. MAIN TITLE

fig.suptitle(
    "360° FRACTAL T-SHIRT DESIGN",
    fontsize=22,
    fontweight="bold",
    y=0.97
)

fig.text(
    0.5,
    0.02,
    "Custom Mandelbrot Fractal • Cream T-Shirt • Black + Navy + Gold",
    ha="center",
    fontsize=12
)

# 5. SAVE THE FINAL IMAGE

plt.savefig(
    "fractal_tshirt_360_design.png",
    dpi=300,
    bbox_inches="tight",
    facecolor="#EAE4DA"
)

# Show result
plt.show()