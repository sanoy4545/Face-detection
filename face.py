import cv2

detect= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img_image=cv2.VideoCapture("hh.jfif")

res,img = img_image.read()
grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

face = detect.detectMultiScale(grey,1.3,5)

for(x,y,w,h) in face:
    cv2.rectangle(img, (x,y), (x+w,y+h),( 255,255,0), 2)

cv2.imshow("hitler", img)
cv2.waitKey(0)
img_image.release()
cv2.destroyAllWindows()