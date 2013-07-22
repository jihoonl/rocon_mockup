#! /usr/bin/env python
import rospy

from rocon_solution_msgs.msg import *
from rocon_solution_msgs.srv import *

class CareerCenter(object):

    pub = {}
    sub = {}
    srv = {}

    jobs = []
    applications = {}

    def __init__(self,applications):
        self.applications = applications

        self.pub['job_announcement'] = rospy.Publisher('job_announcement',JobPostList, latch=True)
        self.sub['apply_for_job'] = rospy.Subscriber('apply_for_job',JobApplication,self.processJobApplication)
        self.srv['post_jobs'] = rospy.Service('post_jobs',AddJobs,self.processJobPosting)

    def processJobPosting(self,srv):
        for j in srv.posts:
            self.jobs.append(j)

        self.announce() 
        
        return AddJobsResponse(True)

    def announce(self):
        self.pub['job_announcement'].publish(self.jobs)

    def processJobApplication(self,msg):
        
        for job in msg.job_name:
            if job not in self.applications:
                self.applications[job] = {}

            self.applications[job][msg.agent_name] = msg

        self.print_application()
        
    def log(self,msg):
        rospy.loginfo(rospy.get_name() + ' : ' + str(msg))


    def print_application(self):


        print "-----------------------------------------------------------"
        for job in self.applications:
            print str(job) + " : "

            for agent in self.applications[job].keys():
                print "\t" + str(agent)
        print "-----------------------------------------------------------"
            


