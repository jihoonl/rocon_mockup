cmake_minimum_required(VERSION 2.8.3)
project(rocon_agent)

find_package(catkin REQUIRED COMPONENTS rocon_solution_msgs rospy)

catkin_python_setup()
catkin_package()
