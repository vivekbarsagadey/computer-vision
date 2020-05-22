import cv2
from matplotlib import pyplot as plt

img = cv2.imread("../data/lena.jpg")
b, g, r = cv2.split(img)
'''
img = np.zeros((200,200),np.uint8)
cv2.rectangle(img,(0,100),(200,200),(255),-1)
cv2.rectangle(img,(0,50),(100,100),(127),-1)
'''

cv2.imshow("img", img)

plt.hist(img.ravel(), 256, (0, 256))
plt.hist(b.ravel(), 256, (0, 256))
plt.hist(g.ravel(), 256, (0, 256))
plt.hist(r.ravel(), 256, (0, 256))

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
