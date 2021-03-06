#! /usr/bin/env python

import rospy
import random
import yaml
from threading import Lock
from rocon_solution_msgs.msg import *
from rocon_solution_msgs.srv import *

class Agent(object):

    pub = {}
    sub = {}
    srv_proxy = {}
    srv = {}
    data = {}
    applied_services= []
    lock = None

    current_job = None

    def __init__(self,filename):
        self.load_agent(filename)
        self.sub['job_announcement'] =    rospy.Subscriber('job_announcement',rocon_solution_msgs.msg.JobPostList,self.processJobAnnouncement)
#        self.pub['apply_for_job'] = rospy.Publisher('apply_for_job',rocon_solution_msgs.msg.JobApplication)
#        self.srv_proxy['post_jobs'] = rospy.ServiceProxy('post_jobs',rocon_solution_msgs.srv.AddJobs)
        self.srv['job_offer'] = rospy.Service('~job_offer',rocon_solution_msgs.srv.JobOffer,self.processJobOffer)

        self.lock = Lock()

    def load_agent(self,filename):
        with open(filename) as f:
            yaml_data = yaml.load(f)

        self.data = yaml_data
        self.log(self.data)

    def processJobAnnouncement(self,msg):
        job_names = [ j.job_name for j in msg.list]
        self.log("Received available job list from " + msg.service_node + " : " + str(job_names))
        job_names = None

        #  If the agent has a job already..
        if self.current_job and not self.current_job.interruptible:
            self.log("The current job["+str(self.current_job.job_name)+"] : is not interruptible")
            return

        self.log("Check what jobs I can do...")
        filtered_list, filtered_list_job_name = self.job_compatibility_test(msg.list)
        self.log("I can do..." + str(filtered_list_job_name))

        if self.current_job:
            self.log("Check the job priorities..if available job is higher than current job apply for the higher priority job")
            filtered_list = [j.job_name for j in filtered_list if j.priority > self.current_job.priority]

        job_names = [ j.job_name for j in filtered_list]
        self.log("Applying for jobs..." + str(job_names))

        if len(filtered_list) > 0:
            self.apply_for_jobs(filtered_list,msg.service_node)
            self.log("Applied to " + str(msg.service_node))
            job_name = [j.job_name for j in filtered_list]
            self.applied_services.append(msg.service_node)

    def processJobOffer(self,req):
        self.lock.acquire()

        self.log("Recieved " + str(req.job.job_name) + " offer")

        if self.current_job:
            if not(req.job.service_node in self.applied_services):
                self.log("    It is not a service where I submitted applications. Declining..")

                return JobOfferResponse(False) 

            if req.job.priority < self.current_job.priority:
                self.log("    Current job has higher prirority. (Offered Job[" + str(req.job.priority) + "] < CurrentJob["+str(self.current_job.priority) +"])")
                self.log("    Decline the offer")
                return JobOfferResponse(False) 
            self.log("Accepting " + str(req.job.job_name) + " from " + str(req.job.service_node))
            self.log("The new job has higher priority")
        else:
            self.log("Accepting " + str(req.job.job_name) + " from " + str(req.job.service_node))
        self.current_job = req.job
        self.lock.release()
        return JobOfferResponse(True)

    def job_compatibility_test(self,job_list):
        self.log("My Condition.. : " + str(self.data['condition']))

        new_job_list = []
        
        for j in job_list:
            flag = True
            self.log("    "+ str(j.job_name) + " conditions : " + str(j.condition))
            self.log("    "+ str(j.job_name) + "            : " + str(j.condition_value))
            for i in range(len(j.condition)): 
                if j.condition[i] not in self.data['condition']:
                    flag = False
                    break
                if j.condition_value[i] < self.data['condition'][j.condition[i]]:
                    flag = False
            if flag:
                new_job_list.append(j)

        names = [ j.job_name for j in new_job_list]

        return new_job_list, names
             

    def apply_for_jobs(self,jobs,service_node):
        ja = rocon_solution_msgs.msg.JobApplication()
        ja.job_name = [j.job_name for j in jobs]
        ja.agent_name = rospy.get_name()

        if self.current_job:
            ja.current_job = self.current_job 

        pub = rospy.Publisher(service_node + '/apply_for_job',rocon_solution_msgs.msg.JobApplication)
        rospy.sleep(1)

        pub.publish(ja)

    def log(self,msg):
        rospy.loginfo(rospy.get_name() + " : " + str(msg))

    def spin(self):
        rospy.loginfo(str(self.data))
        rospy.spin()
