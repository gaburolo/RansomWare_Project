import os
import sys
import logging

from vignere_cipher import vignere_cipher
from key_engine import generate_random_key, generate_key_combinations


def name_backup(filename):
    f = filename.split('.')
    f.insert(len(f)-1, '_backup.')
    return ''.join(f)


def encrypt(filename, key_len):
    with open(filename, 'r') as f:
        content = f.read()

    with open(name_backup(filename), 'w') as f:
        f.write(content)

    secret_key = generate_random_key(key_len)
    encrypted_content, _key = vignere_cipher(content, secret_key)

    with open(filename, 'w') as f:
        f.write(str(encrypted_content))


def decrypt_bf(filename, key_len):
    with open(filename, 'r') as f:
        encrypted_content = f.read()

    with open(name_backup(filename), 'r') as f:
        original_content = f.read()

    for key in generate_key_combinations(key_len):
        decrypted_content, _key = vignere_cipher(encrypted_content, key)
        if original_content == str(decrypted_content):
            with open(filename, 'w') as f:
                f.write(str(decrypted_content))
            print(f'Decrypted with key: {"".join(key)}')
            break


def main():
    filename = str(sys.argv[1])
    key_len = int(sys.argv[2])

    encrypt(filename, key_len)
    decrypt_bf(filename, key_len)


if __name__ == '__main__':
    main()
