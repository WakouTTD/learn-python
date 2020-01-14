is_empty = None
# print(help(is_empty))

# あまり推奨されない
if is_empty == None:
    print('None!!!')

# isを使う
if is_empty is None:
    print('is None!!!')

# is notを使う
is_empty = 'aaa'
if is_empty is not None:
    print('is not None!!!')

print('----------')
# is はオブジェクトが同一かどうかを判定するもの
# is はNoneか否かを判定する際に使用する、と記憶するべき

# Trueになる
print(1 == True)

# Falseになる
print(1 is True)

# Trueになる
print(True is True)

# Trueになる
print(None is None)

# Falseになる
print('' is None)

