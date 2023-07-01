import cv2

capture = cv2.VideoCapture('input_video.mp4')
count = 0
frameNr = 0

while(True):
    sucess, frame = capture.read()
    capture.set(cv2.CAP_PROP_POS_MSEC,(count*500))
    if sucess:
        cv2.imwrite(f'output/frame_{frameNr}.jpg', frame)
        count = count + 1
    else:
        break
    frameNr = frameNr + 1
capture.release()