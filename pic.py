import cv2
import tkinter

p = 75
q = 3

def change_threshold(val):
    global p
    p = int(val)

def change_type(var):
    global q
    q = int(var)

video = cv2.VideoCapture(0)
while True:
    if cv2.waitKey(1) & 0xFF == ord('t'):
        root = tkinter.Tk()
        scale = tkinter.Scale(orient='horizontal', from_=0, to=255, command=change_threshold)
        scale.pack()
        root.mainloop()

    if cv2.waitKey(1) & 0xFF == ord('m'):
        root = tkinter.Tk()
        scale = tkinter.Scale(orient='horizontal', from_=1, to=5, command=change_type)
        scale.pack()
        root.mainloop()
    _, img = video.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    if q == 1:
        _, thresh = cv2.threshold(blur, p, 255, cv2.THRESH_BINARY)
    if q == 2:
        _, thresh = cv2.threshold(blur, p, 255, cv2.THRESH_BINARY_INV)
    if q == 3:
        _, thresh = cv2.threshold(blur, p, 255, cv2.THRESH_TRUNC)
    if q == 4:
        _, thresh = cv2.threshold(blur, p, 255, cv2.THRESH_TOZERO)
    if q == 5:
        _, thresh = cv2.threshold(blur, p, 255, cv2.THRESH_TOZERO_INV)
    cv2.imshow('My Cam', thresh)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
    
