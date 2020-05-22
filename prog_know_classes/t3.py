import cv2

device_index = 0
wait_in_milsec_for_next_frame = 1
cap = cv2.VideoCapture(device_index)
print('Camera frame height {}'.format(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('Camera frame width {}'.format(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('../data/out/output.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    flag, frame = cap.read()

    if flag == False:
        print("Could not able to load frame")
        break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("show", frame)
    cv2.imshow("gray_show", gray_frame)
    out.write(frame)
    if cv2.waitKey(wait_in_milsec_for_next_frame) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
