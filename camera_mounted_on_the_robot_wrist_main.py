from basler import face_detection
from robot_integration import RemoteControlKUKA
import time

   
if __name__ == '__main__':
    rck = RemoteControlKUKA()
    x=0
    z=100
    home = '{E6AXIS: A1 0, A2 -90.0, A3 90.0, A4 0.0, A5 -90.0, A6 270.0, E1 0.0, E2 0.0, E3 0.0, E4 0.0, E5 0.0, E6 0.0}'
    rck.moveTo(home)

    while True:
        for position in face_detection():
            print("main")
            print(position)
            
            x = x+(position[0]-320)/12
            # z = 100-((position[1]-225)/8.75)
            z = max(min(100-((position[1]-225)/8.75), 120), 70)
            e6axis1 = '{E6AXIS: A1 '+str(x)+', A2 -90.0, A3 90.0, A4 0.0, A5 -90.0, A6 270.0, E1 0.0, E2 0.0, E3 0.0, E4 0.0, E5 0.0, E6 0.0}'
            e6axis2 = '{E6AXIS: A1 '+str(x)+', A2 -90.0, A3 '+str(z)+', A4 0.0, A5 -90.0, A6 270.0, E1 0.0, E2 0.0, E3 0.0, E4 0.0, E5 0.0, E6 0.0}'
            
            # e6axis1 = '{E6AXIS: A1 '+str(x)+', A2 -90.0, A3 '+str(z)+', A4 0.0, A5 -90.0, A6 0.0, E1 0.0, E2 0.0, E3 0.0, E4 0.0, E5 0.0, E6 0.0}'

            # z = 887.51    
            # rck.move_lin_e6pos('{X 425.297516,Y '+str(y)+',Z '+str(z)+',A -179.973938,B 67.7722855,C -179.862015,S 6,T 27,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}')
            print("----------------------")
            print(e6axis2)
            # time.sleep(5)
            print(position)
            rck.moveTo(e6axis2)