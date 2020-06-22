import signal
import rclpy
from rclpy.executors import SingleThreadedExecutor
from rclpy.component import ComponentManager
from .talker_component import MyTalker
from .utils import register_component

from . import talker_component


# print("............ register component mycomposition::MyTalker")
# register_component("mycomposition::MyTalker", talker_component)

def main():
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
