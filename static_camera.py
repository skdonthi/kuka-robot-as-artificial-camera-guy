import cv2
# https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html#face-detection-using-haar-cascades
# simple face detection using opencv using haar cascades
class StaticCamera:
    def __init__ (self, data):
        self.data = data
    def face_detect(self):
        # Load the cascade
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        # To capture video from webcam. 
        capture = cv2.VideoCapture(0)
        # To use a video file as input 
        # capture = cv2.VideoCapture('video.mp4')

        while True:
            # Read the frame
            _, img = capture.read()
            # Convert to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Detect the faces
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            # Draw the rectangle around each face
            for (x, y, w, h) in faces:
                print("x=",x,"y=",y,"w=",w,"h=",h)
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            # Display
            cv2.imshow('img', img)
            # Stop if escape key is pressed
            k = cv2.waitKey(30) & 0xff
            if k==27:
                break
        # Release the VideoCapture object
        capture.release()
