#! /usr/bin/env python

import rospy
from rocon_solution_server.msg import *

class SolutionMockup():

    pub = {}
    srv = {}

    agents = [] 
    services = []

    def __init__(self):
        self.pub['service_list'] = rospy.Publisher('~rocon_service_list',RoconServiceList, latch=True)
        self.pub['agent_list'] = rospy.Publisher('~concert_agent_list',RoconAgentList, latch=True)

    def create_agents(self):
        name = ["Marcus","Daniel","Jorge","Huey"]

        for n in name:
            agent = RoconAgent(n,"Dummy")
            self.agents.append(agent)

    def publish_servicelist(self,list):
        self.pub['service_list'].publish(list)

    def publish_agentlist(self,list):
        self.pub['agent_list'].publish(list)

    def spin(self):
        self.create_agents()
        self.publish_agentlist(self.agents)
        self.publish_servicelist(self.services)
        rospy.spin()
