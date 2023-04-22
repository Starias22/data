import math

#Constantes

##pi

print('Pi:',math.pi)
##tau
print('2*Pi:',math.tau)
##e(Euler)
print('e:',math.e)
##inf(infinity)
print('+inf:',math.inf)
print('-inf:',-math.inf)

if math.inf>999945698712578:
    print('Of course')
##nan(not a number)

print('NaN:',math.nan)


# Arithmetical methods

## factorial

print('5!=',math.factorial(5))
print('0!=',math.factorial(0))

##gcd and lcm

print('gcd(10,20):',math.gcd(10,15))
print('gcd(3,-15):',math.gcd(3,-15))

print('lcm(10,20):',math.lcm(10,15))
print('lcm(3,-15):',math.lcm(3,-15))

## prod
print(math.prod([1,2,3,5,8]))

print(math.prod((45,66,-6,-8,-5,2)))


## fsom

print(math.fsum([45,66,-6,9,20,45]))

# Approximation functions

##ceil
print('ceil(5.4):',math.ceil(5.4))
print('ceil(5.7):',math.ceil(5.7))
print('ceil(5):',math.ceil(5))
print('ceil(-5.4):',math.ceil(-5.4))
print('ceil(-5.7):',math.ceil(-5.7))
print('ceil(-5.):',math.ceil(-5.))





##floor

print('floor(5.4):',math.floor(5.4))
print('floor(5.7):',math.floor(5.7))
print('floor(5):',math.floor(5))
print('floor(-5.4):',math.floor(-5.4))
print('floor(-5.7):',math.floor(-5.7))
print('floor(-5.):',math.floor(-5.))

##Trncate:trunc
print('trunc(5.4):',math.trunc(5.4))
print('trunc(5.7):',math.trunc(5.7))
print('trunc(5):',math.trunc(5))
print('trunc(-5.4):',math.trunc(-5.4))
print('trunc(-5.7):',math.trunc(-5.7))
print('trunc(-5.):',math.trunc(-5.))


# Enumeration function

## combination: comb(n,p)
print('C(10,5):',math.comb(10,5))
print('C(5,10):',math.comb(5,10))
print('C(10,0):',math.comb(10,0))

##permutation: A(n,p)

print('A(10,5):',math.perm(10,5))
print('A(5,10):',math.perm(5,10))
print('A(10,0):',math.perm(10,0))

# Power functions

## pow

print(math.pow(4, 3))
print(math.pow(-2,5))
print(math.pow(0.5,2))
print(math.pow(16,0.5))
print(math.pow(8,1/3))
print(math.pow(0.5,1.25))

## Natural exponent:exp

print(math.exp(2))
if math.exp(1)==math.e:
    print('Of course')

# Trigonometric functions red deg

##from radians to degrees

print('pi rad=',math.degrees(math.pi),'degrees')

## from degrees to radians
if math.tau==math.radians(360):
    print('2pi---360')

##sin
##cos
##tan

# Hyperbolic functions
# Reciprocal functions
##asin
##acos
##atan
##asinh
##acosh
##atanh


# Logarithmic functions

##Natural logarithm:log:ln(x) in math

print(math.log(100))
print(math.log(1))
print(math.log(2))
## Decimal logaritm:log10:log(x) in math
print(math.log10(100))
print(math.log10(1))
##log2:ln(x)/ln2 in math
print(math.log2(1))
print(math.log2(25))
##log1p:ln(1+x) in math
print(math.log1p(0))
print(math.log1p(1))


# Other functions

## square root: sqrt and isqrt
print(math.sqrt(3))
print(math.sqrt(9))

print(math.isqrt(25))
print(math.isqrt(3))

## Euclid distance:dist
print(math.dist([1,0],[4,math.sqrt(7)]))
print(math.dist((1,4,9,8),(0.56,-9.55,4,2)))
print(math.dist((-5,0.45,-25.55), [45,66,22]))

## Hypotense: hypot
print(math.hypot(3,4))
##Closeness of numbers:iclose
