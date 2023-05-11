def discount_checker(threshold, *purchases):
    res = []
    for i in range(len(purchases)):
        if purchases[i] > threshold:
            res.append(i+1)
    return res