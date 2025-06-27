
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
    track_config = os.path.join(
        get_package_share_directory("f1tenth_bringup"), "config", "tracking.yaml"
    )
    planning_config = os.path.join(
        get_package_share_directory("f1tenth_bringup"), "config", "planning.yaml"
    )
    control_config = os.path.join(
        get_package_share_directory("f1tenth_bringup"), "config", "control.yaml"
    )

    percep_la = DeclareLaunchArgument(
        "percep_config",
        default_value=percep_config,
        description="Descriptions for perception config",
    )
    track_la = DeclareLaunchArgument(
        "track_config",
        default_value=track_config,
        description="Descriptions for tracking config",
    )
    planning_la = DeclareLaunchArgument(
        "planning_config",
        default_value=planning_config,
        description="Descriptions for planning config",
    )
    control_la = DeclareLaunchArgument(
        "control_config",
        default_value=control_config,
        description="Descriptions for control config",
    )

    ld = LaunchDescription([percep_la, track_la, planning_la, control_la])


    # object detection from 2D images
    # percep_camera_node = Node(
    #     package="avstack_bridge",
    #     executable="mmdetection2d",
    #     name="perception_2d",
    #     parameters=[LaunchConfiguration("percep_config")],
        # arguments=["--ros-args", "--log-level", "INFO"],
    # )

    # object detection from 3D point clouds
    percep_lidar_node = Node(
        package="avstack_perception",
        executable="laserscan_box_detection",
        name="perception_lidar",
        parameters=[LaunchConfiguration("percep_config")],
        arguments=["--ros-args", "--log-level", "INFO"],
    )

    # object tracking from 3D boxes
    track_lidar_node = Node(
        package="avstack_tracking",
        executable="box3d_tracker",
        name="tracking_3d",
        parameters=[LaunchConfiguration("track_config")],
        arguments=["--ros-args", "--log-level", "INFO"],
    )

    # motion planning node
    # not yet...

    # control node
    control_node = Node(
        package="auto_py",
        executable="follower_control",
        name="follower_control",
        parameters=[LaunchConfiguration("control_config")],
        arguments=["--ros-args", "--log-level", "INFO"],
    )

    # add nodes
    ld.add_action(percep_lidar_node)
    ld.add_action(track_lidar_node)
    ld.add_action(control_node)

    return ld