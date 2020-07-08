import random, time

#in order
print()
array = []
for i in range(100):
    array.append(i)
print(array)

#reversed order
print()
array = []
for i in reversed(range(100)):
    array.append(i)
print(array)

#shuffled unique
print()
array = []
for i in reversed(range(100)):
    array.append(i)
random.shuffle(array)
print(array)

#random
print()
array = []
for i in range(100):
    array.append(random.randint(0,100))
print(array)

#Timing
print()
start = time.time()
print("hello")
end = time.time()
print('Elapsed time: '+str(end - start))