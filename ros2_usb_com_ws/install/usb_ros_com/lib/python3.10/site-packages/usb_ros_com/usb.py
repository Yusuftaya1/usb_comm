import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import serial

class CmdVelToSerial(Node):
    def __init__(self):
        super().__init__('cmd_vel_to_serial')
        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.listener_callback,
            10)
        #self.serial_port = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        self.get_logger().info('Seri port açıldı')
        self.wheel_distance = 0.5

    def listener_callback(self, msg):
        # Mesajdaki değerlerin sınırlanması
        if msg.linear.x > 1000:
            msg.linear.x = 1000.0
        
        if msg.linear.x < -1000:
            msg.linear.x = -1000.0

        if msg.linear.y > 1000:
            msg.linear.y = 1000.0
        
        if msg.linear.y < -1000:
            msg.linear.y = -1000.0

        if msg.angular.z < 0:
            msg.linear.x*=-1
            
        # Diferansiyel sürüş hesaplamaları
        v = msg.linear.x
        w = msg.angular.z
        d = self.wheel_distance
        
        v_left = v - (d / 2) * w
        v_right = v + (d / 2) * w

        data_dict = {
            "v_left": v_left,
            "v_right": v_right
        }
        data_list =[v_left,v_right]

        data_str = f"left: {v_left}, right: {v_right}\n"
    
        #self.serial_port.write(data_str.encode())
        self.get_logger().info(f'Seri porta gönderilen veri: {data_dict}')

def main(args=None):
    rclpy.init(args=args)
    node = CmdVelToSerial()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
