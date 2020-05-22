"""
How to Read, Write, Show Images in OpenCV
"""

import cv2

img = cv2.imread('../data/lena.jpg', cv2.IMREAD_UNCHANGED)
print(img)

cv2.imshow("show", img)
key = cv2.waitKey(0) & 0xFF
if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    print("save image")
    cv2.imwrite('../data/lena_copy.jpg', img)
    cv2.destroyAllWindows()
