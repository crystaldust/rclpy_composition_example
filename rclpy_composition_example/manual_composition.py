import rclpy
from rclpy.executors import SingleThreadedExecutor
from talker_component import MyTalker

def main():
    rclpy.init()

    executor = SingleThreadedExecutor()

    node = MyTalker('mytalker')
    executor.add_node(node)
    executor.spin()

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
