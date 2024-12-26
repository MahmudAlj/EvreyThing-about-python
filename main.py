import math
import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2 * math.pi, 1000)
r = 1 + np.sin(6 * theta)
x_gul = r * np.cos(theta)
y_gul = r * np.sin(theta)

t = np.linspace(0, 2 * math.pi, 1000)
x_kalp = 16 * (np.sin(t) ** 3)
y_kalp = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

letters = "Funda Toksöz"
x_positions = np.linspace(-2.5, 2.5, len(letters))
y_positions = -0.1 * (x_positions ** 2) + 3

# Cizim
plt.figure(figsize=(8, 8))
plt.plot(x_gul, y_gul, color='red')
plt.plot(x_kalp / 4, y_kalp / 4 - 1, color='pink')


for i, letter in enumerate(letters):
    if i < len(letters) - 1:
        dx = x_positions[i + 1] - x_positions[i]
        dy = y_positions[i + 1] - y_positions[i]
        angle = math.degrees(math.atan2(dy, dx))
    else:
        angle = 0

    plt.text(
        x_positions[i],
        y_positions[i],
        letter,
        fontsize=16,
        color="black",
        ha="center",
        va="center",
        rotation=angle
    )

plt.axis('off')
plt.show()
