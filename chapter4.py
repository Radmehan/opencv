import numpy as np
import cv2

img = np.zeros([512,512,3], np.uint8)

# draw a line
img = cv2.line(img,(0,0),(255,255),(0,0,255),5) #search: rgb color picker

# draw a arrowed line
img = cv2.arrowedLine(img, (0,255),(255,255),(18, 69, 64),5)

# draw a rectengle
img = cv2.rectangle(img, (384,0), (510,120), (0,255,0), 3)
# img = cv2.rectangle(img, (200,0), (300,100), (0,255,0), -1)

# draw a circle
img = cv2.circle(img,(447,63),63,(255,0,0),-1)

# text on img
font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
img = cv2.putText(img,'Open Cv',(10,500), font, 4, (255,255,255), 10, cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)

cv2.destroyAllWindows()