from win32api import keybd_event
from win32con import KEYEVENTF_KEYUP as KK
from os import system
from time import sleep
from pynput import mouse,keyboard
from pynput.mouse import Button
import win32clipboard


mouse = mouse.Controller()
key = keyboard.Controller()
def baike(name):
    import urllib.parse
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    url = 'https://baike.baidu.com/item/'+urllib.parse.quote(name)
    code = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(code,'html.parser')
    try:
        return soup.find(name='div',attrs={'class':'para'}).get_text().replace('\n','')
    except:
        return '小绿不知道这是什么意思呢，您太厉害了！'

def sendMessage(message):
    mouse.position = (346, 625)
    mouse.click(Button.left)
    key.type(message)
    enter()
    return
def copy():
    mouse.click(Button.right)
    mouse.move(10,10)
    sleep(0.1)
    mouse.click(Button.left)
    return

def enter():
    keybd_event(13,0,0,0)
    sleep(0.01)
    keybd_event(13,0,KK,0)
    return

def windowMax():
    keybd_event(91,0,0,0)
    sleep(0.2)
    keybd_event(38,0,0,0)
    sleep(0.2)
    keybd_event(38,0,KK,0)
    sleep(0.2)
    keybd_event(91,0,KK,0)
    return


def open_wechat():
    os.system('cd C:\Program Files (x86)\Tencent\WeChat&&WeChat.exe')
    windowMax()
    return

def searchMe():
    mouse.position = (99,35)
    mouse.click(Button.left)
    key.type('your Nickname')
    sleep(1)
    mouse.position = (212, 117)
    mouse.click(Button.left)
    sleep(0.2)
    return

def readLastMessage():
    mouse.position = (1116, 541)
    mouse.click(Button.left)
    sleep(0.05)
    mouse.click(Button.left)
    copy()
    sleep(0.5)
    return
def getText():
    win32clipboard.OpenClipboard()
    text = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return text
open_wechat()
searchMe()
lastText = ''
while True:
    readLastMessage()
    text = getText()
    if text==lastText or text=='好' or text=='小绿机器人还没有那么强大呢，换一个试试。' or text=='你好啊，我是小绿机器人！':
        continue

    if text=='你好':
        sendMessage('你好啊，我是小绿机器人！')
        lastText = '你好啊，我是小绿机器人！'
        continue

    if text=='再发一次':
        sendMessage('好')
        lastText = '好'
        continue

    if text[0:2]=='打开':
        lastText = text
        os.system('explorer '+text[2:])
        if os.system('explorer '+text[2:])==1:
            sendMessage('打不开文件，请检查路径后重试')
            continue

        else:
            sendMessage('打开文件成功！')
            continue

    if text=='stop' or text=='拜拜':
        sendMessage('拜拜')
        exit()
    try:
        if text[-3]+text[-2]+text[-1]=='是什么':
            message = baike(text[0:-3])
            sendMessage(message)
            lastText = message
            continue
    except:
        pass

    else:
        lastText = text
        sendMessage('小绿机器人还没有那么强大呢，换一个试试。')




