import cv2
from PIL import Image
from util import getLimits

# define limites de cor para cada cor em BGR
yellow = [0, 255, 255] # amarelo em BGR
blue = [255, 0, 0]     # azul em BGR

cam = cv2.VideoCapture(0) # abrir a câmera

while True:
    ret, frame = cam.read() # capturar um frame da câmera

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # converter o frame de BGR para HSV

    # detecção de cor para amarelo
    lowerLimitYellow, upperLimitYellow = getLimits(yellow) 
    maskYellow = cv2.inRange(hsvImage, lowerLimitYellow, upperLimitYellow) 
 
    # detecção de cor para azul
    lowerLimitBlue, upperLimitBlue = getLimits(blue)
    maskBlue = cv2.inRange(hsvImage, lowerLimitBlue, upperLimitBlue)

    # desenhar caixas limite para cada objeto detectado
    bboxYellow = Image.fromarray(maskYellow).getbbox()
    if bboxYellow is not None:
        x1, y1, x2, y2 = bboxYellow
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 255), 5) # amarelo

    bboxBlue = Image.fromarray(maskBlue).getbbox()
    if bboxBlue is not None:
        x1, y1, x2, y2 = bboxBlue
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 5) # azul

    cv2.imshow("Color Detector", frame) # exibir o nome da janela e o frame capturado
    key = cv2.waitKey(1)

    if (key == 27) or key == ord('q') or cv2.getWindowProperty("Color Detector", cv2.WND_PROP_VISIBLE) < 1: # aguardar pressionamento da tecla 'q' para sair or esc or x da janela
        break

cam.release() # liberar a câmera
cv2.destroyAllWindows() # fechar todas as janelas abertas
