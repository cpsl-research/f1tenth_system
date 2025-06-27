

from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution


def get_sub_launch_description(package_share, subfolders, launch_file):
    return IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [
                PathJoinSubstitution(
                    [
                        get_package_share_directory(package_share),
                        *subfolders,
                        launch_file,
                    ]
                )
            ]
        )
    )
