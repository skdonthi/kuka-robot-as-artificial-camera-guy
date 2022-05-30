from robot_integration import RemoteControlKUKA
from kinect_openni import FixedPositionCamera
import time
import cv2


if __name__ == '__main__':
    key = None
    camera = FixedPositionCamera()
    # rck = RemoteControlKUKA()
    x=0
    z=100
    home = '{E6AXIS: A1 0, A2 -90.0, A3 90.0, A4 0.0, A5 -90.0, A6 270.0, E1 0.0, E2 0.0, E3 0.0, E4 0.0, E5 0.0, E6 0.0}'
    # rck.moveTo(home)
    while key != ord('q'):
        for info in camera.get_face_and_depth_info():
            print('info = ', info)
            # e6axis2 = '{E6AXIS: A1 '+str(x)+', A2 -90.0, A3 '+str(z)+', A4 0.0, A5 -90.0, A6 270.0, E1 0.0, E2 0.0, E3 0.0, E4 0.0, E5 0.0, E6 0.0}'
            key = cv2.waitKey(1) & 0xFF
            # rck.moveTo(e6axis2)
        
    camera.close_frames()