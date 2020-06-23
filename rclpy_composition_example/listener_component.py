from std_msgs.msg import String
from rclpy.node import Node


class Listener(Node):
    def __init__(self, node_name, *kargs, topic_name="py_composition_topic", **kwargs):
        super().__init__(node_name, *kargs, **kwargs)
        self.subscription_ = self.create_subscription(String, topic_name, self.on_receive_msg, 0)


    def on_receive_msg(self, msg):
        self.get_logger().info("I heard %s" % msg.data)
