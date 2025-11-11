import numpy as np
from matplotlib import pyplot as plt, patches

# Luo kuva ja akselit
fig, ax = plt.subplots()

# Piirrä yksikköympyrä
ymp = patches.Circle((0, 0), radius=1, fill=False)
ax.add_patch(ymp)

# Asetetaan akselit keskelle
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Näytetään vain keskiakselien asteikko
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.axis('equal')

# 🔹 Tässä määritellään kulmat asteina
asteet = np.array([30, 45, 60, 90, 120, 150, 180, 270])

# Muutetaan radiaaneiksi
kulmat = np.deg2rad(asteet)

# Lasketaan pisteiden koordinaatit
x = np.cos(kulmat)
y = np.sin(kulmat)

# Piirretään pisteet yksikköympyrälle
plt.scatter(x, y, color='red', marker='X')

# Lisätään kulmien tekstit (asteina)
for i, aste in enumerate(asteet):
    plt.annotate(f"{aste}°",
                 xy=(x[i], y[i]),
                 xycoords='data',
                 xytext=(+10, +5),
                 textcoords='offset points',
                 fontsize=10,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))

# Näytetään kuva
plt.show()