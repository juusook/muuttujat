import numpy as np
import matplotlib.pyplot as plt

# Luo kuva kolminkertaisella leveydellä
fig, ax = plt.subplots(figsize=(19.2, 4.8))

# x-alue -3π ... 3π
x = np.linspace(-3*np.pi, 3*np.pi, 1000)
y1 = np.sin(x)
y2 = np.cos(x)

# Piirretään käyrät eri väreillä ja tyyleillä
ax.plot(x, y1, color='crimson', linestyle='--', linewidth=2, label=r'$\sin(x)$')
ax.plot(x, y2, color='royalblue', linestyle='-.', linewidth=2, label=r'$\cos(x)$')

# Akselien rajat
ax.set_xlim(-3*np.pi, 3*np.pi)
ax.set_ylim(-1.2, 1.2)

# Pi-akselimerkinnät
xticks = np.arange(-3*np.pi, 3.1*np.pi, np.pi/2)
xlabels = [
    r"$-3\pi$", r"$-\frac{5\pi}{2}$", r"$-2\pi$", r"$-\frac{3\pi}{2}$",
    r"$-\pi$", r"$-\frac{\pi}{2}$", "0",
    r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$",
    r"$2\pi$", r"$\frac{5\pi}{2}$", r"$3\pi$"
]
ax.set_xticks(xticks)
ax.set_xticklabels(xlabels, fontsize=11)

# Y-akselin merkit
ax.set_yticks([-1, -0.5, 0, 0.5, 1])
ax.set_yticklabels([r"$-1$", r"$-0.5$", "0", r"$0.5$", r"$1$"])

# Ruudukko, selite ja otsikko
ax.grid(True, linestyle=':', color='gray', alpha=0.7)
ax.legend(loc='upper right', fontsize=12)
ax.set_xlabel("x (rad)", fontsize=12)
ax.set_ylabel("y", fontsize=12)
ax.set_title(r"Sini- ja kosinifunktio välillä $[-3\pi, 3\pi]$", fontsize=14)

plt.show()