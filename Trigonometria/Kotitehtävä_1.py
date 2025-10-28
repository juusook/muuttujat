import numpy as np
import math

'''a = 1.35
b = 2.765

print(np.degrees(a))
print(np.degrees(b))

c = 48
d = 171

print(np.radians(c))
print(np.radians(d))
'''
#tehtävä 1, radiaanit asteiksi
a = 2.493
b = 0.911
print(np.degrees(a))
print(np.degrees(b))

#asteet radiaaneiksi
c = 137.7
d = 62.3
print(np.radians(c))
print(np.radians(d))

#Numpy Array
A = np.array([30, 45, 60, 90,120, 135, 150, 180, 270, 360])
for i in A:
    print(np.radians(i))

print("hypotenuusan pituus on:", np.hypot(1.6, 2.3))