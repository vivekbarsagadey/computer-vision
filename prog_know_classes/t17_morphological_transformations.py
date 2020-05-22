import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('../data/smarties.png', 0)
_, mask_img = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

kernel = np.ones([2, 2], np.uint8)
dilation = cv.dilate(mask_img, kernel, iterations=3)

erodetion = cv.erode(mask_img, kernel, iterations=5)

morphologyopen = cv.morphologyEx(mask_img, cv.MORPH_OPEN, kernel)
morphologyclose = cv.morphologyEx(mask_img, cv.MORPH_CLOSE, kernel)
morphology_bh = cv.morphologyEx(mask_img, cv.MORPH_BLACKHAT, kernel)
morphology_th = cv.morphologyEx(mask_img, cv.MORPH_TOPHAT, kernel)

titles = ['Image', "mask_img", "dilation Image", "erodetion Image", "morphologyopen", "morphologyclose",
          "morphology_bh", "morphology_th"]
images = [img, mask_img, dilation, erodetion, morphologyopen, morphologyclose, morphology_bh, morphology_th]

for i in range(len(titles)):
    plt.subplot(2, 4, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
