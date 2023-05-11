def more_than_five(a):
    return list(filter(lambda x: abs(x) > 10, a))

print(more_than_five([1, 11, 10, 0, 190]))