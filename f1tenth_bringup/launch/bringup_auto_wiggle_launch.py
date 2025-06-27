from launch import LaunchDescription
from .utils import get_sub_launch_description


def generate_launch_description():
    # base nodes to run f1tenth
    base_nodes = get_sub_launch_description(
        "f1tenth_bringup", ["launch"], "base_launch.py",
    )

    # algorithm stack nodes
    stack_nodes = get_sub_launch_description(
        "f1tenth_bringup", ["launch", "stacks"], "wiggle_stack_launch.py",
    )

    return LaunchDescription(
        [
            base_nodes,
            stack_nodes
        ]
    )
