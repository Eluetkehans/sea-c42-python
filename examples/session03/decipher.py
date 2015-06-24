# This is the file for the deciphering partner.

alphabet = "abcdefghijklmnopqrstuvwxyz "

alphabet_list = list(alphabet)

# Copy and paste the cipher list from your partner below,
# instead of the empty list.
cipher_list = ['p', 'r', 't', 'h', 'a', 'w', 'k', 'd', 'v', 'f', 'u', ' ', 'b', 'z', 's', 'l', 'c', 'j', 'y', 'i', 'e', 'g', 'm', 'x', 'o', 'n', 'q']

# copy and paste the cipher_text from your partner in slack
# and assign it to the variable new_cipher_text
new_cipher_text = "mdpiqipyiayqraiiajqidpzqviqyba  y"

decrypt_text = ""

for y in new_cipher_text:
    index = cipher_list.index(y)
    decrypt_char = alphabet_list[index]
    decrypt_text += decrypt_char

print(decrypt_text)
