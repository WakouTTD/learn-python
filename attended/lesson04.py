# list

list = [1, 2, 3, 4, 5, 6, 7]

skip2 = list[::3]
print(skip2)

reverse = list[::-1]
print(reverse)

# nest
x = [['a', 'b', 'c'], [1, 2, 3, 4, 5, 6, 7, 8]]
print(x)
print(type(x))
print(x[1][2])
print(x[-1][-1])
print('--------------')
x[1][2:5] = ['C', 'D', 'E']
print(x)

# 2番目の配列の3,4,5番目を空にする
x[1][2:5] = []
print(x)

print('##############')

s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
s[0] = 'z'
print(s)
s[0] = 1
print(s)


