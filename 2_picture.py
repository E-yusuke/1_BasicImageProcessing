import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("../pool/numeral.jpg")
cv2.imshow('WinName', img)
height = img.shape[0]
width = img.shape[1]
multiple = 5
img = cv2.resize(img, (int(width * multiple), int(height * multiple)))
cv2.imshow('WinName', img)
