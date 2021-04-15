import random
# найдем вероятность того, что из 3 попыток дважды выпадет орел. Всего будет 8 комбинаций, из которых нам
# подойдут 3, то есть вероятность будет 3/8 = 0.375

experiments = 10000
tries = 3
probability = 0

while experiments > 0:
    samples = [random.randint(0, 1) for i in range(tries)]
    heads = samples.count(0)
    tails = samples.count(1)
    if heads == 2:
        probability += 1
    experiments -= 1
print(probability/10000)

