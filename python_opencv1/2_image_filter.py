import cv2

"""
Normal Image
"""
img_color = cv2.imread('truman.jpg', cv2.IMREAD_COLOR)

cv2.namedWindow('IFS Python Team')
cv2.imshow('IFS Python Team', img_color)

cv2.waitKey(0)

"""
GrayScale Image
"""
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

cv2.imshow("Show Gray Image", img_gray)
cv2.waitKey(0)

"""
Save Image
"""
cv2.imwrite('savedimage.jpg', img_gray)

"""
Close Window
"""
cv2.destroyAllWindows()