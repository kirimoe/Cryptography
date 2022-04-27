import egcd, sys

def inverse(a,b):
    g, s, t = egcd.egcd(a,b)
    if g == 1 and s < 0:
        return s + b

    elif g == 1:
        return s

    else:
        print('Not solvable')

if len(sys.argv) != 1:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(f'Modulo inverse of {a}, {b} is {inverse(a,b)}')