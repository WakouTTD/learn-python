# pythonは1行が80文字を超えると折り返せというルール
# 長い文字列連結でバックスラッシュ
s = 'aaaaaaaaaaaaaaa' + \
    'bbbbbbbbbbbbbbb'

print(s)

x = 1 + 1 + 1 + 1 + 1 + 1 + 1 + \
    1 + 1 + 1 + 1 + 1 + 1

print(x)

print('------------------')

# もしくはパレンティス

s = ('aaaaaaaaaaaaaaa' +
     'bbbbbbbbbbbbbbb')

print(s)

x = (1 + 1 + 1 + 1 + 1 + 1 + 1 +
     1 + 1 + 1 + 1 + 1 + 1)

print(x)
