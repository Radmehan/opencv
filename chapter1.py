import cv2

# img read in gray mode
# img = cv2.imread('HappyFish.jpg',0)

# img read in alpha mode
# img = cv2.imread('HappyFish.jpg',-1)

# img read in color mode
img = cv2.imread('HappyFish.jpg',1)

print(img)

cv2.imshow('image',img)

k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('happyfish_copy.png', img)
    cv2.destroyAllWindows()

# image write. create a copy img name 'happyfish_copy.png'
# cv2.imwrite('happyfish_copy.png',img)