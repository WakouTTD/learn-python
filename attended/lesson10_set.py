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

print('----------------')

my_friends = {'A', 'C', 'D'}
A_friends = {'B', 'D', 'E', 'F'}
# 共通の友達を＆で探せる
print(my_friends & A_friends)

f = ['apple', 'banana', 'apple', 'banana']
# どんな種類の果物か listからsetに型変換して実行
kind = set(f)
print(kind)
