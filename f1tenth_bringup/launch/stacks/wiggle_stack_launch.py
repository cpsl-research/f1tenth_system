
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    control_config = os.path.join(
        get_package_share_directory("f1tenth_bringup"), "config", "control.yaml"
    )

    control_la = DeclareLaunchArgument(
        "control_config",
        default_value=control_config,
        description="Descriptions for control config",
    )

    ld = LaunchDescription([control_la])


    # control node
    control_node = Node(
        package="auto_py",
        executable="wiggle_control",
        name="wiggle_control",
        parameters=[LaunchConfiguration("auto_config")],
    )

    # add nodes
    ld.add_action(control_node)

    return ld