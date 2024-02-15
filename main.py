import webbrowser
from colorama import Fore

def print_banner():
    try:
        with open("banner.txt", 'r', encoding='utf-8') as file:
            banner_content = file.read()
            print(f"{Fore.RED}{banner_content}")
    except FileNotFoundError:
        print(f"Error: File 'banner.txt' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    print_banner()

address = input(f"{Fore.GREEN}Input Address or Coordinates: ")

URL = f"https://earth.google.com/web/search/{address}"

webbrowser.open(URL)

input("Press Enter to Exit. . .")