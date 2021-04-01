import cv2 as cv
import numpy as np

# reading images
img = cv.imread('1.jpg')
cv.imshow('img', img)


# Transformation
def translate(img, x, y):  # x,y are number of pixels you want to shift along the x and y
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimenstions = (img.shape[1], img.shape[0])
    # -x --> Left
    # -y --> Up
    # x --> Right
    # y --> Down
    return cv.warpAffine(img, transMat, dimenstions)


translated = translate(img, -100, 100)
cv.imshow("trans", translated)


# Rotation
def rotate(img, angle, rotPoint=None):
    (height, widght) = img.shape[:2]

    if rotPoint is None:  # rotate around the center:
        rotPoint = (widght // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimenstion = (widght, height)

    return cv.warpAffine(img, rotMat, dimenstion)


rotated = rotate(img, 9, (1,1))
cv.imshow("Rotate", rotated)

# Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow("resized", resized)

# Flipping
flip = cv.flip(img, -1) # 0 - vertically , 1 - horizontally, -1 - both
cv.imshow("Flip", flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow("cropped", cropped)


cv.waitKey(0)  # press '0' to break
