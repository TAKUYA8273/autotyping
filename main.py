from PIL import Image,ImageGrab
import sys
import pyocr
import pyautogui
import time
from selenium import webdriver
#環境せってー
pyocr.tesseract.TESSERACT_CMD = r'D:\\tesseract 2022 v2\\tesseract.exe'
pyautogui.PAUSE = 0.1
#起動確認とか
tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("OCRツールが見つかりませんでした")
    sys.exit(1)
tool = tools[0]
print("使ってるツール :", tool.get_name())
#起動確認2
langs = tool.get_available_languages()
print(langs)

time.sleep(3)
for rool in range(228):
    ImageGrab.grab(bbox=(234, 590, 805, 646)).save("img.png")
    txt = tool.image_to_string(Image.open('img.png'), lang="eng")#jpn
    txt = txt.replace(' ', '')
    print(txt)
    pyautogui.write(txt)