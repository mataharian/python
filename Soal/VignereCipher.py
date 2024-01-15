def VigenereCipher(plaintext, key):
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
                new_index = (index + key_index) % 26
                chipertext += letters[new_index]
        else:
            chipertext += ' '        
    return chipertext

print()
print('========VIGNERE CIPHER=========')
print()
key = str(input('Enter the key : '))
text = input('Enter the plaintext: ')
ciphertext = VigenereCipher(text, key)
print(f'Ciphertext: {ciphertext}')
