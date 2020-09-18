# dæmi 3
def runa(m):
    if m == 1:
        print("1", end=" ")
        return 1
    else:
        rec = m + runa(m - 1)
        print(rec, end=" ")
        return rec

print("runa: ")
print(runa(5))

# dæmi 4

def thversumma(n):
    if not n:
        return 0
    else:
        return int(str(n)[0]) + thversumma(str(n)[1:])

print("þversumma: ", thversumma(1206))

# dæmi 5

def samnefnari(n, m):
    if n%m == 0:
        return m
    elif n%m == 1:
        return 1
    return samnefnari(m, n%m)

print("samnefnari (8,12): ", samnefnari(8,12))
print("samnefnari (3,13): ", samnefnari(3,13))
print("samnefnari (12,60): ", samnefnari(12,60))
