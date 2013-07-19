#! /usr/bin/env python

import rospy
import rocon_agent

if __name__  == '__main__':

  rospy.init_node('agent')
  
  filename = rospy.get_param('~agent_spec')

  agent = rocon_agent.Agent(filename)
  rospy.loginfo("Initialized")
  agent.spin()
  rospy.loginfo("Bye Bye")


