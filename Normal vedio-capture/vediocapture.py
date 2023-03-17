import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    #line 9 to 11 for drawing text on windows
    height = int(cap.get(4))
    font = cv2.FONT_HERSHEY_DUPLEX
    img = cv2.putText(frame, 'Opee is Great!', (10, height - 10), font, 2, (0, 0, 0), 5, cv2.LINE_AA)

    cv2.imshow('You', frame)

    if cv2.waitKey(1) == ord('q'): #press q to terminate program
        break
cap.relese()
cap.destrAllWindows()

#To show same capture prompt 4 times
'''
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    image[:height//2, :width//2] = smaller_frame
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = smaller_frame
    image[height//2:, width//2:] = smaller_frame

    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() '''