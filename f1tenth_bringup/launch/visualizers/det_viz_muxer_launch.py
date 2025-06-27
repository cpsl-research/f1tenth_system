from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    det_muxer_node = Node(
        package="detection_visualizer",
        namespace="",
        executable="detection_visualizer",
        name="detection_visualizer",
        remappings=[
            ("/detections", "/detections_2d"),
            ("/images", "/robot1/camera/color/image_raw"),
            ("/dbg_images", "/image_detection_mux"),
        ]
    )

    return LaunchDescription([det_muxer_node])