import math
arr = [input("Введите координату X: "), input("Введите координату Y: "), input("Введите координату Z: ")]
summa = math.sqrt(float(arr[0])**2 + float(arr[1])**2 + float(arr[2])**2)
print(f"Длина вектора с выбранными координатами = {summa}")