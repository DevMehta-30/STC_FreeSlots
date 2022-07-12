import cv2
import pytesseract
import numpy as np
import pandas as pd

pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = cv2.imread("green.png")
#grayscale = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
#adaptive= cv2.adaptiveThreshold(grayscale,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,57,41)

text=pytesseract.image_to_string(image)

print(text)
# dataframe = pd.DataFrame(arr.reshape(len(row), countcol))
# print(dataframe)
# data = dataframe.style.set_properties(align="left")
# dataframe.to_csv("output1.csv")