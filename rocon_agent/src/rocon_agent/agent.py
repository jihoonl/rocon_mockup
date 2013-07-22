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
      self.log("Received available job list")
      job_names = None

      self.log("Check whats job I can do...")
      self.job_compatibility_test(msg.list)

      self.log("Check the job priorities..if available job is higher than current job apply for the higher priority job")
      if self.current_job == None:
        job_names = [ j.job_name for j in msg.list]
      else:
        job_names = [j.job_names for j in msg.list if j.priority > self.current_job.priority]

      self.log("Appling for jobs..." + str(job_names))

      self.apply_for_jobs(job_names)


    def processJobOffer(self,req):
      return JobOfferResponse(True)

    def job_compatibility_test(self,job_list):
      self.log("I'm mockup. I can do everything...")

    def apply_for_jobs(self,job_names):
      ja = rocon_solution_msgs.msg.JobApplication()
      ja.job_name = job_names
      ja.agent_name = rospy.get_name()

      if self.current_job:
          ja.current_job = self.current_job 
      

      self.pub['apply_for_job'].publish(ja)

    def log(self,msg):
      rospy.loginfo(rospy.get_name() + " : " + str(msg))

    def spin(self):
        rospy.loginfo(str(self.data))
        rospy.spin()
