#Python challenge to sort a number array from smallest to largest
import random

numbers = []
for i in range(10):
    x = random.randint(1,101)
    numbers.append(x)
    print(x)
print(numbers)

for i in range (len(numbers)):
    for j in range (len(numbers)):
        if numbers[i] < numbers[j]:
            temp = numbers[j]
            numbers[j] = numbers[i]
            numbers[i] = temp
print(numbers)
