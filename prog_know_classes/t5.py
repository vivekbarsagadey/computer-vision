import cv2

device_index = 0
wait_in_milsec_for_next_frame = 1
cap = cv2.VideoCapture(device_index)

cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 512)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 512)

print('Camera frame height {}'.format(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('Camera frame width {}'.format(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))

while cap.isOpened():
    flag, frame = cap.read()

    if flag == False:
        print("Could not able to load frame")
        break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("show", frame)
    cv2.imshow("gray_show", gray_frame)
    if cv2.waitKey(wait_in_milsec_for_next_frame) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
