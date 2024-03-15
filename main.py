import cv2
from PIL import Image
from util import getLimits
from tkinter import Tk, colorchooser

def calculaArea(bbox): # função que calcula a área de um retângulo
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        largura_cm = (x2 - x1) * (2.54 / 96)  # 96 pixels por polegada (dpi), 2.54 cm por polegada
        altura_cm = (y2 - y1) * (2.54 / 96)
        area_cm2 = largura_cm * altura_cm
        return area_cm2
    else:
        return 0
    
def getColor():
    root = Tk()
    root.withdraw()
    color = colorchooser.askcolor(title="Selecione uma cor")
    root.destroy()
    if color[0] is not None:
        return color[0]
    else:
        # se o usuário fechar o seletor de cor sem escolher uma, retorna none
        return None


# define limites de cor para cada cor em BGR
color_rbg = getColor()

if color_rbg is not None: # somente abre a câmera se o usuário escolher uma cor
    color_bgr = [color_rbg[2], color_rbg[1], color_rbg[0]]

    cam = cv2.VideoCapture(0) # abrir a câmera

    while True:
        ret, frame = cam.read() # capturar um frame da câmera

        hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # converter o frame de BGR para HSV
        
        lowerLimitColor, upperLimitColor = getLimits(color_bgr)
        maskColor = cv2.inRange(hsvImage, lowerLimitColor, upperLimitColor)

        bboxColor = Image.fromarray(maskColor).getbbox()
        if bboxColor is not None:
            x1, y1, x2, y2 = bboxColor
            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), color_bgr, 5) # cor selecionada
            area = calculaArea(bboxColor)
            area = "{:.2f}".format(area)
            cv2.putText(frame, f"Area: {area} cm**2", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        cv2.imshow("Color Detector", frame) # exibir o nome da janela e o frame capturado
        key = cv2.waitKey(1)

        if (key == 27) or key == ord('q') or cv2.getWindowProperty("Color Detector", cv2.WND_PROP_VISIBLE) < 1: # aguardar pressionamento da tecla 'q' para sair or esc or x da janela
            break

    cam.release() # liberar a câmera
    cv2.destroyAllWindows() # fechar todas as janelas abertas
