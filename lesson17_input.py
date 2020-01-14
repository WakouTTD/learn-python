# input 関数は対話型スクリプトを作る時によくwhileとセットで使う
while True:
    word = input('Enter:')
    if word == 'ok':
        break
    print('next')

