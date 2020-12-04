cmake_minimum_required(VERSION 3.0.2)
project(trigno_capture)
find_package(catkin REQUIRED COMPONENTS rospy)

## Uncomment this if the package has a setup.py. This macro ensures
## modules and global scripts declared therein get installed
## See http://ros.org/doc/api/catkin/html/user_guide/setup_dot_py.html
catkin_python_setup()

#add_service_files(
#    DIRECTORY srv
#    FILES
#    MotionCapture.srv
#    RawCameraTransforms.srv
#    RawCameraTransformsV2.srv
#    IntrinsicCalibration.srv
#)
#generate_messages(DEPENDENCIES std_msgs geometry_msgs sensor_msgs visp_hand2eye_calibration)
catkin_package(
    CATKIN_DEPENDS 
    rospy 
)
include_directories(include ${catkin_INCLUDE_DIRS})


