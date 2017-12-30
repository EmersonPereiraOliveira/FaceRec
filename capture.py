import cv2
import numpy as np

#Create my own auxiliary class
from UsefulFunctions import UsefulFunctions

#Create UsefulFunctions object
uf = UsefulFunctions()

#Classifiers for detection of faces and eyes
classifier_face = cv2.CascadeClassifier("classifiers/haarcascade-frontalface-default.xml")
classifier_eye = cv2.CascadeClassifier("classifiers/haarcascade-eye.xml")

#Create VideoCapture object
cap = cv2.VideoCapture(0)

#Initial value of samples and maximum number of samples
sample = 1
number_of_samples = 25

#Set values for width and height
width, height = 220, 220

#Identification of user/people in the database of images
id = input("Insert your id: ")

print("Initializing... Press 'c' to capture the faces:")
while True:
    ret, frame = cap.read()
    #Function than verify status/return of capture
    if uf.verify_ret(ret) == 0:
        break

    #Convert the frame for gray scale
    gray_frame = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2GRAY)

    #Detect faces
    detected_faces = classifier_face.detectMultiScale(gray_frame, scaleFactor=1.5, minSize=(50,50))

    for fx, fy, fw, fh in detected_faces:
        #Draw rectangle on the face detected
        cv2.rectangle(frame, (fx,fy), (fx+fw, fy+fh ), (0,0,255), 5)
        #Face cropped
        face = gray_frame[fy:(fy+fh), fx:(fx+fw)]
        detected_eyes = classifier_eye.detectMultiScale(gray_frame)
        for (ex, ey, ew, eh) in detected_eyes:
            cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), (255,0,0), 2)

            if cv2.waitKey(1) & 0xFF == ord("c"):
                #Resize image of face
                face_resize = cv2.resize(gray_frame[fy:fy+fh, fx:fx+fw], (width, height))
                #Save faces in the database_faces
                cv2.imwrite("database_faces/user" + str(id) + "." + str(sample) + ".jpg", face_resize)
                print("Face" + str(sample) + " captured")
                sample += 1

    #In the hstack(), must have the same dimensions
    gray_frame_3_channels = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)
    #Show images in the same window
    cv2.imshow("Face", np.hstack((frame, gray_frame_3_channels)))
    cv2.waitKey(100)
    if sample >= number_of_samples + 1:
        break


print("Finish!")
cv2.destroyAllWindows()


