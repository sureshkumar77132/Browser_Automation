# here i used this script to get the screen shot from the sucuri scan of the web site 

import webbrowser
import random 
from selenium import webdriver       
import webbrowser, sys, pyperclip
import time
driver=webdriver.Chrome()
text=(open("trackers.txt")).read()                           //put the list of web site name here 
pyperclip.copy(text)
address = pyperclip.paste()
j=1
for i in address.split("\n"):  
    
    driver.get('https://sitecheck.sucuri.net/results/' + i)  //put the link of the web site you want to get the result from
    time.sleep(10)
    driver.save_screenshot("screenshot-"+str(j)+".png")
    j=j+1



