# The composition example for rclpy



## Try the example

**For now the  composition API implementation is not in ROS2 base repos**, so we use the customized rclpy, ros2cli for demonstration. I assume you have a underlay ready to work, I'd personally recommend using Docker image `ros2:nightly-dev` to test it to make a minimal impact of your own environment.

First prepare the workspace and related repos

```shell
$ mkdir -p ~/rclpy_composition_ws/src
$ cd ~/rclpy_composition_ws/src
$ git clone --branch composition-api https://github.com/crystaldust/rclpy
$ git clone --branch composition-api-py-entrypoints https://github.com/crystaldust/ros2cli
$ git clone --branch composition-api https://github.com/crystaldust/rclpy_composition_example
$ cd ../
```

Then build and source the environment script, use `which ros2` command to check if our customized cli tool is being used:

```shell
$ colcon build
$ source install/setup.bash
$ which ros2
/root/rclpy_composition_ws/install/ros2cli/bin/ros2 # Make sure it's not /opt/ros/<distro>/bin/ros2
```

Test if ros2cli can recognize the rclpy_components:

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

A little difference here is, the composition types will begin with a language mark(the `rclcpp_components`, `rclpy_components`), let's run a component_container:

```shell
$ ros2 run rclpy_composition_example component_container
```

Open a new session and call the component commands:

```shell
$ source ~/rclpy_composition_ws/install/setup.bash # Don't forget to update the environment
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

## What's happening behind this?

If you look into the `setup.py` file you'll find the entry_points parameter for composition:

```python
setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
	entry_points={
        'console_scripts': [
            'component_container = rclpy_composition_example.component_container:main',
            'component_container_mt = rclpy_composition_example.component_container_mt:main',
        ],
        'rclpy_components': [
            'py_composition::Talker = rclpy_composition_example.talker_component:Talker',
            'py_composition::Listener = rclpy_composition_example.listener_component:Listener',
        ]
    },
)
```

Here we declares a couple of `rclpy_components` entry points which will let the ros2cli component verb find the entry point values. Then when loading components, the component container will be able to access the actual class reference, instantiate it and put the instance into the executor.
