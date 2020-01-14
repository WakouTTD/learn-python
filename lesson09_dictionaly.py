# 余談ですが、{}はブレイシーズの他にカーリーブラケットと言ったりもする

d = {'x': 10, 'y': 20}

print(d)
print(type(d))

print(str(d['x']))
print(str(d['y']))
d['x'] = 100
print(d)

# intだったところにstringを入れられる
d['x'] = 'XXXX'
print(d)
print(type(d['x']))

d['z'] = 200
print(d)
d[1] = 10000
print(d)

# dictは別の生成方法もある
new_d = dict(a=10, b=20)
print(new_d)

# tupleでもできる
new_d = dict([('c', 10), ('d', 20)])
print(new_d)
print('--------------------')

print(help(d))
d.keys()

print('--------------------')

# listと同じく参照渡しに注意
x = {'a': 1}
y = x
y['a'] = 1000
print(x)
print(y)

print('--------------------')
# listと同様、dictもcopyメソッドを使えば良い
x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)

print('--------------------')
fruits = {
    'apple': 100,
    'banana': 200,
    'orange': 300,
}

# dictは内部的にhash tableを使っているのでlistで2次元配列にするより早い
print(fruits['apple'])
