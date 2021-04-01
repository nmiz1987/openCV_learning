import cv2 as cv


def rescaleFrame(frame, scale=8):
    width = int(frame.shape[1] * scale) # shape[1]=width of the image
    height = int(frame.shape[0] * scale) # shape[0]=height of the image
    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width,height): # only for live videos
    capture.set(3, width) # 3 = width
    capture.set(4, height) # 4= height


img = cv.imread('11.jpg')
resized_img = rescaleFrame(img)
cv.imshow('resized_img', resized_img)
cv.waitKey(0)  # press '0' to break

# reading videos
capture = cv.VideoCapture('vid.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    # cv.imshow('Video', frame)
    cv.imshow('Resized Video', frame_resized)

    if cv.waitKey(20) % 0xff==ord('d'): # press 'd' to break
        break

capture.release()
cv.destroyAllWindows()
