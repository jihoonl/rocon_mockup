#! /usr/bin/env python

import rospy
from rocon_solution_msgs.srv import *


rospy.init_node('add_srv')

filename = rospy.get_param('~filename')
srv = rospy.ServiceProxy('add_a_service',AddService)

r = srv(filename)
rospy.loginfo(str(r))
