import rclpy
import ackermann_msgs.msg

from .base import set_member, AutoControl, AutoControlException


class StraightControl(AutoControl):
    """Basic control algorithm to make the f1tenth go straight"""

    def __init__(self):
        super().__init__()

    def get_control_command(self) -> ackermann_msgs.msg.AckermannDriveStamped:
        # get ackermann command
        drive = ackermann_msgs.msg.AckermannDrive()
        # -- lateral
        set_member(drive, "steering_angle", 0.0)
        set_member(drive, "steering_angle_velocity", 0.0)
        # -- longitudinal
        set_member(drive, "speed", 0.5)
        set_member(drive, "acceleration", 0.0)
        set_member(drive, "jerk", 0.0)

        # package in stamped message
        msg = ackermann_msgs.msg.AckermannDriveStamped()
        set_member(msg.header, "stamp", self.get_clock().now().to_msg())
        set_member(msg, "drive", drive)

        return msg


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
