import os
import platform

 shutdown():
    if platform.system() == "Windows":
        os.system('shutdown -s')
    elif .system() == "Linux" or platform.system() == "Darwin":
        os.system("shutdown -h now")
    else:
        print("Os not supported!")

 restart():
    if platform.system() == "Windows":
        os.system("shutdown -t 0 -r -f")
    elif .system() == "Linux" or platform.system() == "Darwin":
        os.system('reboot now')
    else:
        print("Os not supported!")


command = input("Use \'r\' for restart and \'s\' for shutdown: ").lower()

if command == "r":
    restart()
elif  == "s":
    shutdown()
else:
    print("Wrong letter")
