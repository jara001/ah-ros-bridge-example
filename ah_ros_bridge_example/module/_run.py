#!/usr/bin/env python
# _run.py
"""Run node for ah_ros_bridge_example.
"""
######################
# Imports & Globals
######################

from autopsy.node import Node


######################
# RunNode
######################

class RunNode(Node):

    def __init__(self):
        super(Node, self).__init__("ah_ros_bridge_example")


