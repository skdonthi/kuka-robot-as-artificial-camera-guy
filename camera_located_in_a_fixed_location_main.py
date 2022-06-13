from robot_integration import RemoteControlKUKA
from kinect_openni import FixedPositionCamera
import time
import cv2
import math
import sys

PrevDepth = 0
distanceRtoC = 0
isCalibrate = False
cameraAngle = 0

def calcAngle(depth1, depth2, distance):
    print(depth1)
    print(depth2)
    print(distance)
    return math.acos((((depth1)**2) + ((round(depth2,2))**2) - ((distance)**2))/(2*(depth1)*(depth2)))
    #return 0

if __name__ == '__main__':
    if len(sys.argv) > 1:
        distanceRtoC = int(sys.argv[1])
        PrevDepth = int(sys.argv[2])
        print("distanceRtoC = ", distanceRtoC)
        print("PrevDepth = ", PrevDepth)
    key = None
    
    home = '{E6AXIS: A1 0, A2 -90.0, A3 90.0, A4 0.0, A5 -90.0, A6 270.0, E1 0.0, E2 0.0, E3 0.0, E4 0.0, E5 0.0, E6 0.0}'
    # rck.moveTo(home)
    
    camera = FixedPositionCamera()
    
    robotX = 0
    robotY = 0
    cameraX = 165
    cameraY = 220
    personX = 200
    personY = 0

    # calculate distance between camera and personX
    # calculate camera angle
    # start program
    # calculate angle between camera and person as angle 2
    # calculate difference of angle2 and angle1 and increase decrease angle of the robot respectively 
    # rck = RemoteControlKUKA()
    count = 0
    while key != ord('q'):
        for info in camera.get_face_and_depth_info(isCalibrate):
            print('info = ', info)
            # e6axis2 = '{E6AXIS: A1 '+str(x)+', A2 -90.0, A3 '+str(z)+', A4 0.0, A5 -90.0, A6 270.0, E1 0.0, E2 0.0, E3 0.0, E4 0.0, E5 0.0, E6 0.0}'
            key = cv2.waitKey(1) & 0xFF
            if isCalibrate is False:
                isCalibrate = key is ord('s')
            elif count == 0:
                cameraAngle = calcAngle(PrevDepth,200,280)
                print("example1 = ", calcAngle(PrevDepth,140,274))
                print("example2 = ", calcAngle(PrevDepth,160,-210))
                print("example3 = ", calcAngle(PrevDepth,160,40))
                print("example4 = ", calcAngle(PrevDepth,180,165))
                print("example5 = ", calcAngle(PrevDepth,137,250))
                count = 1
            elif len(info) == 3:                
                x = (info[1]- 320)/2
                z = info[0] - 240
                y = info[2]*100
                
                print("x= ",x , "y= ",y , "z= ",z, "angle = ", calcAngle(PrevDepth,y,x))
                # rck.moveTo(e6axis2)
        
    camera.close_frames()

