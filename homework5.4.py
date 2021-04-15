import itertools
import math

for p in itertools.permutations('1234', 3):
    print(''.join(str(x) for x in p))
print()
print(f'Количество размещений: {math.factorial(4)/math.factorial(4-3)}')
print()

for p in itertools.combinations('1234', 3):
    print(''.join(str(x) for x in p))
print()
print(f'Количество сочетаний: {int(math.factorial(4)/(math.factorial(3) * math.factorial(4-3)))}')
print()

for p in itertools.permutations('12345', 2):
    print(''.join(str(x) for x in p))
print()
print(f'Количество размещений: {int(math.factorial(5)/ math.factorial((5-2)))}')
print()

for p in itertools.combinations('12345', 2):
    print(''.join(str(x) for x in p))
print()
print(f'Количество сочетаний: {int(math.factorial(5)/(math.factorial(2) * math.factorial(5-2)))}')
print()
