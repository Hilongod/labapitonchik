def f(n):
    s = []
    for i in range(2, n): #перебираем
        if n % i == 0: #если i делится на n без остатка — добавляем в список
            s.append(i)
        if len(s) == 5: #перебираем до 5 делителей
            break
    return s

def f1():
    res = []
    n = 200_000_001
    while len(res) < 5: #пока не нашли 5 подходящих чисел
        s = f(n)
        if len(s) == 5:  #если делителей ровно 5 (иначе M(N) = 0)
            m = s[0] * s[1] * s[2] * s[3] * s[4] #вычисляем произведение 5 делителей
            if 0 < m < n: #если 0 < m < n, то добавляем результат
                res.append((n, m))
        n += 1
    return res

for n, m in f1():
    print(f"N={n}, M(N)={m}")