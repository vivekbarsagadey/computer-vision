import cv2

img = cv2.imread("../data/messi5.jpg")
logo_img = cv2.imread("../data/opencv-logo.png")

print("Shape of image {} ".format(img.shape))
print("Size of image {} ".format(img.size))
print("Type of image {} ".format(img.dtype))

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

ball = img[280:340, 330:390]
img[273:333, 130:190] = ball

img = cv2.resize(img, (512, 512))
logo_img = cv2.resize(logo_img, (512, 512))

dst_image = cv2.addWeighted(img, .9, logo_img, .1, 0)

cv2.imshow("img", dst_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
