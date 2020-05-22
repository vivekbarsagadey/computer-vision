import cv2

img = cv2.imread("../data/lena.jpg", cv2.IMREAD_COLOR)

print("Shape of image {} ".format(img.shape))
print("Size of image {} ".format(img.size))
print("Type of image {} ".format(img.dtype))

b, g, r = cv2.split(img[300:400, 100:500])
img1 = cv2.merge((b, g, r))

cv2.imshow("old img", img)
cv2.imshow("new img", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
