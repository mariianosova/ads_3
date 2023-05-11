one = 10
two = 55
three = ""

def roman():
    global one, two, three
    s = one + two
    num = [1, 4, 5, 9, 10, 40, 50, 90,
		100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
		"L", "XC", "C", "CD", "D", "CM", "M"]

    for i in range(len(sym) - 1, -1, -1):
        cnt = s // num[i]
        s %= num[i]
        for _ in range(cnt):
            three += sym[i]
