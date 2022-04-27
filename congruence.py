def congruence(a, b):
    n = abs(a-b)
    m = []
    for i in range(1,n+1):
        if n % i == 0:
            m.append(i)
    return m 