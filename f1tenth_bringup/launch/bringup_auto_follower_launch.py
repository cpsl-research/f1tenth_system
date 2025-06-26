# MIT License

# Copyright (c) 2020 Hongrui Zheng

# Permission is hereby granted, free of charge, to any person obtaining a co py
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    joy_teleop_config = os.path.join(
        get_package_share_directory("f1tenth_bringup"), "config", "joy_teleop.yaml"
    )
    vesc_config = os.path.join(
        get_package_share_directory("f1tenth_bringup"), "config", "vesc.yaml"
    )
    sensors_config = os.path.join(
        get_package_share_directory("f1tenth_bringup"), "config", "sensors.yaml"
    )
    mux_config = os.path.join(
        get_package_share_directory("f1tenth_bringup"), "config", "mux.yaml"
    )
    auto_config = os.path.join(
        get_package_share_directory("f1tenth_bringup"), "config", "auto_control.yaml"
    )
    percep_config = os.path.join(
        get_package_share_directory("f1tenth_bringup"), "config", "percep.yaml"
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

    joy_la = DeclareLaunchArgument(
        "joy_config",
        default_value=joy_teleop_config,
        description="Descriptions for joy and joy_teleop configs",
    )
    vesc_la = DeclareLaunchArgument(
        "vesc_config",
        default_value=vesc_config,
        description="Descriptions for vesc configs",
    )
    sensors_la = DeclareLaunchArgument(
        "sensors_config",
        default_value=sensors_config,
        description="Descriptions for sensor configs",
    )
    mux_la = DeclareLaunchArgument(
        "mux_config",
        default_value=mux_config,
        description="Descriptions for ackermann mux configs",
    )
    auto_la = DeclareLaunchArgument(
        "auto_config",
        default_value=auto_config,
        description="Descriptions for autonomous mode config",
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

    ld = LaunchDescription([
        joy_la,
        vesc_la,
        sensors_la,
        mux_la,
        auto_la,
        percep_la,
        track_la,
        planning_la,
        control_la,
    ])

    joy_node = Node(
        package="joy",
        executable="joy_node",
        name="joy",
        parameters=[LaunchConfiguration("joy_config")],
    )
    joy_teleop_node = Node(
        package="joy_teleop",
        executable="joy_teleop",
        name="joy_teleop",
        parameters=[LaunchConfiguration("joy_config")],
    )
    ackermann_to_vesc_node = Node(
        package="vesc_ackermann",
        executable="ackermann_to_vesc_node",
        name="ackermann_to_vesc_node",
        parameters=[LaunchConfiguration("vesc_config")],
    )
    vesc_to_odom_node = Node(
        package="vesc_ackermann",
        executable="vesc_to_odom_node",
        name="vesc_to_odom_node",
        parameters=[LaunchConfiguration("vesc_config")],
    )
    vesc_driver_node = Node(
        package="vesc_driver",
        executable="vesc_driver_node",
        name="vesc_driver_node",
        parameters=[LaunchConfiguration("vesc_config")],
    )
    throttle_interpolator_node = Node(
        package="f1tenth_stack",
        executable="throttle_interpolator",
        name="throttle_interpolator",
        parameters=[LaunchConfiguration("vesc_config")],
    )
    urg_node = Node(
        package="urg_node",
        executable="urg_node_driver",
        name="urg_node",
        parameters=[LaunchConfiguration("sensors_config")],
    )
    ackermann_mux_node = Node(
        package="ackermann_mux",
        executable="ackermann_mux",
        name="ackermann_mux",
        parameters=[LaunchConfiguration("mux_config")],
        remappings=[("ackermann_drive_out", "ackermann_cmd")]
        # remappings=[('ackermann_cmd_out', 'ackermann_drive')]
    )
    static_tf_node = Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        name="static_baselink_to_laser",
        arguments=["0.27", "0.0", "0.11", "0.0", "0.0", "0.0", "base_link", "laser"],
    )

    # object detection from 2D images
    # percep_camera_node = Node(
    #     package="avstack_bridge",
    #     executable="mmdetection2d",
    #     name="perception_2d",
    #     parameters=[LaunchConfiguration("percep_config")],
    #     # remappings=[
    #     #     ("point_cloud", "lidar0"),
    #     #     ("detections_3d", det_topic),
    #     # ],
    #     arguments=["--ros-args", "--log-level", "INFO"],
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
    )

    # finalize
    ld.add_action(joy_node)
    ld.add_action(joy_teleop_node)
    ld.add_action(ackermann_to_vesc_node)
    ld.add_action(vesc_to_odom_node)
    ld.add_action(vesc_driver_node)
    # ld.add_action(throttle_interpolator_node)
    ld.add_action(urg_node)
    ld.add_action(ackermann_mux_node)
    ld.add_action(static_tf_node)
    ld.add_action(percep_lidar_node)
    ld.add_action(track_lidar_node)
    ld.add_action(control_node)

    return ld
