s = 'My name is Mike. Hi Mike.'
print(s)
is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('X')
print(is_start)

print("################")

print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))

# 最初以外は小文字に変換
print(s.capitalize())
# 全てのwordの頭を大文字に変換
print(s.title())
# 大文字化
print(s.upper())
# 小文字化
print(s.lower())

# リプレイス
print(s.replace('Mike', 'Nancy'))

s = 'My name is {name} {family}. Watasi ha {family} {name}'.format(name='太郎', family='山田')
print(s)

# python3.6からformatではなくf-string
family = '鈴木'
name = '一郎'
s = f'My name is {name} {family}. Watasi ha {family} {name}'
print(s)
