r = [1, 2, 3, 4, 1, 2, 3]
print(r)

print(r.index(3))
print(r)
print(r.remove(1))
print(r)
print(r.pop(0))
print(r)
print(r.pop(0))

#r.delete

print('----------------')
r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r)
# 3を探してください
print(r.index(3))
# 4文字目以降から3を探してください
print(r.index(3, 3))
print('----------------　if')

if 3 in r:
    print('3 exist')
if 100 in r:
    print('100 exist')

print('----------------　sort')
r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)


print('----------------　split')
s = 'My name is Mike'
to_split=s.split(' ')
print(to_split)
# 元に戻す
x = ' '.join(to_split)
print(x)











