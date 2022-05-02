import cv2
# from PIL import Image, ImageFilter
# import numpy as np


'''
Used to calculate the mean values of all faces 
return the mean value 
'''
def calculate_Mean(All_Faces):
    all_x = 0
    all_y = 0
    all_w = 0
    all_h = 0
    for x, y, w, h in All_Faces:
        all_x += x
        all_y += y
        all_w += w
        all_h += h
        # print(x)
        # print(y)
        # print(w)
        # print(h)
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return [int(all_x/10), int(all_y/10), int(all_w/10), int(all_h/10)]


def get_Center(values):
    return [int(values[0] + values[2]/2), int(values[1] + values[3]/2)]


'''
Used to create circle on the image
return the center values 
'''
def createCircle(values):
    center_coordinates = (get_Center(values))
    radius = 10
    color = (255, 0, 0)
    thickness = -1
    cv2.circle(img, center_coordinates, radius, color, thickness)


if __name__ == '__main__':

    # fpsLimit = 0.001 # throttle limit
    # startTime = time.time()
    # cv = cv2.VideoCapture(0)

    outer_count = 0

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)

    All_Faces = []
    imageRcvdValue = 0
    flag = False
    while True:
        count = 0
        # Read the frame
        _, img = cap.read()
        # kernel = np.ones((5, 5), np.float32) / 25
        # img = cv2.filter2D(img, -1, kernel)
        # img = cv2.blur(img, (5, 5))
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect the faces
        # faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        faces = face_cascade.detectMultiScale(image=gray, scaleFactor=1.1, minNeighbors=1, minSize=(25, 25))

        new_X = 0
        new_Y = 0
        new_W = 0
        new_H = 0
        count = 0

        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            new_X += x
            new_Y += y
            new_W += w
            new_H += h
            # Number of faces detected
            count += 1
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            # print(faces)

        # Check if there is a face in the frame
        if count != 0:
            new_X = int(new_X / count)
            new_Y = int(new_Y / count)
            new_W = int(new_W / count)
            new_H = int(new_H / count)

            All_Faces.append([new_X, new_Y, new_W, new_H])
            imageRcvdValue += 1

            # TODO: make a check if the count reaches to 100 values then set the mean value of the face
            if imageRcvdValue >= 10 or flag:
                # calculate the mean value
                values = calculate_Mean(All_Faces)
                # cv2.rectangle(img, (new_X, new_Y), (new_X + new_W, new_Y + new_H), (255, 0, 255), 2)
                cv2.rectangle(img, (values[0], values[1]), (values[0] + values[2], values[1] + values[3]), (255, 0, 255), 2)

                ######################################
                createCircle(values)
                # center_coordinates = (get_Center(values))
                # radius = 10
                # color = (255, 0, 0)
                # thickness = -1
                # cv2.circle(img, center_coordinates, radius, color, thickness)
                ######################################
                imageRcvdValue = 0
                All_Faces = []

        # Display
        cv2.imshow('img', img)
        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break


    # Release the VideoCapture object
    cap.release()