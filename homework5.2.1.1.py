import random

tries = 100000
samples = [random.randint(0, 1) for i in range(tries)]
heads = samples.count(0)
tails = samples.count(1)

print(f"Heads count = {heads}, Tails count = {tails}")

# Сумма вероятностей выпадения орла или решки должна быть равна 1, проверяем

p = heads / tries + tails / tries
print(p)





