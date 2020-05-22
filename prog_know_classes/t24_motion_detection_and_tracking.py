import cv2

cap = cv2.VideoCapture("../data/vtest.avi")
_, frame1 = cap.read()
_, frame2 = cap.read()

while cap.isOpened():
    diff_img = cv2.absdiff(frame1, frame2)
    gray_img = cv2.cvtColor(diff_img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray_img, (5, 5), 0)
    _, th_img = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilate_img = cv2.dilate(th_img, None, iterations=5)

    contours, _ = cv2.findContours(dilate_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame1,contours,-1,(0,255,0),2)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 1000:
            continue

        ract_img = cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("video", frame1)
    frame1 = frame2
    _, frame2 = cap.read()
    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()
