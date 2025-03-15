#Project Goals
#You and your pen pal, Vishal, have been exchanging letters for some time now.
# Recently, he has become interested in cryptography and the two of you have started
# sending encoded messages within your letters.

def caesar_cipher_decrypt(ciphertext, shift):
    ciphertext = ""

    for char in ciphertext::
    if char.isalpha():
        is_uppercase = char.isupper()

        shifted_char = chr((ord(char) - shift) % 26 + ord('A')