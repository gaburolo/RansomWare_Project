from math import fmod

# The minimum and maximum valid char, ascii table defined order
ASCII_MIN = ord(' ')
ASCII_MAX = ord('~')


def vignere_cipher(content, key):
    """
    > We take the difference between the index of the letter in the content and the index of the letter
    in the key, then we use the inverse of that difference to find the letter in the alphabet

    :param content: The string to be encrypted
    :param key: 'abcdefghijklmnopqrstuvwxyz'
    :return: the encrypted/decrypted message and the key used to encrypt/decrypt it.
    """

    # Generate a string of all the possible chars
    alpha = ''

    for printable in range(ASCII_MIN, ASCII_MAX+1):
        alpha = alpha + chr(printable)

    # Ensure the key is at least as long as the ciphertext by cat'ing it
    while len(key) < len(content):
        key = key + key
        key = key[0:len(content)]

    out = ''
    for i in range(len(content)):
        index_from_phrase = (ord(content[i])-ASCII_MIN)
        index_from_key = ord(key[i]) - ASCII_MIN
        difference = (index_from_phrase - index_from_key)

        # We want the sign of the dividend so we use fmod()
        # Use the inverse of this result (I'm not certain why - is there a simpler way?
        intersect = int(fmod(index_from_phrase - index_from_key,
                        (ASCII_MAX - ASCII_MIN + 1)) * -1)

        letter = alpha[intersect]
        out += letter

    return out, key
