#eulicid algorithm for gcd
#https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm#:~:text=The%20Algorithm,%3D%20B%E2%8B%85Q%20%2B%20R)
# If A = 0 then GCD(A,B)=B, since the GCD(0,B)=B, and we can stop.  
# If B = 0 then GCD(A,B)=A, since the GCD(A,0)=A, and we can stop.  
# Write A in quotient remainder form (A = B⋅Q + R)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)