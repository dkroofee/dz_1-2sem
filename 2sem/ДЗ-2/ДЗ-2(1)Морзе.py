alpha = {
    "A": ".-", "B": "-...", "W": ".--", "G": "--.", "D": "-..", "E": ".", "V": "...-",
    "Z": "--..", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--",
    "N": "-.", "O": "---", "P": ".--.", "R": ".-.", "S": "...", "T": "-", "U": "..-",
    "F": "..-.", "H": "....", "C": "-.-.", "Q": "--.-", "Y": "-.--", "X": "-..-"
}
def encode_to_morse(text):
    b = []
    for i in text:
        b.append(alpha[i])
    return ' '.join(b)

def decode_from_morse(code):
    b = []
    code1 = code.split(' ')
    for i in code1:
        for v, k in alpha.items():
            if k == i:
                b.append(v)
    return ''.join(b)



def main():
    t = input("Здраствуйте. Вы хотите кодировать или декодировать код Морзе? ")
    if t.lower() == 'декодировать':
        code = input("Вставьте код: ")
        return decode_from_morse(code)
    if t.lower() == 'кодировать':
        text = input("Вставьте текст: ")
        return encode_to_morse(text)


print(main())