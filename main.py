import random

numbers = []

for _ in range(100):
    numbers.append(random.randint(1,100))

for _ in range(len(numbers)-1):
    swapped = False
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            inbetween = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i+1] = inbetween
            swapped = True
    if not swapped:
        break

print(numbers)