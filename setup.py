from setuptools import setup

package_name = 'rclpy_composition_example'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
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

