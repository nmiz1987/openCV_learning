import cv2 as cv

# reading images
img = cv.imread('1.jpg')
cv.imshow('img', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Blur
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow("canny", canny)

# Dilating the image
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (5, 5), iterations=5)
cv.imshow('eroded', eroded)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow("Resized", resized)

cv.rectangle(img, (200, 50), (399,199), (0, 250,0), thickness=1) # src, from, to, color
cv.imshow("Rectangle", img)

# Cropping
crop = img[50:200, 200:400]
cv.imshow("Crop", crop)

cv.waitKey(0)  # press '0' to break
