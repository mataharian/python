def BeaufortCipher(plaintext, key):
    letters = "abcdefghijklmnopqrstuvwxyz"
    key = key.lower()
    key_length = len(key)
    chipertext = ''
    for i, letter in enumerate(plaintext):
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                chipertext += letter
            else:
                key_letter = key[i % key_length]
                key_index = letters.find(key_letter)
                new_index = (key_index - index) % 26
                chipertext += letters[new_index]
        else:
            chipertext += ' '
    return chipertext


print()
print('=======BEAUFORT CIPHER=========')
print()
key = str(input('Key = '))
text = input('Plaintext = ')
ciphertext = BeaufortCipher(text, key)
print(f'Ciphertext = {ciphertext}')
