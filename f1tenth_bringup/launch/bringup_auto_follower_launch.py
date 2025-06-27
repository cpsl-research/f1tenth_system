

from launch import LaunchDescription
from .utils import get_sub_launch_description


def generate_launch_description():
    # base nodes to run f1tenth
    base_nodes = get_sub_launch_description(
        "f1tenth_bringup", ["launch"], "base_launch.py",
    )

    # camera sensor
    realsense_nodes = get_sub_launch_description(
        "f1tenth_bringup", ["launch", "sensors"], "realsense_launch.py",
    )

    # lidar sensor
    hokuyo_nodes =get_sub_launch_description(
        "f1tenth_bringup", ["launch", "sensors"], "hokuyo_launch.py",
    )

    # algorithm stack nodes
    stack_nodes = get_sub_launch_description(
        "f1tenth_bringup", ["launch", "stacks"], "follower_stack_launch.py",
    )

    # visualization nodes
    muxer_nodes = get_sub_launch_description(
        "f1tenth_bringup", ["launch", "visualizers"], "det_viz_muxer_launch.py",
    )

    # rviz nodes
    rviz_nodes = get_sub_launch_description(
        "f1tenth_bringup", ["launch", "visualizers"], "rviz_node_launch.py",
    )

    return LaunchDescription(
        [
            base_nodes,
            realsense_nodes,
            hokuyo_nodes,
            stack_nodes,
            muxer_nodes,
            rviz_nodes,
        ]
    )
