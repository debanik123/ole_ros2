# ole_ws
added ole_ws for localization

```
cd ros2_ws/src/
git clone https://github.com/debanik123/ole_ros2.git
cd ..
colcon build --packages-select ouster_msgs ros2_ouster
source ~/ros2_ws/install/setup.bash
ros2 launch ros2_ouster ole2dv2_launch.py

```
