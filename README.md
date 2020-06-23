# The composition example for rclpy(ROS2 python client library)



## Try the example

**For now the  composition API implementation is not in ROS2 base repos**, so we use the customized rclpy, ros2cli and these project for demonstration. I assume you have a ready to work underlay, I'd personally recommend using Docker image `ros2:nightly-dev` to test it to make a minimal impact of your own environment.

First prepare the workspace and related repos

```shell
$ mkdir -p ~/rclpy_composition_ws/src
$ cd ~/rclpy_composition_ws/src
$ git clone --branch composition_api https://github.com/crystaldust/rclpy
$ git clone --branch composition_api https://github.com/crystaldust/ros2cli
$ git clone --branch composition_api https://github.com/crystaldust/rclpy_composition_example
$ cd ../
```

Then, **important: build rclpy first**, since rclpy_composition_example calls `rclpy.component.rclpy_register_components` while building, we are not able to solve the build time dependency availability problem yet.

```shell
$ colcon build --packages-select rclpy
$ source install/setup.bash

$ colcon build --packages-skip rclpy # Build the rest two packages
$ source install/setup.bash
```

When `rclpy_composition_example` is built, the customized component should be registered under the path:

```shell
$ cat install/rclpy_composition_example/share/ament_index/resource_index/rclpy_components/py_composition
py_composition::Talker;rclpy_composition_example.talker_component:Talker
py_composition::Listener;rclpy_composition_example.listener_component:Listener
```

Then test if ros2cli can recognize the rclpy_components:

```shell
$ ros2 component types
...
rclcpp_components/composition
  composition::Talker
  composition::Listener
  composition::NodeLikeListener
  composition::Server
  composition::Client

rclpy_components/py_composition
  py_composition::Talker
  py_composition::Listener
```

A little difference here is, the composition types will begin with a language mark(the `rclcpp_components`, `rclpy_components`).



Run a component_container:

```shell
$ ros2 run rclpy_composition_example component_container
```

Open a new session and call the component commands:

```shell
$ ros2 component list
/PyComponentManager
$ ros2 component load /PyComponentManager py_composition py_composition::Talker
Loaded component 1 into '/PyComponentManager' container node as '/talker'
$ ros2 component load /PyComponentManager py_composition py_composition::Listener
Loaded component 2 into '/PyComponentManager' container node as '/listener'

```

Then go back to the previous session, the container will display the Talker and Listener components' logs:

```shell
[INFO] [1592908811.949662551] [Talker]: Pulibhsing Hello from composition talker 0 
[INFO] [1592908812.918946940] [Talker]: Pulibhsing Hello from composition talker 1 
[INFO] [1592908813.917545186] [Talker]: Pulibhsing Hello from composition talker 2 
[INFO] [1592908814.918682372] [Talker]: Pulibhsing Hello from composition talker 3 
[INFO] [1592908814.922476919] [Listener]: I heard Hello from composition talker 3 
[INFO] [1592908815.918818523] [Talker]: Pulibhsing Hello from composition talker 4 
[INFO] [1592908815.920822898] [Listener]: I heard Hello from composition talker 4
```
