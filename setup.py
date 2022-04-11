#!/usr/bin/env python
# setup.py
"""Install script for ROS1 catkin / ROS2 ament_python."""

from setuptools import setup

package_name = 'ah_ros_bridge_example'

setup(
 name=package_name,
 version='0.0.0',
 packages=[package_name, package_name+".module"],
 data_files=[
     ('share/ament_index/resource_index/packages',
             ['resource/' + package_name]),
     ('share/' + package_name, ['package.xml']),
   ],
 install_requires=['setuptools'],
 zip_safe=True,
 author='Jaroslav Klapálek',
 author_email='klapajar@fel.cvut.cz',
 maintainer='Jaroslav Klapálek',
 maintainer_email='klapajar@fel.cvut.cz',
 description='An example of ROS connector for Arrowhead Framework.',
 license='GPLv3',
 tests_require=['pytest'],
 entry_points={
     'console_scripts': [
             'run = ah_ros_bridge_example.run:main'
     ],
   },
)
