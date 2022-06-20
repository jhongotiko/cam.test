import cv2 

webcam = cv2.VideoCapture(0)


title = "Webcam"


if webcam.isOpened:
    validation, frame = webcam.read()
    while validation:
        validation, frame = webcam.read()
        cv2.imshow(title, frame)
        key = cv2.waitKey(1)

        if key == 27:
            break


webcam.release()
cv2.destroyAllWindows()
