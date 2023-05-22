import random
list=[]
sum=0
for i in range (10):
    num = range(1, 10)
    num_random =int(random.choice(num))
    list.append(num_random)
    sum += list[i]

print(list)
print(sum)