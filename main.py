def diophantine(a, b, c):
    if c % gcd(a, b) != 0:
        return None
    x, y = 0, 1
    last_x, last_y = 1, 0
    while b != 0:
        q = a // b
        a, b = b, a - q * b
        x, last_x = last_x - q * x, x
        y, last_y = last_y - q * y, y
    return last_x * (c // gcd(a, b)), last_y * (c // gcd(a, b))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Misol uchun test
a = 12
b = 15
c = 3
print(diophantine(a, b, c))
```

Kodda `diophantine` funksiyasi Diophantine tenglamani yechish uchun ishlatiladi. Uning ichida `gcd` funksiyasi ikki sonning kattaligini topish uchun ishlatiladi. Funksiya `c` ni `a` va `b` ning kattaligiga bo'lishi sharti bilan ishlaydi. Agar shart bo'lmagan bo'lsa, funksiya `None` qiymatini qaytaradi.
