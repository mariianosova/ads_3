def f(a):
    odds = []
    for i in a:
        if i % 2 == 1:
            odds.append(i)
    for i in range(len(a)):
        if a[i] % 2 == 1:
            a[i] = odds.pop()
    return a

print(f([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))