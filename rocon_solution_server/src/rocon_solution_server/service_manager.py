#! /usr/bin/env python
import rospy
import random
from rocon_solution_msgs.msg import *
from .service_handler import *
from .career_center import *
from .composer import *
class ServiceRecruiter():
  
    service_handler = None
    career_center   = None
    composer        = None

    applications    = {}

    def __init__(self,filename,review_process):
        self.rocon_careercenter = CareerCenter(self.applications)
        self.service_handler = ServiceHandler(filename)
        self.composer = Composer(self.rocon_careercenter,review_process)
#        self.log("Hola")

    def log(self,msg):
        rospy.loginfo(rospy.get_name() + ' : ' + str(msg))

    def spin(self):
        rospy.spin()
