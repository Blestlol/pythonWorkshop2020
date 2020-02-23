import cv2

video = cv2.VideoCapture(r"/home/aiktc/Desktop/saud/faceDetection.mp4")
#video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

'''
print(type(video))
print(type(check))
print(type(frame))
'''
while True:
    check, frame = video.read()
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.250, minNeighbors = 14)
    for x,y,w,h in faces:
        frame = cv2.rectangle(gray_img, (x,y),(x + w, y + h), (0, 255, 0), 3)    
    cv2.imshow("Video Frame:", frame)
    key = cv2.waitKey(2)
    if(key == ord('q')):
        break
    img = frame
cv2.destroyAllWindows()
video.release()





