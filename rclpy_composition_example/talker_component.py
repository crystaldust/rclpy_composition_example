from std_msgs.msg import String
from rclpy.node import Node


class MyTalker(Node):
    def __init__(self, node_name, *kargs, **kwargs):
        super().__init__(node_name, *kargs, **kwargs)
        self.publisher_ = self.create_publisher(String, "composition_topic", 10)
        self.timer_ = self.create_timer(1, self.on_timer)
        self.i = 0

    def on_timer(self):
        msg = String()
        msg.data = "Hello from composition talker %d " % self.i
        self.publisher_.publish(msg)
        self.get_logger().info("Pulibhsing %s" % msg.data)
        self.i += 1
