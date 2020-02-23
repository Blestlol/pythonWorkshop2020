import cv2
video = cv2.VideoCapture(r"/home/aiktc/Desktop/saud/carr.mp4")
face_cascade = cv2.CascadeClassifier("cars.xml")
while True:
    check, frame = video.read()
    print(check)
    print(frame)
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 2, minNeighbors = 1)
    for x,y,w,h in faces:
        frame = cv2.rectangle(frame, (x,y),(x + w, y + h), (0, 255, 0), 0)    
    cv2.imshow("Video Frame:", frame)
    key = cv2.waitKey(2)
    if(key == ord('q')):
        break
    img = frame
cv2.destroyAllWindows()
video.release()

