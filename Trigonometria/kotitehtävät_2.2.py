import numpy as np
import matplotlib.pyplot as plt

# Luo kuva kolminkertaisella leveydellä
fig, ax = plt.subplots(figsize=(19.2, 4.8))

# Määritä x-alue -3π ... 3π
x = np.linspace(-3*np.pi, 3*np.pi, 1000)

# Lasketaan käyrät
y1 = np.sin(x)
y2 = np.cos(x)

# Piirretään eri väreillä ja tyyleillä
ax.plot(x, y1, color='crimson', linestyle='--', linewidth=2, label='sin(x)')
ax.plot(x, y2, color='royalblue', linestyle='-.', linewidth=2, label='cos(x)')

# Akselien rajat
ax.set_xlim(-3*np.pi, 3*np.pi)
ax.set_ylim(-1.2, 1.2)

# Ruudukko ja otsikot
ax.grid(True, linestyle=':', color='gray', alpha=0.7)
ax.set_xlabel('x (rad)', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_title('Sini- ja kosinifunktio väliltä -3π ... 3π', fontsize=14)

# Selite
ax.legend(loc='upper right', fontsize=12)

plt.show()