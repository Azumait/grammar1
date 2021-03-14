import cv2 as cv

img_color = cv.imread('truman.jpg')
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
ret, img_binary = cv.threshold(img_gray, 127, 255, 0)

# CHAIN_APPROX_SIMPLE, CHAIN_APPROX_NONE
contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# cv.drawContours(image 変数, contours, contoursId, (color), thickness)
cv.drawContours(img_color, contours, -1, (0, 255, 0), 3)

cv.imshow("result", img_color)
cv.waitKey(0)