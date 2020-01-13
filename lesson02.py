word = 'python'

print(word)
print(word[0])

# 同じ出力
print(word[5])
print(word[-1])

# slice
print(word[1:4])

# 同じ出力
print(word[:4])
print(word[:-2])


print(word[1:])

# sliceの始まりも終了も省略できる
print(word[:])


print('#########')
word = 'j' + word[1:]
print(word)


print('#########　index')
print(len(word))

