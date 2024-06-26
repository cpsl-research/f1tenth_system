import rclpy

from .base import AutoControl, AutoControlException


class WiggleControl(AutoControl):
    """
    Basic control algorithm to make the f1tenth wiggle around
    """

    def __init__(self):
        super().__init__()


def main(args=None):
    rclpy.init(args=args)
    node = WiggleControl()

    try:
        rclpy.spin(node)
    except AutoControlException as e:
        node.get_logger().error(e.message)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()
