

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    sensors_config = os.path.join(
        get_package_share_directory("f1tenth_bringup"), "config", "sensors.yaml"
    )

    sensors_la = DeclareLaunchArgument(
        "sensors_config",
        default_value=sensors_config,
        description="Descriptions for sensor configs",
    )

    ld = LaunchDescription([sensors_la])

    urg_node = Node(
       package='urg_node',
       executable='urg_node_driver',
       name='urg_node',
       parameters=[LaunchConfiguration('sensors_config')]
    )

    ld.add_action(urg_node)

    return ld
