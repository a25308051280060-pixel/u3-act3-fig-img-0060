import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2 

# Ambar Fierro NC 0060
print("Ambar Fierro NC 0060")
print("UIII Act3 colocar puntos a una imagen  en blanco y negro ")
mi_imagen= cv2.imread('alaniis yuki.jpeg')
plt.imshow(mi_imagen)
plt.title('alanis yuki y Ambar Fierro 0060')
plt.show()
print("+-+-+-+ puntos en la imagen +-+-+-+")
plt.imshow(mi_imagen)
x = [100,100,300,340]
y = [100,400,500,402]
plt.scatter(x, y, s = 20,c='red')
plt.show()