import pyautogui
position=pyautogui.position()
print(position)
pyautogui.doubleClick(148,317)
pyautogui.press('down')
pyautogui.press('enter')
pyautogui.write('I am 19 yrs old')
pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('ctrl','c')
pyautogui.press('down')
pyautogui.hotkey('ctrl','v')