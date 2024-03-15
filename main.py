import cv2

cam = cv2.VideoCapture(0) # abre a câmera

while True:
    ret, frame = cam.read() # captura um frame da câmera
    cv2.imshow("Color Detector", frame) # exibe o nome da janela e o frame capturado
    if cv2.waitKey(1) & 0xFF == ord('q'): # aguarda pressionamento da tecla 'q' para sair
        break

cam.release() # libera a câmera
cv2.destroyAllWindows() # fecha todas as janelas abertas