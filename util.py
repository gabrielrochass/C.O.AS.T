import numpy as np
import cv2

def getLimits(color):
    c = np.uint8([[color]]) # converte input color para inteiro de 8 bits (0-255)
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV) # converte cor de BGR para HSV usado pelo OpenCV

    # define limites inferior e superior para a cor
    lowerLimit = hsvC[0][0][0] - 10, 100, 100 
    upperLimit = hsvC[0][0][0] + 10, 255, 255

    # converte limites para array de inteiros de 8 bits
    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit