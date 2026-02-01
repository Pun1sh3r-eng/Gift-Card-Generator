import requests  
import random  
import colorama  
from colorama import Fore, Style

colorama.init()

def generate_giftcard():  
    """Roblox formatında sahte bir gift card kodu oluşturur."""  
    code = f"{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"  
    return code

def inject_roblox_servers(code):  
    """Roblox'un sunucularına sahte bir istek gönderir."""  
    url = "https://roblox.com/api/giftcard/validate"  # BU URL ÇALIŞMAYACAKTIR!  
    headers = {"Content-Type": "application/json"}  
    data = {"code": code}  
      
    try:  
        response = requests.post(url, headers=headers, json=data)  
        response.raise_for_status()  
        result = response.json()  
          
        if result.get("valid"):  
            return "Çalışıyor"  
        else:  
            return "Geçersiz"  
    except requests.exceptions.RequestException as e:  
        print(Fore.YELLOW + f"Hata: {e}" + Style.RESET_ALL)  
        return "Hata"

def main():  
    """Ana fonksiyon."""  
    num_codes = int(input("Kaç adet gift card kodu oluşturmak istiyorsunuz? "))  
      
    for _ in range(num_codes):  
        code = generate_giftcard()  
        status = inject_roblox_servers(code)  
          
        if status == "Çalışıyor":  
            print(Fore.GREEN + f"Kod: {code} - {status}" + Style.RESET_ALL)  
        elif status == "Geçersiz":  
            print(Fore.RED + f"Kod: {code} - {status}" + Style.RESET_ALL)  
        else:  
            print(Fore.YELLOW + f"Kod: {code} - {status}" + Style.RESET_ALL)

if __name__ == "__main__":  
    main()  
