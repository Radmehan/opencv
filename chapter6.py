import cv2
import datetime

cap = cv2.VideoCapture(0)

# get height and width before set Width and Height
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # VideoWritter_fourcc('X','V','I','D')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

print(cap.isOpened())
# capture the frame continuously
# while True:
while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        out.write(frame)

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: '+ str(cap.get(4)) +' '+'HEIGHT: ' + str(cap.get(3))
        dateSet = datetime.datetime.now().strftime("%c")
        lineType = cv2.LINE_AA
        
        # frame = cv2.putText(frame, text, (10,50), font, 1, (0,255,255), 2, lineType)
        
        frame = cv2.putText(frame, dateSet, (10,50), font, 1, (0,255,255), 2, lineType)

        # cv2.imshow('frame',frame)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()