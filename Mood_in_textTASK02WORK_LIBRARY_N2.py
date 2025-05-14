from colorama import Fore, init
import emoji
init()
mood_choise = int(input("1 joyful mood \n2 grief mood \n3 excited mood \n4 exhausted mood \nhi!, How are you today:"))
if mood_choise == 1:
    print(U+5350(Fore.Orange + ":"))