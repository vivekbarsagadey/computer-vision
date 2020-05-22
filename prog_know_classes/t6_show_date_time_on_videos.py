"""
Show Date and Time on Videos using OpenCV Python

"""
import datetime as dt

import cv2

device_index = 0
wait_in_milsec_for_next_frame = 1
cap = cv2.VideoCapture(device_index)

print('Camera frame height {}'.format(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('Camera frame width {}'.format(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))

while cap.isOpened():
    flag, frame = cap.read()
    date = dt.datetime.now()
    date_str = date.strftime("%d/%m/%Y %H:%M:%S")
    frame = cv2.putText(frame, date_str, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 1, cv2.LINE_AA)

    if flag == False:
        print("Could not able to load frame")
        break
    cv2.imshow("show", frame)
    if cv2.waitKey(wait_in_milsec_for_next_frame) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
