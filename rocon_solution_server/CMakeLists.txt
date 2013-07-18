cmake_minimum_required(VERSION 2.8.3)
project(rocon_solution_server)

find_package(catkin REQUIRED COMPONENTS rospy message_generation std_msgs)

catkin_python_setup()

## Generate messages in the 'msg' folder
add_message_files(
  DIRECTORY msg
  FILES
  RoconService.msg
  RoconServiceList.msg
  RoconAgent.msg
  RoconAgentList.msg
)

## Generate services in the 'srv' folder
# add_service_files(
#   FILES
#   Service1.srv
#   Service2.srv
# )

# Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  std_msgs  # Or other packages containing msgs
)

catkin_package()
