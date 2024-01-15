def AutokeyCipher(plaintext, key):
    letters = "abcdefghijklmnopqrstuvwxyz"
    key = key.lower()
    key_length = len(key)
    chipertext = ''

    running_key = key + plaintext.lower()

    for i, letter in enumerate(plaintext):
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                chipertext += letter
            else:
                key_letter = running_key[i]
                key_index = letters.find(key_letter)
                new_index = (index + key_index) % 26
                chipertext += letters[new_index]
        else:
            chipertext += ' '
    return chipertext

print()
print('========AUTOKEY CIPHER=========')
print()
key = str(input('Key = '))
text = input('Plaintext = ')
ciphertext = AutokeyCipher(text, key)
print(f'Ciphertext = {ciphertext}')
