#!/usr/bin/env python3
# _run.py
"""Run node for ah_ros_bridge_example.
"""
######################
# Imports & Globals
######################

from autopsy.node import Node

from aclpy.client.client_pkcs12 import ArrowheadClient
from aclpy.interface import ArrowheadInterface
from aclpy.server import ArrowheadServer
from aclpy.service import ArrowheadService


######################
# RunNode
######################

class RunNode(Node):

    def __init__(self):
        super(Node, self).__init__("ah_ros_bridge_example")

        from . import configuration
        """Expected contents:
        Server = ArrowheadServer(
            address = AH_CORE_IP_ADDRESS,
        )

        Interface = ArrowheadInterface(
            name = NAME_OF_THE_INTERFACE,
        )

        Service = ArrowheadService(
            name = NAME_OF_THE_SERVICE,
        )

        Client = ArrowheadClient(
            name = NAME_OF_THE_SYSTEM,
            address = SYSTEM_IP_ADDRESS,
            port = SYSTEM_PORT,
            pubfile = PATH_TO_PUB_FILE,
            p12file = PATH_TO_P12_FILE,
            p12pass = PASS_TO_P12_FILE,
            cafile = PATH_TO_CA_FILE,
            server = Server,
            interfaces = [Interface],
        )
        """
        self.server = configuration.Server
        self.client = configuration.Client
        self.service = configuration.Service
        self.interface = configuration.Interface

        # Communicate with AHCore
        self.client.obtain_id()

        if self.client.id < 0:
            raise Exception ("Unable to communicate with AHCore.")

        success, matches = self.client.orchestrate(self.service)

        if not success:
            print (self.client.last_error)
            raise Exception ("Unable to communicate with Orchestrator.")

        if len(matches) == 0:
            raise Exception ("No matched providers. Is the target system running?")

        print ("Found %d provider(s):" % len(matches))
        for _i, match in enumerate(matches):
            print ("\t%d: %s:%d" % (_i + 1, match.get("provider").address, match.get("provider").port))
