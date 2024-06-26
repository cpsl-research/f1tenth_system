import importlib
import typing

import rclpy
from rclpy.node import Node
import sensor_msgs.msg
import std_msgs.msg


class AutoControlException(Exception):
    pass


def get_interface_type(type_name: str, interface_type: str) -> typing.Any:
    split = type_name.split('/')
    if len(split) != 3:
        raise AutoControlException("Invalid type_name '{}'".format(type_name))
    package = split[0]
    interface = split[1]
    message = split[2]
    if interface != interface_type:
        raise AutoControlException("Cannot use interface of type '{}' for an '{}'"
                                 .format(interface, interface_type))

    mod = importlib.import_module(package + '.' + interface_type)
    return getattr(mod, message)


class AutoControl(Node):
    """Base class for autonomous control"""
    def __init__(self):
        super().__init__('auto_control', allow_undeclared_parameters=True,
                    automatically_declare_parameters_from_overrides=True)

        # Don't subscribe until everything has been initialized.
        qos = rclpy.qos.QoSProfile(history=rclpy.qos.QoSHistoryPolicy.KEEP_LAST,
                                   depth=1,
                                   reliability=rclpy.qos.QoSReliabilityPolicy.RELIABLE,
                                   durability=rclpy.qos.QoSDurabilityPolicy.VOLATILE)
        self._subscription = self.create_subscription(
            std_msgs.msg.Int8, 'autonomous', self.auto_callback, qos)
        
    def auto_callback(self, msg: std_msgs.msg.Int8) -> None:
        self.get_logger().info("callback reached!")