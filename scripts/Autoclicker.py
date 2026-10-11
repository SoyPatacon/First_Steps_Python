import pyautogui
import time

print("Pon el cursor sobre donde quieres hacer click, empieza en 10 segundos")
time.sleep(10)

try:
    while True:
        pyautogui.click()
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Detenido") 