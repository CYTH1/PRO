import os, platform, time
os.system('clear')
print('checking updates')
os.system('git pull')
print('first allow permations (y)')
os.system('termux-setup-storage')
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    print("\n\x1b[1;92m Congratulations ! Your Device Support This Tool")
    from DUMP import main
    main_menu()
elif bit == '32bit':
    print("\x1b[1;91mSorry Brother Your Mobile Not Support This Tools")
