import numpy as np

R, a = float(input("Введите радиус: ")), float(input("Введите угол в градусах: "))

x = R * np.cos(a)
y = R * np.sin(a)
print(f"x = {x};\ny = {y}")