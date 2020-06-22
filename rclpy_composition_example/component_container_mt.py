import signal
import rclpy
from rclpy.executors import MultiThreadedExecutor
from rclpy.component import ComponentManager

def main():
    try:
        _main()
    except KeyboardInterrupt:
        print('KeyboardInterrupt received, exit')
        return signal.SIGINT


def _main():
    rclpy.init()

    executor = MultiThreadedExecutor()
    component_manager = ComponentManager(executor)

    executor.add_node(component_manager)
    executor.spin()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
