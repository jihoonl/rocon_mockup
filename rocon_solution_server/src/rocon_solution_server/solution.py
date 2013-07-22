#! /usr/bin/env python
import rospy
import random
from rocon_solution_msgs.msg import *
from .service_handler import *
from .career_center import *
#from .composer import *
class Solution():
  
    service_handler = None
    career_center   = None
    composer        = None

    applications    = {}

    def __init__(self):
        self.service_handler = ServiceHandler()
        self.rocon_careercenter = CareerCenter(self.applications)
#    self.composer = Composer(applications)
        self.log("Hola")

    def log(self,msg):
        rospy.loginfo(rospy.get_name() + ' : ' + str(msg))

    def spin(self):
        rospy.spin()
