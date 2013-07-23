#! /usr/bin/env python

import rospy
import std_srvs.srv as std_srv
import geometry_msgs.msg

class RoconAgent():

    clean_flip = False 
    delivery_flag = False

    def __init__(self):
        job_srv = rospy.Service('job_notification',std_srv.Empty,self.processJob)
        self.move_base_pub = rospy.Publisher('/move_base_simple/goal',geometry_msgs.msg.PoseStamped)

        self.buildPose()



    def buildPose(self):
        go = geometry_msgs.msg.PoseStamped()
        go.header.frame_id = "map"
        go.pose.position.x=0.10198
        go.pose.position.y=2.10198
        go.pose.orientation.w = 1
        self.go = go

        back = geometry_msgs.msg.PoseStamped()
        back.header.frame_id = "map"
        back.pose.position.x=0.049
        back.pose.position.y=0.036
        back.pose.orientation.w = 1
        self.back = back

        delivery_pose = geometry_msgs.msg.PoseStamped()
        delivery_pose.header.frame_id = "map"
        delivery_pose.pose.position.x=8.536
        delivery_pose.pose.position.y=6.783
        delivery_pose.pose.orientation.w = 1
        self.delivery_pose = delivery_pose

        pickup_pose = geometry_msgs.msg.PoseStamped()
        pickup_pose.header.frame_id = "map"
        pickup_pose.pose.position.x=6.819
        pickup_pose.pose.position.y=1.515
        pickup_pose.pose.orientation.w = 1
        self.pickup_pose = pickup_pose
         


    def spin(self):
        self.log("I'm Kobuki agent mockup.")
        self.log("Assumes that I have received cleaning job already...")
        self.log("Cleaning service job is interruptible by higher priority jobs...")
        self.log("Let's start....")
        self.log("In clean mode...")

        while not rospy.is_shutdown():
            if self.delivery_flag:
                self.delivery()
                self.log("Delivery is finished.. return to cleaning job..")
                self.delivery_flag = False

            if self.clean_flip:
                self.publish(self.back)
                self.clean_flip = False
            else:
                self.publish(self.go)
                self.clean_flip = True
            self.log("Clean...")
            rospy.sleep(7)

    def publish(self,pose):
        pose.header.stamp = rospy.Time.now()
        self.move_base_pub.publish(pose)
                

    def processJob(self,srv):
        self.log("Received job_notification. Delivery Job has higher priority...")
        self.log("Send Job application to solution...")
        self.log("Received Delivery job offer")
        self.log("Starts delivery...")

        self.delivery_flag = True
        return std_srv.EmptyResponse()

    def delivery(self):
        self.log("Going to pickup Pose..")
        self.publish(self.pickup_pose)
        rospy.sleep(25)
        self.log("Going to delivery pose..")
        self.publish(self.delivery_pose)
        rospy.sleep(15)
        self.log("Delivery is done. Return to initial pose ..")
        self.publish(self.back)
        rospy.sleep(30)
        
    def log(self,msg):
        rospy.loginfo("Agent : " + str(msg))
        rospy.sleep(2)



if __name__  == '__main__':

  rospy.init_node('agent')

  agent = RoconAgent()
  agent.spin()

  
