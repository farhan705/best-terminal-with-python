from subprocess import getoutput as get
import colorama

name = get("echo %username%")
get("cls")
print("farhan terminal")

while True:
    user = input(colorama.Fore.GREEN+"pc@"+name+"$ ")
    if user =="":
        print(colorama.Fore.RED+"Not Command")
    else:
        anwser = get("powershell "+user)
        print(colorama.Fore.BLUE+anwser)
