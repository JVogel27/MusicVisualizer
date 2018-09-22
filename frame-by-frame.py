import cv2
cap = cv2.VideoCapture('highway_long.gif')
count = 0
while cap.isOpened():
    ret,frame = cap.read()
    #apply gray scale
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    # now apply a gradient...
    # sobel-y
    frame = cv2.Sobel(frame,cv2.CV_8UC1,0,1,ksize=13)

    # or sobel-x
    #frame = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=11)

    # or laplacian
    #frame = cv2.Laplacian(frame,cv2.CV_64F)

    #apply a color map to the image
    frame = cv2.applyColorMap(frame, cv2.COLORMAP_SPRING)

    cv2.imshow('window-name',frame)
    cv2.waitKey(90)
    count = count + 1
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()  # destroy all the opened windows