def f():
    a = 4**511 + 2**511 - 511
    return bin(a).count('1')
print(f())