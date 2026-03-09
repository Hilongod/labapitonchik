from itertools import product

def f():
    alf = ['A', 'B', 'C', 'D', 'E']
    s = [
        ''.join(i)
        for i in product(alf, repeat = 5)
        if not (i[0] == 'E' and i[4] == 'A') #обрабатываем 1 буква не Е и ластовая не А
    ]
    return len(s)

print(f())
