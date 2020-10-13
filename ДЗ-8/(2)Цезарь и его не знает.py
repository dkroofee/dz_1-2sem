num = int(input())
mess = input()
for i in mess:
    if i == ' ' or i == ',' or i == '.' or i == '!' or i == '?':
        print(i, end='')
    else:
        if (1040 <= ord(i) <= 1071 and ord(i) + num > 1071) or (1072 <= ord(i) <= 1103 and ord(i) + num > 1103):
            print(chr(ord(i) + num - 32), end='')
        else:
            print(chr(ord(i) + num), end='')