import pyautogui, time 
time.sleep(5) 
f=open("spam.txt",'r')  
for word in f: 
    pyautogui.typewrite("bot")    
    pyautogui.press("enter")    