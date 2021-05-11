

"""Código para comunicar información de los que hacen las I.A. todos los días
                                    y como esto afecta nuestro entorno cercano"""

import cv2


face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()

cap= cv2.VideoCapture(0)

while(True):
    ret,frame = cap.read()
    #Capture frame by frame
    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces= face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
        print(x, y, w, h)
        roi_gray = gray[y:y + h, x:x + w]  # (cord1-height, cord2-height)
        cv2.rectangle(frame, (x,y-20),(x+300,y),(0,0,0),thickness= cv2.FILLED)
        font = cv2.FONT_HERSHEY_COMPLEX
        name = "Eres seleccionado por A.I. DIARIO "
        color = (255, 255, 255)
        stroke = 1
        cv2.putText(frame, name, (x, y-5), font, 0.5, color, stroke, cv2.LINE_AA)

        img_item = "Prueba.png"
        cv2.imwrite(img_item, roi_gray)
        color = (255, 0, 0)
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

#When everything done, release teh capture
cap.release()
cv2.destroyAllWindows()