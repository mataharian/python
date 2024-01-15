def MonoalphabeticCipher(plaintext, key):
    letters = "abcdefghijklmnopqrstuvwxyz"
    key = key.lower()
    chipertext = ''

    for letter in plaintext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                chipertext += letter
            else:
                chipertext += key[index]
        else:
            chipertext += ' '
    return chipertext

key = "dkvqfibjwpescxhtmyauolrgzn"
print()
print('=====MONOALPHABETIC CIPHER=====')
print()
text = input('Plaintext = ')
ciphertext = MonoalphabeticCipher(text, key)
print(f'Ciphertext = {ciphertext}')