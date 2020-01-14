i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('j = ', j)
# 参照渡しだから、iの値も変わってしまう
print('i = ', i)

x = [1, 2, 3, 4, 5]
y = x.copy()
# このcopyと同様のことは[:]でもできる
# y = x[:]

y[0] = 200
print('y=', y)
print('x=', x)

print('---------------')

X = 20
Y = X
Y = 5
print(id(X))
print(id(Y))
print(Y)
print(X)

print('--------------- 配列はcopyしないと参照渡しになる')

X = ['a', 'b']
Y = X
Y[0] = 'p'
# 同じidになる
print(id(X))
print(id(Y))
print(Y)
print(X)
