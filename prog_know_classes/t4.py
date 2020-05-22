import cv2
import numpy as np

# img = cv2.imread("../data/lena.jpg", cv2.IMREAD_UNCHANGED)
img = np.zeros([480, 640, 3], np.uint8)

color_BGR = (0, 255, 0)
color_BGR_org = (0, 0, 255)
img = cv2.line(img, (0, 0), (255, 255), color_BGR, 2)
img = cv2.arrowedLine(img, (30, 50), (400, 500), color_BGR_org, 2)
img = cv2.rectangle(img, (30, 50), (400, 500), color_BGR_org, 2)
img = cv2.circle(img, (130, 150), 50, color_BGR_org, 5)
img = cv2.putText(img, "Thanks", (140, 160), cv2.FONT_HERSHEY_COMPLEX, 5, (255, 255, 0), 10, cv2.LINE_AA)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
