# Create a program that generates 100 random numbers and find the frequency of each number
import random
x = random.choices(range(0,500), k=100)
print(x)
frequency_dict = {}
for number in x:
    if number in frequency_dict:
        frequency_dict[number] +=1
    else:
        frequency_dict[number] = 1
for number,frequeny in frequency_dict.items():
    print(f" {number} is repeated {frequeny} times")


