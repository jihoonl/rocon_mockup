#! /usr/bin/env python

import rospy
import yaml

class RoconSolution():

    services = {}

    def __init__(self):
        self.load_services()

    def load_services(self):
        filename = rospy.get_param('~services')

        with open(filename) as f:
            yaml_data = yaml.load(f)
  
        self.log(yaml_data)


    def spin(self):
        rospy.spin()
          

    def log(self,msg):
        rospy.loginfo("Rocon Solution : " + str(msg))

if __name__  == '__main__':

  rospy.init_node('solution')
  
  solution = RoconSolution()
  rospy.loginfo("Initialized")
  solution.spin()
