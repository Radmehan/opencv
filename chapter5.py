import cv2

cap = cv2.VideoCapture(0)

# get height and width before set Width and Height
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # VideoWritter_fourcc('X','V','I','D')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

# set width & height. width asosiated num = 3 and height assosiated num = 4 
cap.set(3,800) #cap.set(cv2.cv2.CAP_PROP_FRAME_WIDTH,800)
cap.set(4,500) #cap.set(cv2.cv2.CAP_PROP_FRAME_HEIGHT,500)

# get height and width after set Width and Height
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(cap.isOpened())
# capture the frame continuously
# while True:
while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        out.write(frame)

        # convert color into gray
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # cv2.imshow('frame',frame)
        cv2.imshow('frame',gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()