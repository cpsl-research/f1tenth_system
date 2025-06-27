from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node


def generate_launch_description():
    rviz_config_launch_arg = DeclareLaunchArgument(
        "rviz_config", default_value="viz_config_1.rviz"
    )
    rviz_param = PathJoinSubstitution(
        [
            get_package_share_directory("f1tenth_bringup"),
            "config",
            "visualizer",
            LaunchConfiguration("rviz_config"),
        ]
    )

    rviz_node = Node(
        package="rviz2",
        namespace="",
        executable="rviz2",
        name="rviz2",
        parameters=[{"use_sim_time": True}],
        arguments=["-d", rviz_param],
    )

    return LaunchDescription([rviz_config_launch_arg, rviz_node])