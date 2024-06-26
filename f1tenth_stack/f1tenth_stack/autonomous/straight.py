import rclpy

from .base import AutoControl, AutoControlException


class StraightControl(AutoControl):
    """Basic control algorithm to make the f1tenth go straight"""

    def __init__(self):
        super().__init__()


def main(args=None):
    rclpy.init(args=args)
    node = StraightControl()

    try:
        rclpy.spin(node)
    except AutoControlException as e:
        node.get_logger().error(e.message)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()
