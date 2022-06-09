# Python
import os
import sys

# Algorithm engines
from vignere_cipher import vignere_cipher
from key_engine import generate_random_key, generate_key_combinations
from cpu_stats import cpu_usage


def name_backup(filename):
    """
    It takes a filename, splits it into a list of strings, inserts '_backup.' into the list, and then
    joins the list back into a string

    :param filename: the name of the file to be backed up
    :return: the filename with '_backup' inserted before the file extension.
    """
    f = filename.split('.')
    f.insert(len(f)-1, '_backup.')
    return ''.join(f)


def encrypt(filename, key_len):
    """
    It reads the content of the file, writes it to a backup file, generates a random key, encrypts the
    content with the key, and writes the encrypted content to the original file

    :param filename: the name of the file to encrypt
    :param key_len: The length of the key to be used for encryption
    """
    with open(filename, 'r') as f:
        content = f.read()

    with open(name_backup(filename), 'w') as f:
        f.write(content)

    secret_key = generate_random_key(key_len)
    print('-'*60)
    print(f'Encrypting with key of size: {key_len}')
    print(f'Generated key: {secret_key}\n')
    encrypted_content, _key = vignere_cipher(content, secret_key)

    with open(filename, 'w') as f:
        f.write(str(encrypted_content))


@cpu_usage
def decrypt_bf(filename, key_len):
    """
    It reads the encrypted file, reads the original file, and then tries every possible key combination
    until it finds the one that decrypts the encrypted file to the original file

    :param filename: the name of the file to be decrypted
    :param key_len: The length of the key used to encrypt the file
    """
    with open(filename, 'r') as f:
        encrypted_content = f.read()

    with open(name_backup(filename), 'r') as f:
        original_content = f.read()

    count = 0
    for key in generate_key_combinations(key_len):
        count+=1
        sys.stdout.write('\033[F')
        print(f'Proven key: {"".join(key)} ... [{count}/{26**key_len}]')
        decrypted_content, _key = vignere_cipher(encrypted_content, key)
        if original_content == str(decrypted_content):
            with open(filename, 'w') as f:
                f.write(str(decrypted_content))
            print(f'Decrypted with key: {"".join(key)}')
            break


def main():
    """
    It takes a filename and a key length as arguments, encrypts the file, and then decrypts it using a
    brute force method
    """
    filename = str(sys.argv[1])
    key_len = int(sys.argv[2])

    encrypt(filename, key_len)
    decrypt_bf(filename, key_len)

    os.remove(name_backup(filename))


if __name__ == '__main__':
    main()
