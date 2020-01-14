count = 0

while count < 5:
    print(count)
    count += 1

count = 0
while True:
    if count >= 5:
        break

    if count == 2:
        print('continue')
        count += 1
        continue

    print(count)
    count += 1

print('-----------')

count = 0
while count < 5:
    print(count)
    count += 1
else:
    print('done')

print('-----------')

count = 0
while count < 5:
    if count == 1:
        break
    print(count)
    count += 1
else:
    print('done')
