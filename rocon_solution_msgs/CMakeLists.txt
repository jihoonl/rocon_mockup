cmake_minimum_required(VERSION 2.8.3)
project(rocon_solution_msgs)

find_package(catkin REQUIRED COMPONENTS message_generation std_msgs)

## Generate messages in the 'msg' folder
add_message_files(
  DIRECTORY msg
  FILES
  RoconService.msg
  RoconServiceList.msg
  RoconAgent.msg
  RoconAgentList.msg
  RoconJob.msg
  RoconJobList.msg
  
  JobApplication.msg
  JobPost.msg
  JobPostList.msg
)

## Generate services in the 'srv' folder
add_service_files(
  DIRECTORY srv
  FILES
  AddService.srv
  AddJobs.srv
)

# Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  std_msgs  # Or other packages containing msgs
)

catkin_package()
