import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, img_color = cap.read()

    if ret == False:
        continue

    cv2.imshow("Color", img_color)
    if cv2.waitKey(1)&0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()