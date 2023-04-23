import numpy
import numpy as np

arr=['Welcome ','How ']
arr2=['bro','are you?']

print(np.char.add(arr,arr2))
print(np.char.multiply('Hello',5))
print(np.char.multiply(arr,3))

print(np.char.center('I love Python',30,'*'))

print(np.char.upper('welcome my Dear'))
print(np.char.lower('welcome my Dear'))
print(np.char.capitalize('welcome my dear'))
print(np.char.title('welcome my dear'))

print(np.char.split("Welcome To you bro"),sep = " ")
print(np.char.splitlines("Welcome\nTo\nJavatpoint"))



var='      I love programming     '
print(np.char.center(var, 80,'*'))

print(np.char.center(np.char.strip(var), 80,'*'))

print(np.char.join(':','HM'))

print(np.char.replace('I love you','love','hate'))
