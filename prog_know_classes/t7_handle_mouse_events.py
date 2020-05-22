import cv2

events = [i for i in dir(cv2) if 'EVENT' in i]

text = "thanks"
points = []

img = cv2.imread("../data/lena.jpg", cv2.IMREAD_COLOR)


# img = np.zeros([500, 500, 3], np.uint8)

def handle_click_event(event, x, y, flag, params):
    if event == cv2.EVENT_FLAG_LBUTTON:
        print("X pos is {} and Y pos is {} ".format(x, y))
        cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 1, cv2.LINE_AA)
        cv2.imshow("Image window", img)
    elif event == cv2.EVENT_FLAG_RBUTTON:
        blue_channel = img[y, x, 0]
        green_channel = img[y, x, 1]
        red_channel = img[y, x, 2]
        print("X pos is {} and Y pos is {} ".format(x, y))
        cv2.putText(img, "({},{},{})".format(blue_channel, green_channel, red_channel), (x, y),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 1, cv2.LINE_AA)
        cv2.imshow("Image window", img)


def handle_click_event_for_line(event, x, y, flag, params):
    if event == cv2.EVENT_FLAG_LBUTTON:
        print("X pos is {} and Y pos is {} ".format(x, y))
        cv2.circle(img, (x, y), 5, (255, 255, 0), -1)
        points.append((x, y))
        if len(points) > 1:
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 5)
    elif event == cv2.EVENT_FLAG_RBUTTON:
        if len(points) > 1:
            cv2.line(img, points[-1], points[0], (255, 0, 0), 5)
        points.clear()

    cv2.imshow("Image window", img)


cv2.imshow("Image window", img)
cv2.setMouseCallback("Image window", handle_click_event_for_line)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
