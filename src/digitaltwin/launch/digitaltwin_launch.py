from  launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    print("Running custom launcher...")
    
    return LaunchDescription([
        Node(
            package='digitaltwin',
            executable='asset.py',
            name='uav_asset',
            output='screen',
            emulate_tty=True,
            arguments=['--ros-args', '--log-level', 'debug'],
        ),
        Node(
            package='digitaltwin',
            executable='twin.py',
            name='uav_twin',
            output='screen',
            emulate_tty=True,
            arguments=['--ros-args', '--log-level', 'debug'],
        ),
    ])
