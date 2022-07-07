import pyautogui
import pyperclip

position=pyautogui.position()
print(position)
pyautogui.doubleClick(122,345)
pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('ctrl','c')
text=pyperclip.paste()
pyautogui.alert(text)
print(text)