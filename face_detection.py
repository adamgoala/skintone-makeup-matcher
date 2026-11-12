import cv2

photo = cv2.imread("LEBRON_FACE.PNG")

#cv2.imshow("Face Detection Test", photo)
cv2.waitKey(0)
cv2.destroyAllWindows()

#----------------------------------------------

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

gray = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)

faces = face_detector.detectMultiScale(gray, 1.1, 5) # 1.1 is the scale factor, 5 minimum neighboring detections

print(faces)
#------------------------------------------

for (x, y , w, h) in faces:
    cv2.rectangle(photo, (x,y),(x+w, y+h), (0,255,0),2 )

cv2.imshow("Face Detection TEST2", photo)
cv2.waitKey(0)
#--------------------------------------------