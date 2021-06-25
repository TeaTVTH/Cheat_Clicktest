import pyautogui
import keyboard
import time
import win32api, win32con
import numpy as np

#make list X to random
X_pos = [488,489,490,487,486]
#make a list Y to use to random
Y_pos = [505,504,503,506,507,508]
#make a list Time to
Time_list = [0.06,0.04,0.05,0.01,0.07]

#definte Check_white to check the x and use Blue Fuction
def check_white():
    if pyautogui.locateOnScreen('Bruh.png', region=(1067,135,74,64), grayscale=True,confidence=0.5)!= None:
        time.sleep(2)
        click(1126,157)
        
    else:
        check_Blue()

#Definte Check_blue to check Blue buttom in white check
def check_Blue():
    if pyautogui.pixel(488,505)!=[255,255,255] :
        click(448,505)



#definte click() to click to Position x,y
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep((np.random.choice(Time_list)))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('esc') == False:
    check_white()
    click((np.random.choice(X_pos)),(np.random.choice(Y_pos)))
