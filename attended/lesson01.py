
"""
print("hello")
"""
from os.path import sep

"""
num = 1
name = 'Mike'
is_ok = True

# 1 <class 'int'>と出力される
print(num, type(num))

# Mike <class 'str'>と出力される
print(name, type(name))

# True <class 'bool'> と出力される
print(is_ok, type(is_ok))
"""

"""
num = 1
name = 'Mike'
num = name
# Mike <class 'str'>が出力される
print(num, type(num))
"""

"""
# 型変換
num: int = 1
name: str = '1'
new_num = int(name)
print(new_num, type(new_num))
"""


"""
print('Python')
# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
print('Hi', 'Mike', sep=' ', end='\n')

# 複数の文字列をまとめて出力する
print('This', 'is', 'a', 'chair.')
# => This is a chair.

# 文字列以外のオブジェクトを出力する
print('Total: ', 1000)
# => Total:  1000

print('List: ', [3, 5, 7])
# => List:  [3, 5, 7]

print('---------------------')
"""

"""
print(2 + 2)

print(round(4.1415151515, 2))

print('---------------------')

import math

print("math.sqrt(25):" + str(math.sqrt(25)))

print("math.log2(10):" + str(math.log2(10)))

print('help:' + str(help(math)))
"""


print("I don't know")
print("say \"I don't know\" ")
print('say "I don\'t know" ')
print('I don\'t know')

# raw データという意味のr
print(r'C:\name\name')

# line1前とline3後が改行される
print("#############")
print("""
line1
line2
line3
""")
print("#############")

# line1前とline3後が改行されない
print("#############")
print("""\
line1
line2
line3\
""")
print("#############")

# Hi.Hi.Hi.mike
print('Hi.' * 3 + 'Mike')

# シングルクォートで囲む物をリテラルと呼ぶ
# プラスでつなげてもつなげなくても同じ出力
print('Py' + 'thon')
print('Py' 'thon')
print("Py" + "thon")
print("Py" "thon")


s = ('aaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbb')
print(s)

# 同じ出力
ss = 'aaaaaaaaaaaaaaaaa'\
     'bbbbbbbbbbbbbbbbb'
print(ss)


"""
"""

"""
"""

"""
"""

"""
"""

"""
"""

