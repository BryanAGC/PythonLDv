"""
Usa OpenCV para detectar rostros en una imagen.
"""
import cv2

def detectar_rostros(imagen):
    cascada = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    img = cv2.imread(imagen)
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rostros = cascada.detectMultiScale(gris, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in rostros:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Detección de Rostros", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# detectar_rostros("imagen.jpg")  # Descomentar para probar con una imagen real
