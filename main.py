import random
import matplotlib.pyplot as plt

numbers = []

plt.ion()
fig, ax = plt.subplots()

for _ in range(100):
    numbers.append(random.randint(1,100))

for _ in range(len(numbers)-1):
    swapped = False
    for i in range(len(numbers)-1):
        if numbers[i] > numbers[i+1]:
            inbetween = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i+1] = inbetween
            if i % 10 == 0:
                if not plt.fignum_exists(fig.number):
                    plt.ioff()
                    exit()  
                plt.clf()
                plt.bar(range(len(numbers)),numbers)
                plt.pause(0.01)
            swapped = True
    if not swapped:
        break

plt.ioff() 