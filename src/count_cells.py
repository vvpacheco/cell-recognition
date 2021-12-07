import pandas as pd
import cv2
import numpy as np
import os
#%matplotlib inline
from matplotlib import pyplot as plt

my_dpi = 96
filename = '../dataset/img_cells_typical/T124.jpg'

#analise das dimensoes das imagens e quantitativo de imagens
# lista = []
# colunas = ['linhas','colunas','dimensao']
# for root, _, files in os.walk("./img_cells_typical", topdown = False):
#     for name in files:
#             imagem = cv2.imread(os.path.join(root, name))
#             #lista.append(list(imagem.shape))
#             print(imagem.shape)
#             print(imagem.size)
#             exit(0)
# df = pd.DataFrame(lista,columns=colunas)
# print(df.head())
# print(df.describe())
# exit(0)

img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.figure(figsize=(img.shape[0]/my_dpi,img.shape[1]/my_dpi))

cv2.imshow('Imagem Colorida',img)
cv2.imshow('Imagem Tons Cinza',gray)

#hist = plt.hist(gray)


#Blur
img_blur= cv2.GaussianBlur(gray,(7,7),cv2.BORDER_DEFAULT)
cv2.imshow('Apenas com Blur', img_blur)


#Edge Cascade
canny = cv2.Canny(img_blur,9,12)
cv2.imshow('Canny',canny)

#Dilated
dilated = cv2.dilate(canny,(7,7),iterations=3)
cv2.imshow('Dilated Image',dilated)

#Traçar linhas
lines = cv2.HoughLinesP(dilated, 1, np.pi/180,80, minLineLength=10, maxLineGap=250)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
# Show result
cv2.imshow("HoughLines", img)

#Threshold
ret, im = cv2.threshold(img_blur, 130, 255, cv2.THRESH_BINARY)
cv2.imshow('Threshold Binary', im)

#AdaptiveThreshold
img_adpt = cv2.adaptiveThreshold(gray, 255 , cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 27,3)
cv2.imshow('Adaptive Threshold MEAN C',img_adpt)


#AdaptiveThreshold
img_gauss = cv2.adaptiveThreshold(gray, 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 41,3)
cv2.imshow('Adaptive Gauss',img_gauss)


img_gblur = cv2.GaussianBlur(img_gauss, (11,11), 0)
_, img_final = cv2.threshold(img_gblur,0,127,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('Gaussian Blur + OTSU',img_final)

#Usando matplotlib
# plt.figure(num=None,figsize=(200,300),dpi=96)
# plt.imshow(img_final)
# plt.show()

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()