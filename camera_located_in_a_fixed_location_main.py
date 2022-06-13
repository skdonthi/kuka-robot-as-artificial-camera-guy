from robot_integration import RemoteControlKUKA
from kinect_openni import FixedPositionCamera
import time
import cv2
import math
import sys

# in centimeters
realword_dimensions = { 
    "width" : 400,
    "height": 200,
    "depth": 200
}

# camera resolution
camera_dimensions = { 
    "width" : 640,
    "height": 480
}

# c2=a2+b2−2 a b cos(γ)
def calcAngle(a, b, c):
    if a != 0 and b != 0 and c != 0:
        length3 = (math.pow(a, 2) + math.pow(b,2) - math.pow(c, 2))/(2*a*b)
        angle = math.acos(length3)
        print("Angle in Radians:", angle)
        angleInDegrees = convertRadiansIntoDegrees(angle)
        print("Angle in Degrees:", angleInDegrees)
        return angleInDegrees
        
def convertRadiansIntoDegrees(x):
    pi=math.pi
    degree=(x*180)/pi
    return degree

if __name__ == '__main__':
    if len(sys.argv) > 1:
        distanceRtoC = 300 # int(sys.argv[1]) // 230, 200
        distanceCtoP = 185 # int(sys.argv[2]) # This value is depth from camera
        distanceRtoP = 200 # int(sys.argv[3])
        cameraAngle = calcAngle(distanceCtoP, distanceRtoC, distanceRtoP)
    key = None
    rck = RemoteControlKUKA()
    home = '{E6AXIS: A1 0, A2 -90.0, A3 90.0, A4 0.0, A5 -90.0, A6 270.0, E1 0.0, E2 0.0, E3 0.0, E4 0.0, E5 0.0, E6 0.0}'
    A1 = 0
    A2 = -90
    A3 = 90
    rck.moveTo(home)    
    camera = FixedPositionCamera()    
    # calculate distance between camera and personX
    # calculate camera angle
    # start program
    # calculate angle between camera and person as angle 2
    # calculate difference of angle2 and angle1 and increase decrease angle of the robot respectively     
    while key != ord('q'):
        for info in camera.get_face_and_depth_info():
            print('info = ', info)
            key = cv2.waitKey(1) & 0xFF
            if len(info) == 3:
                new_depth = (info[2] - distanceCtoP)/6
                new_width = ((info[1]-(camera_dimensions['width']/2))*(0.625))/4
                new_height = ((info[0] - (camera_dimensions['height']/2)) * (0.416))
                # when camera is at angle 40 degree, depth is A1, width is A2, height is A3
                
                e6axis2 = '{E6AXIS: A1 '+str("{:.2f}".format(A1+new_depth))+', A2 '+str("{:.2f}".format(A2+new_width))+', A3 90, A4 0.0, A5 -90.0, A6 270.0, E1 0.0, E2 0.0, E3 0.0, E4 0.0, E5 0.0, E6 0.0}'
                
                print('aman',e6axis2)
                rck.moveTo(e6axis2)
        
    camera.close_frames()

