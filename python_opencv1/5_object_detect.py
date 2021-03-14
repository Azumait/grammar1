# cv2はOpenCVライブラリ
import cv2 as cv
# NumPyは大きな配列を簡単に処理するライブラリ
import numpy as np

# HSV色を処理するための整数変数の設定
hsv = 0
lower_blue1 = 0
upper_blue1 = 0
lower_blue2 = 0
upper_blue2 = 0
lower_blue3 = 0
upper_blue3 = 0

def nothing(x):
    pass

def mouse_callback(event, x, y, flags, param):
    global hsv, lower_blue1, upper_blue1, lower_blue2, upper_blue2, lower_blue3, upper_blue3, threshold

    # マウスの左ボタンを押す時にそこにあるピクセル値を読み取ってきて、HSVに変換します。
    if event == cv.EVENT_LBUTTONDOWN:

        print(img_color[y, x])

        # マウスの左ボタンを押す時にそこにあるピクセル値を読み取ってきて、
        color = img_color[y, x]

        # HSVに変換
        one_pixel = np.uint8([[color]])
        hsv = cv.cvtColor(one_pixel, cv.COLOR_BGR2HSV)
        hsv = hsv[0][0]

        threshold = cv.getTrackbarPos('threshold', 'img_result')

        # HSV色空間で、マウスクリックで得られたピクセル値と、似てるピクセル値の範囲を決めます。
        if hsv[0] < 10:
            print("case1")
            lower_blue1 = np.array([hsv[0]-10+180, threshold, threshold])
            upper_blue1 = np.array([180, 255, 255])
            lower_blue2 = np.array([0, threshold, threshold])
            upper_blue2 = np.array([hsv[0], 255, 255])
            lower_blue3 = np.array([hsv[0], threshold, threshold])
            upper_blue3 = np.array([hsv[0]+10, 255, 255])
            #     print(i-10+180, 180, 0, i)
            #     print(i, i+10)

        elif hsv[0] > 170:
            print("case2")
            lower_blue1 = np.array([hsv[0], threshold, threshold])
            upper_blue1 = np.array([180, 255, 255])
            lower_blue2 = np.array([0, threshold, threshold])
            upper_blue2 = np.array([hsv[0]+10-180, 255, 255])
            lower_blue3 = np.array([hsv[0]-10, threshold, threshold])
            upper_blue3 = np.array([hsv[0], 255, 255])
            #     print(i, 180, 0, i+10-180)
            #     print(i-10, i)
        else:
            print("case3")
            lower_blue1 = np.array([hsv[0], threshold, threshold])
            upper_blue1 = np.array([hsv[0]+10, 255, 255])
            lower_blue2 = np.array([hsv[0]-10, threshold, threshold])
            upper_blue2 = np.array([hsv[0], 255, 255])
            lower_blue3 = np.array([hsv[0]-10, threshold, threshold])
            upper_blue3 = np.array([hsv[0], 255, 255])
            #     print(i, i+10)
            #     print(i-10, i)

        print(hsv[0])
        print("@1", lower_blue1, "~", upper_blue1)
        print("@2", lower_blue2, "~", upper_blue2)
        print("@3", lower_blue3, "~", upper_blue3)


# 指定したウィンドウに(img_color, img_result)、それぞれの結果値を出力する。
cv.namedWindow('img_color')
cv.setMouseCallback('img_color', mouse_callback)

cv.namedWindow('img_result')
cv.createTrackbar('threshold', 'img_result', 0, 255, nothing)
cv.setTrackbarPos('threshold', 'img_result', 30)
cap = cv.VideoCapture(0)

while(True):
    ret, img_color = cap.read()
    height, width = img_color.shape[:2]
    img_color = cv.resize(img_color, (width, height), interpolation=cv.INTER_AREA)

    # 原本映像をHSV映像に変換します。
    img_hsv = cv.cvtColor(img_color, cv.COLOR_BGR2HSV)

    # HSV映像から、img_maskを生成します。
    img_mask1 = cv.inRange(img_hsv, lower_blue1, upper_blue1)
    img_mask2 = cv.inRange(img_hsv, lower_blue2, upper_blue2)
    img_mask3 = cv.inRange(img_hsv, lower_blue3, upper_blue3)
    img_mask = img_mask1 | img_mask2 | img_mask3


    # img_maskの中に、原本のimg_colorから、（青いとか、赤いとかの決めてる色の）範囲値に該当する映像部分を獲得します。
    img_result = cv.bitwise_and(img_color, img_color, mask=img_mask)


    cv.imshow('img_color', img_color)
    cv.imshow('img_mask', img_mask)
    cv.imshow('img_result', img_result)


    # ESC Keyを押すと出ます。
    if cv.waitKey(1) & 0xFF == 27:
        break


cv.destroyAllWindows()