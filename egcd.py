import sys
import gcd

def egcd(a, b, s1=1, s2=0, t1=0, t2=1):
    if b == 0:
        return a, s1, t1
    q = a // b
    r = a % b
    s = s1 - s2 * q
    t = t1 - t2 * q
    return egcd(b, r, s2, s, t2, t)

if len(sys.argv) != 1:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print('By using Euclidians standard GCD Algorithm : ', gcd.gcd(a, b))
    print('By using Euclidians Extended GCD Algorithm : ',egcd(a, b))