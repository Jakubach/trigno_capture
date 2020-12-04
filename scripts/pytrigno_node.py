#!/usr/bin/env python3
import rospy
from pytrigno.pytrigno import TrignoOrientation


class TrignoCapture:
    def __init__(self):
        self.trigno_sensor = TrignoOrientation(channel_range = (0,2), samples_per_read = 100)
    def stop(self):
        self.trigno_sensor.stop()
        
        
if __name__ == "__main__":
    rospy.init_node("emg_capture")
    trigno_capture = TrignoCapture()
    rospy.on_shutdown(trigno_capture.stop)
    rospy.loginfo("Sensor node is ready.")
    rospy.spin()
