import signal
import rclpy
from rclpy.executors import SingleThreadedExecutor
from rclpy.component import ComponentManager

def main():
    print("run component_container")
    try:
        _main()
    except KeyboardInterrupt:
        print('KeyboardInterrupt received, exit')
        return signal.SIGINT


def _main():
    rclpy.init()

    executor = SingleThreadedExecutor()
    component_manager = ComponentManager(executor)

    executor.add_node(component_manager)
    executor.spin()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
