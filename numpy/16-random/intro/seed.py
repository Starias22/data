import numpy.random as rd
rd.seed(42)
#Seed must be between 0 and 2**32 - 1
# generate 5 random integers between 0 and 9
random_integers = rd.randint(0, 10, size=5)

print(random_integers)
# Output: [6 3 7 4 6]

rd.seed(42)

# generate 5 random integers between 0 and 9
random_integers = rd.randint(0, 10, size=5)

print('from seed(42)',random_integers)
# Output: [6 3 7 4 6]

rd.seed(0)

# generate 5 random integers between 0 and 9
random_integers = rd.randint(0, 10, size=5)

print('from seed 0',random_integers)
# Output: [5 0 3 3 7]

rd.seed(1)

# generate 5 random integers between 0 and 9
random_integers = rd.randint(0, 10, size=5)

print('from seed 1',random_integers)
# Output: [5 8 9 5 0]

rd.seed(0)
print(rd.randint(10))

rd.seed(42)
print(rd.randint(10))

rd.seed(0)
print(rd.rand())

