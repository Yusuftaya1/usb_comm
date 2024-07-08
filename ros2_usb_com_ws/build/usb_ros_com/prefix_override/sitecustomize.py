import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/yusuf/ros2_usb_com_ws/install/usb_ros_com'
