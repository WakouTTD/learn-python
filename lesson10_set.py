a = {1, 2, 3, 3, 3, 3, 3, 8, 9, 10}
print(type(a))
print(a)

b = {8, 9, 10, 11}

a = a - b

print(a)

b = b - a

print(b)
print('----------------')

a = {1, 2, 3, 3, 3, 3, 3, 8, 9, 10}
b = {8, 9, 10, 11}
# aにもbにもあるもの
print(a & b)
# aかbにあるもの
print(a | b)
# aかbにあるが、重複してないもの
print(a ^ b)
