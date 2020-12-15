import os
import math


def main():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input'), 'r') as file:
        buses = file.read().split(',')
        data = [(int(bus[1]) - int(bus[0]) % int(bus[1]), int(bus[1])) for bus in enumerate(buses) if bus[1] != 'x']
        print(data)
        (a1, n1) = data.pop()
        while data:
            (a2, n2) = data.pop()
            m1, m2 = eea(n1, n2)
            a1, n1 = a1 * m2 * n2 + a2 * m1 * n1, n1 * n2

        return a1 % n1


def eea(r1, r2):  # extended euclidean algorithm
    q = 0
    s1 = 1
    s2 = 0
    t1 = 0
    t2 = 1
    while True:
        q2 = r1 // r2
        s = s1 - q2 * s2
        t = t1 - q2 * t2
        r1, r = r2, r1 - q2 * r2
        if r == 0:
            return s2, t2
        else:
            r2, q = r, q2
            s1, s2 = s2, s
            t1, t2 = t2, t


def is_pw_coprime(list):
    print(list)
    product = math.prod(list)
    lecomu = 1
    for item in list:
        print(lecomu)
        lecomu = lcm(lecomu, item)
    return product == lecomu


def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x


def lcm(x, y):
    return (x * y) // gcd(x, y)


if __name__ == "__main__":
    print(main())
