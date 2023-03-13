import numpy as np
import cv2

img = cv2.imread('HappyFish.jpg')

# draw a line
img = cv2.line(img,(0,0),(100,100),(0,0,255),5) #search: rgb color picker

# draw a arrowed line
img = cv2.arrowedLine(img, (0,100),(100,100),(18, 69, 64),5)

# draw a rectengle
img = cv2.rectangle(img, (140,0), (250,110), (0,255,0), 3)
# img = cv2.rectangle(img, (200,0), (300,100), (0,255,0), -1)

# draw a circle
img = cv2.circle(img,(195,53),53,(255,0,0),-1)

# text on img
font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
img = cv2.putText(img,'Open Cv',(10,100), font, 3, (255,255,255),3,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)

cv2.destroyAllWindows()