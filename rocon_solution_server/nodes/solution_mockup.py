#! /usr/bin/env python

import rospy 
from rocon_solution_server import Solution

if __name__ == '__main__':

    rospy.init_node('solution_mockup')
    
    mockup = Solution()
    rospy.loginfo('Initialized')
    mockup.spin()
    rospy.loginfo('Bye Bye')
