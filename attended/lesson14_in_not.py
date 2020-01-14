y = [1, 2, 3]
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

a = 1
b = 2

# これはあまり推奨されない
if not a == b:
    print('Not equal')

# こう書くことが好ましい
if a != b:
    print('Not equal')

# じゃあ、どんな時にnotを使うか
is_ok = True

# これは好ましくない　notを使う
if not is_ok != False:
    print('hello')

if not is_ok:
    print('hello')

print('----------')

#is_ok = True
# 1でもif文はOK
is_ok = 'unko'

# 100でもOK -1でもOK strも値が入っていたらOK
# 0ならNG ''と空文字ならNG

if is_ok:
    print('OK!')
else:
    print('No!')

#if len(str) > 0: なんて判定をしなくて良いよ