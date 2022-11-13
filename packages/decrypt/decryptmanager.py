from base64 import b64decode

class DecryptManager:
    
    def __init__(self):
        self.__decrypted = ''
        pass
    
    
    def decrypt(self, code):
        decoded = b64decode(code).decode('utf-8')
        self.__set_decrypted(decoded)
        pass
        
    
    def __set_decrypted(self, decoded):
        self.__decrypted = decoded
    
    def get_decrypted(self):
        return self.__decrypted