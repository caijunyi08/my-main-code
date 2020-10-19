from urllib import request
import datetime
today = datetime.datetime.today()
from bs4 import BeautifulSoup
import ctypes

code = request.urlopen('http://cn.bing.com').read().decode('utf-8')

soup = BeautifulSoup(code,'html.parser')

imgLink = 'http://cn.bing.com'+soup.find(name='link',attrs={'id':'bgLink'})['href']
filename = str(today.year)+','+str(today.month)+','+str(today.day)+'.png'
request.urlretrieve(imgLink,filename)

ctypes.windll.user32.SystemParametersInfoW(20, 0, __import__('os').path.abspath('.')+'/'+filename, 0)
