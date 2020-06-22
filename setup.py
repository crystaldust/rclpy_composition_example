from setuptools import setup
from setuptools.command.install import install
from setuptools.command.develop import develop
from setuptools.command.build_py import build_py

package_name = 'rclpy_composition_example'


class PostInstallCommand(install):
    def run(self):
        install.run(self)
        print('POST INSTALL CALLED!', flush=True)
        print('dir(self):', dir(self))


from os import system
from rclpy_composition_example.utils import register_component_in_setuppy


class PostDevelopCommand(develop):
    def run(self):
        develop.run(self)
        print('POST DEVELOP CALLED!')
        register_component_in_setuppy(package_name, rclpy_components)


class PostBuildPyCommand(build_py):
    def run(self):
        build_py.run(self)
        print('POST BUILD PY CALLED!')
        system('date > /tmp/post_build')


rclpy_components = [
    'my_composition::Talker = rclpy_composition_example.talker_component:MyTalker'
]

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
            'run_container = rclpy_composition_example.run_container:main'
        ],
        'rclpy_components': rclpy_components
    },
    cmdclass={
        # 'install': PostInstallCommand,
        # 'build_py': PostBuildPyCommand,
        'develop': PostDevelopCommand,
    },
)
