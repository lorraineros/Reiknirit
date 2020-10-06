import time
import random

start = time.time()
start2 = time.time()
#start3 = time.time()

# dæmi 1
"""
a. O(n) = fallið keyrir n sinnum fyrir hvert stak

b. O(n^2) = fallið keyrir n sinnum í öðru veldi t.d. bubblesort og selection sort.

c. O(n*log(n)) = þýðir að fallið keyri log(n) sinnum.

"""

# dæmi 2

def SelectionSort(Arr):
    for i in range(len(Arr)):
        min_idx = i
        for j in range(i + 1, len(Arr)):
            if Arr[min_idx] > Arr[j]:
                min_idx = j
        Arr[i], Arr[min_idx] = Arr[min_idx], Arr[i]

    return Arr

A = random.sample(range(1, 10001), 10000)
print("______________________________________________________________")
print("--------------------Dæmi 2----------------------")
print("Unsorted Array")
print(A)

print("--------------------------------------------------------------")
SelectionSort(A)
print("Sorted array")
print(A)
print("%f seconds" % (time.time() - start))
print("--------------------------------------------------------------")
print("Python Sorted array")
print(sorted(A))
print("%f seconds" % (time.time() - start2))
print("______________________________________________________________")

# dæmi 3
print("--------------------Dæmi 3--------------------")
print("Stafrof")
def stafrof(ord):
    res = ''.join(sorted(ord))
    print(res)

moo="pqowieurytlaksjdhfgmnbvcxz"
stafrof(moo)
print("______________________________________________________________")

# dæmi 4

"""
a) Fallið tekur inn lista af tölum og raðar tölunum frá minnstu til hæstu

b) counting sort

c) O(n+k)
"""


# dæmi 5

print("--------------------Dæmi 5--------------------")
start3 = time.time()

def setja_inn(listi, tala):
    if len(listi) == 0:
        listi.append(tala)
        return listi
    for i in range(0, len(listi) - 1):
        if tala <= listi[i]:
            listi.insert(i, tala)
            return listi
    else:
        listi.append(tala)
        return listi

listi = [2,3,3,5,6,7,9,10]
print("Listi",listi)

n = input("Sláðu inn tölu:")
print(setja_inn(listi, int(n)))
print("%f seconds" % (time.time() - start3))
print("______________________________________________________________")
