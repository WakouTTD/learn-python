num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
print(x, y)

# これ実はtuple
x, y = 10, 20
print(x, y)

# たとえばこんなコードだと見やすい
min, max = 0, 100
print(min, max)

# やりすぎると読みにくい
a, b, c, d, e, f = 'Mike', '1', '1', '1', 'e', 'f'

# 変数の値の入れ替えがtupleで楽に書ける
i = 10
j = 20
tmp = i
i = j
j = tmp
print(i, j)

print('-----------')

a = 100
b = 200
print(a, b)
# tupleによる入れ替え
a, b = b, a
print(a, b)

print('-----------')

chose_from_two = ('A', 'B', 'C')

answer = []
answer.append('A')
answer.append('C')

print(chose_from_two)
print(answer)
