import random
import string
import time
import sys
import os
from colorama import Fore, Style, init

# Renkleri başlat
init(autoreset=True)

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def get_timestamp():
    # Loglar için saat ekleyelim, videoda profesyonel durur
    return time.strftime("%H:%M:%S")

def generate_roblox_code():
    # Roblox genelde 10 haneli rakam (PIN) veya 12-16 haneli karışık kod kullanır.
    # Biz videoda karmaşık durması için 12 haneli karışık format (XXXX-XXXX-XXXX) yapalım.
    part1 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    part2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    part3 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return f"{part1}-{part2}-{part3}"

def slow_print(text, delay=0.05):
    # Yazıların daktilo gibi akması için
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def banner():
    print(Fore.RED + Style.BRIGHT + """
    ███╗   ███╗ ██████╗ ██████╗ ██████╗ ████████╗███████╗██╗   ██╗██╗  ██╗
    ████╗ ████║██╔═══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██╔════╝██║   ██║╚██╗██╔╝
    ██╔████╔██║██║   ██║██████╔╝   ██║      ██║   █████╗  ██║   ██║ ╚███╔╝ 
    ██║╚██╔╝██║██║   ██║██╔══██╗   ██║      ██║   ██╔══╝  ██║   ██║ ██╔██╗ 
    ██║ ╚═╝ ██║╚██████╔╝██║  ██║   ██║      ██║   ███████╗╚██████╔╝██╔╝ ██╗
    ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═╝
    """ + Fore.WHITE + "    >>> ROBLOX GIFT CARD GENERATOR & CHECKER TOOL <<<\n")

def main():
    clear_screen()
    banner()
    
    slow_print(Fore.YELLOW + "[?] Initializing connection to database...", 0.03)
    time.sleep(1)
    print(Fore.GREEN + "[OK] Connected!\n")
    
    try:
        # Kullanıcıdan adet bilgisi al
        target_amount = int(input(Fore.CYAN + f"[{get_timestamp()}] Enter amount of codes to generate: " + Fore.WHITE))
        
        # Slow Mode ayarı (Check hızı)
        print(Fore.CYAN + f"[{get_timestamp()}] Select Mode:")
        print(Fore.WHITE + "1. Fast Mode (Check speed: 0.1s)")
        print(Fore.WHITE + "2. Slow Mode (Check speed: 1.5s - More Realistic)")
        mode_choice = input(Fore.CYAN + "Choice (1/2): " + Fore.WHITE)
        
        delay_time = 1.5 if mode_choice == '2' else 0.1
        
        print("\n" + Fore.YELLOW + "--- STARTING BRUTEFORCE PROCESS ---\n")
        time.sleep(1)
        
        valid_found = 0
        
        for i in range(target_amount):
            code = generate_roblox_code()
            
            # Ekrana bas: Checking...
            sys.stdout.write(Fore.WHITE + f"[{i+1}/{target_amount}] Checking: {code} ... ")
            sys.stdout.flush()
            
            # Check işlemini simüle et (Beklet)
            time.sleep(delay_time)
            
            # %1 ihtimalle 'Working' çıksın (Video için heyecanlı olsun)
            is_valid = random.random() < 0.01
            
            if is_valid:
                # Satırı silip sonucu yaz
                print(Fore.GREEN + Style.BRIGHT + " [ VALID ] $10")
                valid_found += 1
                with open("hits.txt", "a") as f:
                    f.write(f"{code} | $10\n")
            else:
                print(Fore.RED + " [ INVALID ]")
        
        print("\n" + "="*50)
        print(Fore.CYAN + f"Process Complete.")
        print(Fore.GREEN + f"Total Hits: {valid_found}")
        print(Fore.WHITE + "Valid codes saved to 'hits.txt'")
        print("="*50)

    except ValueError:
        print(Fore.RED + "Please enter a valid number!")
    except KeyboardInterrupt:
        print(Fore.RED + "\nProcess stopped by user.")

if __name__ == "__main__":
    main()
