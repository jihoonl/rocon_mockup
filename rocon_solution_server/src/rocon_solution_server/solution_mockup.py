#! /usr/bin/env python

import rospy
import random
from rocon_solution_msgs.msg import *

class SolutionMockup():

    pub = {}
    srv = {}

    agents = [] 
    services = []

    def __init__(self):
        self.pub['service_list'] = rospy.Publisher('~rocon_service_list',RoconServiceList, latch=True)
        self.pub['agent_list'] = rospy.Publisher('~concert_agent_list',RoconAgentList, latch=True)

    def create_fake_agents(self):
        name = ["Marcus","Daniel","Jorge","Huey","Jihoon","Amigo"]

        for n in name:
            agent = RoconAgent(n,"Dummy",random.randint(0,2),[])
            self.agents.append(agent)

    def create_fake_services(self):
        name = ["Drink Delivery","Floor Cleaning","Sensor Validation"]

        for n in name:
            service = RoconService(n,random.randint(0,2),range(random.randint(1,4)),['Waiter','Manager'],['speed:99m/s','Brilliantness: low'])
            self.services.append(service)

    def publish_servicelist(self,list):
        self.pub['service_list'].publish(list)

    def publish_agentlist(self,list):
        self.pub['agent_list'].publish(list)

    def spin(self):
        self.create_fake_agents()
        self.create_fake_services()
        self.publish_agentlist(self.agents)
        self.publish_servicelist(self.services)
#        self.publish_jobs(self.jobs)
        rospy.spin()
