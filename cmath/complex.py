
z=4+5j
print('z:',z)
print(type(z))

z=45.45-20j
print(z)
z=4j
print(z)

z=20
print(z)
z=45+0j
print(z)
z=complex(20)
print(z)
z=complex()
print(z)

print(4+5j==4+5j)
print(2+6j==2+4j)
print(4-5j!=3-4j)

print(2==2+0j)

print(4+5j+6+9j)
print(4-5j+3j-8)

z1=4+4j
z2=2+8j
print('z1*z2:',z1*z2)
print('z1/z2:',z1/z2)
print('4*z1:',4*z1)
print('-8/z2:',-8/z2)
print('z2/6.5:',z2/6.5)


z=complex(3.8,4)
print(z)

print(isinstance(z,complex ))
print(isinstance(7,complex ))

import numbers
print(isinstance(z,numbers.Complex ))
print(isinstance(7,numbers.Complex ))

print(issubclass(numbers.Real,numbers.Complex ))
print(issubclass(numbers.Real,complex ))

print(z.real)
print(z.imag)

print(z.conjugate())
print(z.conjugate().conjugate()==z)

z=4+1j
print('z²:',z**2)
print(':',z**(1/3))
print(2**z)
print(z**(2+4j))
print(z**z)

print(abs(45))
print(abs(-45))
print(abs(45j))
print(abs(-20+45j))



