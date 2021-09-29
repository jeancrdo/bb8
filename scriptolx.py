from time import time
import pyautogui
pyautogui.keyDown('alt');
pyautogui.press(['tab']);
pyautogui.keyUp('alt');
pyautogui.sleep(3);

for i in range(4):
    pyautogui.press("tab");

pyautogui.sleep(3);

pyautogui.write('Anuncio Teste');
pyautogui.press(['tab']);
pyautogui.sleep(2);
pyautogui.write('Descricao teste do anuncio'); 

pyautogui.sleep(3);
pyautogui.click(200,730);
pyautogui.sleep(3);

for i in range(3):
    pyautogui.press("down");

pyautogui.click(500,930);

pyautogui.sleep(2);

pyautogui.click(800,530);
pyautogui.sleep(3);

pyautogui.click(400,180);
pyautogui.sleep(3);
pyautogui.press('down');
pyautogui.sleep(3);
pyautogui.press('enter');
pyautogui.sleep(3);
pyautogui.press('tab');

for i in range(6):
    pyautogui.press("down");
    
pyautogui.press('tab');

for i in range(10):
    pyautogui.press("down");

for i in range(2):
    pyautogui.press("tab");

pyautogui.write('100');

pyautogui.click(250,700);

pyautogui.sleep(3);

pyautogui.press("enter");










