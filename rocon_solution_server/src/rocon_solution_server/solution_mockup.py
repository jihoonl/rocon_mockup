#! /usr/bin/env python

import rospy
from rocon_solution_server.msg import RoconService, RoconServiceList

class SolutionMockup():

    pub = {}
    srv = {}

    def __init__(self):
        self.pub['service_list'] = rospy.Publisher('~rocon_service_list',RoconServiceList)


    def spin(self):

        rospy.spin()
