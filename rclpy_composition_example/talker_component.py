from std_msgs.msg import String
from rclpy.node import Node


class Talker(Node):
    def __init__(self, node_name, *kargs, topic_name="py_composition_topic", timer_period=1, **kwargs):
        super().__init__(node_name, *kargs, **kwargs)
        self.publisher_ = self.create_publisher(String, topic_name, 10)
        self.timer_ = self.create_timer(timer_period, self.on_timer)
        self.i = 0

    def on_timer(self):
        msg = String()
        msg.data = "Hello from composition talker %d " % self.i
        self.publisher_.publish(msg)
        self.get_logger().info("Pulibhsing %s" % msg.data)
        self.i += 1
