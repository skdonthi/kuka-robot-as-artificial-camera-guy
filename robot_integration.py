import time
from py_openshowvar import openshowvar
from camera import check

class RemoteControlKUKA:

    def __init__(self, address="192.168.1.15", port=7000, debug=False):
        self.debug = debug
        self._client = openshowvar(address, port)
        if (not self._client.can_connect):
            raise RuntimeError("Unable to connect.")
            
    def __del__(self):
        self._client.close()

    def _read(self, identifier, debug=False):
        return self._client.read(identifier, debug=debug)
        
    def _write(self, identifier, value, debug=False):
        return self._client.write(identifier, value, debug=self.debug or debug)
        
    def get_pos(self):
        return self._read("$POS_ACT")
        
    def get_axis(self):
        return self._read("$AXIS_ACT")
        
    def is_idle(self):
        return b'0' == self._read("COM_ACTION")
        
    def _set_e6pos(self, e6pos):
        self._write("COM_E6POS",e6pos)
        
    def _set_e6axis(self, e6axis):
        self._write("COM_E6AXIS",e6axis)
        
    def _set_action(self, s_action):
        if (s_action == "PTP_E6POS"):
            a = 11
        elif (s_action == "LIN_E6POS"):
            a = 12
        elif (s_action == "PTP_E6AXIS"):
            a = 13
        else:
            raise NotImplementedError("Unknown action string.")
        self._write("COM_ACTION", str(a))

    def _wait(self, wait=True):
        while (wait and not self.is_idle()):
            time.sleep(0.1)

    def move_lin_e6pos(self, e6pos, block=True):
        self._set_e6pos(e6pos)
        self._set_action("LIN_E6POS")
        self._wait(block)

    def move_ptp_e6pos(self, e6pos, block=True):
        self._set_e6pos(e6pos)
        self._set_action("PTP_E6POS")
        self._wait(block)
    
    def move_ptp_e6axis(self, e6axis, block=False):
        self._set_e6axis(e6axis)
        self._set_action("PTP_E6AXIS")
        self._wait(block)
        
    def moveTo(self,coordinates, flag=True):
        rck = RemoteControlKUKA()
        print("robot")
        # print(coordinates)
        # y = 135.903534
        # y = (coordinates[0]-320)/12
        # z = 887.51    
        # e6pos1 = '{X 425.297516,Y '+str(y)+',Z '+str(z)+',A -179.973938,B 67.7722855,C -179.862015,S 6,T 27,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}'
        # e6pos1 = '{A1 425.297516,A2 '+str(y)+',A3 '+str(z)+',A4 -179.973938,A5 67.7722855,A6 -179.862015,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}'

        while flag:
            # e6axis1 = '{E6AXIS: A1 '+str(y)+', A2 -90.0, A3 100.0, A4 0.0, A5 0.0, A6 0.0, E1 0.0, E2 0.0, E3 0.0, E4 0.0, E5 0.0, E6 0.0}'
            print(coordinates)
            # print(rck.get_axis())
            rck.move_ptp_e6axis(coordinates)
            flag = False
            
    # if __name__ == '__main__':
    # rck = RemoteControlKUKA()
    # y = 135.903534
    # z = 691.804626
    # rck.moveTo('{A1 425.297516,A2 '+str(y)+',A3 '+str(z)+',A4 -179.973938,A5 67.7722855,A6 -179.862015,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}')