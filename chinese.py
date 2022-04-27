from numpy import multiply
from gcd import gcd
from inverse import inverse
from itertools import combinations
from math import prod

m = [5, 11, 17]
a = [2, 3, 5]

for i in combinations(m, 2):
    assert gcd(i[0], i[1]) == 1
print('all good')

M = prod(m) 
print(M)

m0 = M // m[0]
m1 = M // m[1]
m2 = M // m[2]

m0_inverse = inverse(m0, m[0])
m1_inverse = inverse(m1, m[1])
m2_inverse = inverse(m2, m[2])

print(m0, m1, m2)
print(m0_inverse, m1_inverse, m2_inverse)

x = a[0]*m0*m0_inverse + a[1]*m1*m1_inverse + a[2]*m2*m2_inverse

print(x)