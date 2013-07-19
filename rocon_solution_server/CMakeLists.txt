cmake_minimum_required(VERSION 2.8.3)
project(rocon_solution_server)

find_package(catkin REQUIRED COMPONENTS rospy rocon_solution_msgs)

catkin_python_setup()

catkin_package()
