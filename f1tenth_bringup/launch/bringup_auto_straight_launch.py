

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution


def generate_launch_description():
    # base nodes to run f1tenth
    base_nodes = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [
                PathJoinSubstitution(
                    [
                        get_package_share_directory("f1tenth_bringup"),
                        "launch",
                        "base_launch.py",
                    ]
                )
            ]
        ),
    )

    # algorithm stack nodes
    stack_nodes = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [
                PathJoinSubstitution(
                    [
                        get_package_share_directory("f1tenth_bringup"),
                        "launch",
                        "stacks",
                        "straight_stack_launch.py",
                    ]
                )
            ]
        ),
    )

    return LaunchDescription(
        [
            base_nodes,
            stack_nodes
        ]
    )
