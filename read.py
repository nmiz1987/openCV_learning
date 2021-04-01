import cv2 as cv

# reading images
img = cv.imread('src/1.jpg')
cv.imshow('img', img)
cv.waitKey(0)  # press '0' to break

# reading videos

capture = cv.VideoCapture('vid.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) % 0xff==ord('d'): # press 'd' to break
        break

capture.release()
cv.destroyAllWindows()