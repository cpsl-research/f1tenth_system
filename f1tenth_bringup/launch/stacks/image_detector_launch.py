
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    # config files
    percep_config = os.path.join(
        get_package_share_directory("f1tenth_bringup"), "config", "perception.yaml"
    )

    percep_la = DeclareLaunchArgument(
        "percep_config",
        default_value=percep_config,
        description="Descriptions for perception config",
    )

    track_config = os.path.join(
        get_package_share_directory("f1tenth_bringup"), "config", "tracking.yaml"
    )

    track_la = DeclareLaunchArgument(
        "track_config",
        default_value=track_config,
        description="Descriptions for tracking config",
    )

    ld = LaunchDescription([percep_la, track_la])


    # object detection from 2D images
    percep_camera_node = Node(
        package="avstack_perception",
        executable="mmdetection2d",
        name="perception_2d",
        remappings=[
            ("image", "/robot1/camera/color/image_raw"),
        ],
        parameters=[LaunchConfiguration("percep_config")],
        arguments=["--ros-args", "--log-level", "INFO"],
    )

    # tracks from 2D boxes
    track_camera_node = Node(
        package="avstack_tracking",
        executable="box2d_tracker",
        name="tracking_2d",
        parameters=[LaunchConfiguration("track_config")],
        arguments=["--ros-args", "--log-level", "INFO"],
    )

    # add nodes
    ld.add_action(percep_camera_node)
    ld.add_action(track_camera_node)

    return ld