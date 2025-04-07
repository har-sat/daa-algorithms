def karat(x, y):
    if x < 10 or y < 10:
        return x * y
    
    m = max(len(str(x)), len(str(y)))
    m2 = m // 2

    a = x // (10**m2)
    b = x % (10**m2)
    c = y // (10**m2)
    d = y % (10**m2)

    A = karat(a, c)
    C = karat(b, d)
    B = karat(a + b, c + d)

    return A * (10 ** (2 * m2)) + (B - A - C) * (10**m2) + C


a = float(input())
b = float(input())

scale = 10**3
a_int = int(a * scale)
b_int = int(b * scale)

output = round(karat(a_int, b_int) / (scale * scale), 3)

print(output)
