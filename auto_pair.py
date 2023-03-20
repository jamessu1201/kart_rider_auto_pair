import cv2
import pytesseract
import time
import pyscreenshot as ImageGrab
import numpy
import keyboard



pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract.exe' 

while True:
# 讀取圖像
    img = ImageGrab.grab()
    img = cv2.cvtColor(numpy.asarray(img), cv2.COLOR_RGB2BGR)

# 轉為灰度圖像
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 應用二值化，使圖像變為黑白兩色
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# 將黑色背景轉換為白色背景
    thresh = 255 - thresh

# 進行文字檢測和識別
    text = pytesseract.image_to_string(thresh, lang='chi_tra')

# 檢測是否包含 "快速配對" 這四個字
    if '結束' in text:
        print('已檢測到 "快速配對"')
        keyboard.press_and_release('r')
    else:
        print('未檢測到 "快速配對"')
    time.sleep(5)