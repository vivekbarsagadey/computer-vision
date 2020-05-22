import cv2

img = cv2.imread("../data/smarties.png")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, th_img = cv2.threshold(gray_img, 240, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(th_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0, 255, 0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    if len(approx) == 3:
        cv2.putText(img, "It is triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 4:
        x, y, w, h = cv2.boundingRect(contour)
        aspectRatio = float(w) / h
        if .95 < aspectRatio < 1.2:
            cv2.putText(img, "It is Square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        else:
            cv2.putText(img, "It is Rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

    else:
        cv2.putText(img, "It is circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
