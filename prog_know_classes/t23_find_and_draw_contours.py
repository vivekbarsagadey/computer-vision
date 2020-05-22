"""
Learn to find contours, draw contours, we will see these functions :
    cv2.findContours(), cv2.drawContours().
The function retrieves contours from the binary image.
The contours are a useful tool for shape analysis and object detection and recognition.

"""

import cv2

img = cv2.imread('../data/opencv-logo.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, th_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(th_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Counter no is " + str(len(contours)))

cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

cv2.imshow("img", img)
cv2.imshow("gray img", gray_img)
cv2.imshow("Thresh hold img", th_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
