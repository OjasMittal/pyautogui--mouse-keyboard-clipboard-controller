import pyautogui
position=pyautogui.position()
print(position)
pyautogui.moveTo(1310,567,duration=1)
pyautogui.click()
pyautogui.drag(150,0,duration=1,button='left')
pyautogui.drag(0,-150,duration=1,button='left')
pyautogui.drag(-150,0,duration=1,button='left')
pyautogui.drag(0,150,duration=1,button='left')