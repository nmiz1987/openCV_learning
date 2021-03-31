import cv2 as cv
# import numpy as np

# blank = np.zeros((500, 500, 3), dtype='uint8') # uint8 - dataType of a image
# cv.imshow("Blank", blank)
#
# # Paint the image a certain color
# blank[100:200, 250:300] = 255, 0, 0
# cv.imshow("Blue", blank)

# Drew a Rectangle
# cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//3), (0, 250,0), thickness=-1) # src, from, to, color
# cv.imshow("Rectangle", blank)

# Drew Circle
# cv.circle(blank, (250, 250), 100, (255, 101,10), thickness=-1) # src, center, radius, color
# cv.imshow("Cirle", blank)

# Drew line
# cv.line(blank, (0,0), (255, 150), (0,0,250), thickness=2)
# cv.imshow("Line", blank)

# Write text
# cv.putText(blank, "hello",(100, 100), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2 ) # src, text, from, font, size, color
# cv.imshow("Text", blank)


# cv.waitKey(0)