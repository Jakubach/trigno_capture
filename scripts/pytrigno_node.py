#!/usr/bin/env python3
import rospy
from pytrignos.pytrignos import TrignoAdapter


class TrignoCapture:
    def __init__(self):
        self.trigno_sensors = TrignoAdapter()
        self.trigno_sensors.add_sensors(sensors_mode='ORIENTATION', sensors_ids=(1,), sensors_labels=('ORIENTATION1',), host='192.168.4.118')
    def start(self):
        self.trigno_sensors.start_acquisition()
    def stop(self):
        self.trigno_sensors.stop_acquisition()
        
        
if __name__ == "__main__":
    rospy.init_node("trigno_capture")
    trigno_capture = TrignoCapture()
    trigno_capture.start()
    rospy.on_shutdown(trigno_capture.stop)
    rospy.loginfo("Sensor node is ready.")
    rospy.spin()
