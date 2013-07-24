#! /usr/bin/env python
import rospy
import threading
import std_srvs.srv

from rocon_solution_msgs.msg import *
from rocon_solution_msgs.srv import *

class Composer(object):

    srv = {}
    srv_proxy = {}

    def __init__(self,cc,review_process):
        self.review_process = review_process

        self.careercenter = cc

        self.srv['review_applications'] = rospy.Service('~review_applications',std_srvs.srv.Empty,self.process_review)

    def process_review(self, msg):
        self.review_process(self.careercenter,msg)
        return std_srvs.srv.EmptyResponse()

        

