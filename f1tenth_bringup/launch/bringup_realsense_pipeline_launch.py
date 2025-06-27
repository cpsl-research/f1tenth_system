import os
import sys
from launch import LaunchDescription

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)
from utils import get_sub_launch_description


def generate_launch_description():
    # camera sensor
    realsense_nodes = get_sub_launch_description(
        "f1tenth_bringup", ["launch", "sensors"], "realsense_launch.py",
    )

    # detection stack
    stack_nodes = get_sub_launch_description(
        "f1tenth_bringup", ["launch", "stacks"], "image_detector_launch.py",
    )

    # muxer nodes
    muxer_nodes = get_sub_launch_description(
        "f1tenth_bringup", ["launch", "visualizers"], "det_viz_muxer_launch.py",
    )

    # rviz nodes
    rviz_nodes = get_sub_launch_description(
        "f1tenth_bringup", ["launch", "visualizers"], "rviz_image_node_launch.py",
    )

    return LaunchDescription(
        [
            realsense_nodes,
            stack_nodes,
            muxer_nodes,
            rviz_nodes,
        ]
    )