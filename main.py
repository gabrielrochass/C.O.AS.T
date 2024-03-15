import cv2
from PIL import Image
from util import getLimits

yellow = [0, 255, 255] # cor amarela em BGR

cam = cv2.VideoCapture(0) # abre a câmera

while True:
    ret, frame = cam.read() # captura um frame da câmera

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # converte o frame de BGR para HSV

    lowerLimit, upperLimit = getLimits(yellow) # obtém os limites inferior e superior para a cor amarela

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit) # cria máscara para pixels de cor amarela

    fullMask = Image.fromarray(mask) # cria um objeto Image a partir da máscara

    bbox = fullMask.getbbox() # obtém bounding box da máscara

    if bbox is not None: # se a bounding box não for vazia
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5) 

    # cv2.imshow("Color Detector", mask) -> deixa a tela toda preta e quando aparece a cor amarela, ela fica branca no lugar da cor amarela (objeto)
    cv2.imshow("Color Detector", frame) # exibe o nome da janela e o frame capturado
    if cv2.waitKey(1) & 0xFF == ord('q'): # aguarda pressionamento da tecla 'q' para sair
        break

cam.release() # libera a câmera
cv2.destroyAllWindows() # fecha todas as janelas abertas