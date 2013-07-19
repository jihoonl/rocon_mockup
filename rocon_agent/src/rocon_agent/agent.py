#! /usr/bin/env python

import rospy
import random
import yaml
from rocon_solution_msgs.msg import *

class Agent(object):

    pub = {}
    srv = {}
    data = {}

    def __init__(self,filename):

      self.load_agent(filename)
      self.sub['jobposting'] =  rospy.Subscriber('jobposting',rocon_solution_msgs.msg.RoconJobList,self.processJobPosting)
      self.pub['apply_for_job'] = rospy.Publisher('apply_for_job',rocon_solution_msgs.JobApplication)

    def load_agent(self,filename):
      with open(filename) as f:
        yaml_data = yaml.load(f)

      self.data = yaml_data

    def processJobPosting(self,msg):
      self.log(str(msg))

    def log(self,msg):
      rospy.loginfo(rospy.get_name() + " : " + str(msg))

    def spin(self):
        rospy.loginfo(str(self.data))
        rospy.spin()
