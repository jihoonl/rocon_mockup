#! /usr/bin/env python

import rospy
import random
import yaml
from rocon_solution_msgs.msg import *
from rocon_solution_msgs.srv import *

class Agent(object):

    pub = {}
    sub = {}
    srv_proxy = {}
    srv = {}
    data = {}

    current_job = None

    def __init__(self,filename):
      self.load_agent(filename)
      self.sub['job_announcement'] =  rospy.Subscriber('job_announcement',rocon_solution_msgs.msg.JobPostList,self.processJobAnnouncement)
      self.pub['apply_for_job'] = rospy.Publisher('apply_for_job',rocon_solution_msgs.msg.JobApplication)
      self.srv_proxy['post_jobs'] = rospy.ServiceProxy('post_jobs',rocon_solution_msgs.srv.AddJobs)
      self.srv['job_offer'] = rospy.Service('job_offer',rocon_solution_msgs.srv.JobOffer,self.processJobOffer)

    def load_agent(self,filename):
      with open(filename) as f:
        yaml_data = yaml.load(f)

      self.data = yaml_data

    def processJobAnnouncement(self,msg):
      job_names = None

      if current_job == None:
        job_names = [ j.job_name for j in msg.list]
      else:
        job_names = [j.job_names for j in msg.list if j.priority > current_job.priority]

      rospy.loginfo(str(job_names))
        
        

    def processJobOffer(self,req):
      return JobOfferResponse(True)

    def log(self,msg):
      rospy.loginfo(rospy.get_name() + " : " + str(msg))

    def spin(self):
        rospy.loginfo(str(self.data))
        rospy.spin()
