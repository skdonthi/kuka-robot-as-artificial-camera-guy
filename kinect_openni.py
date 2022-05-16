# needs https://structure.io/openni
# much is taken from https://github.com/severin-lemaignan/openni-python

from openni import openni2
import numpy as np
import cv2

openni2.initialize() # can also accept the path of the OpenNI redistribution

dev = openni2.Device.open_any()
print(dev.get_device_info())
#print(dev.get_sensor_info())

depth_stream = dev.create_depth_stream()
depth_stream.start()
color_stream = dev.create_color_stream()
color_stream.start()
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
key = None
while key != ord('q'):
    depth_frame = depth_stream.read_frame()
    depth_data = depth_frame.get_buffer_as_uint16()
    depth_img1 = np.ndarray((depth_frame.height, depth_frame.width), dtype=np.uint16, buffer=depth_data).astype(np.float32)
    depth_img = depth_img1/1000.0 # convert to meters 
    cv2.imshow("Depth", depth_img-.5) # uniform shift by 0.5 m distance for better display
    # print('start=', depth_img[depth_frame.height//2,depth_frame.width//2]) ## access one distance sample from the middle
    color_frame = color_stream.read_frame()
    color_data = color_frame.get_buffer_as_uint8()
    color_img = np.ndarray((color_frame.height, color_frame.width, 3), dtype=np.uint8, buffer=color_data)  

    # Convert to grayscale
    gray = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(color_img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        height = int(y+(h/2))
        width = int(x+(w/2))
        depth = depth_img[height, width]
        print('end=', depth)
    # Display
    cv2.imshow("Color", color_img[...,::-1])
    key = cv2.waitKey(1) & 0xFF

depth_stream.stop()
color_stream.stop()

openni2.unload()
