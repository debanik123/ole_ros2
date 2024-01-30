import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class LidarSubscriber(Node):
    def __init__(self):
    
        super().__init__('lidar_detection')
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan', 
            self.lidar_callback,
            10
        )
        self.stop_cmd_publisher = self.create_publisher(Twist, '/cmd_vel', 10)

    def lidar_callback(self, msg):
        
        #start_index = int((100 - msg.angle_min) / msg.angle_increment)
        #end_index = int((120 - msg.angle_min) / msg.angle_increment)
        start_index = 600
        end_index = 1200

        for i in range(start_index, end_index + 1):
            range_value = msg.ranges[i]
            if range_value < 0.5:
                self.send_stop_command()
                print(msg.ranges[i])
                print("Obstacle is detected")
                
            else:
                print("Obstacle is not detected")
             
    def send_stop_command(self):
        stop_cmd = Twist()
        stop_cmd.linear.x = 0.0
        stop_cmd.angular.z = 0.0
        self.stop_cmd_publisher.publish(stop_cmd)

def main(args=None):
    rclpy.init(args=args)
    lidar_subscriber = LidarSubscriber()
    rclpy.spin(lidar_subscriber)
    lidar_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

