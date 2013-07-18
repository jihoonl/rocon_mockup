#! /usr/bin/env python

import rospy 
from rocon_solution_server import SolutionMockup

if __name__ == '__main__':

    rospy.init_node('solution_mockup')
    
    mockup = SolutionMockup()
    rospy.loginfo('Initialized')
    mockup.spin()
    rospy.loginfo('Bye Bye')
