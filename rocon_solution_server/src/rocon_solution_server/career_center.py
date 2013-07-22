#! /usr/bin/env python
import rospy

from rocon_solution_msgs.msg import *
from rocon_solution_msgs.srv import *

class CareerCenter(object):

    pub = {}
    sub = {}
    srv = {}

    jobs = []

    def __init__(self):
        self.srv['post_jobs'] = rospy.Service('post_jobs',AddJobs,self.processJobPosting)
        self.pub['job_announcement'] = rospy.Publisher('job_announcement',JobPostList, latch=True)

    def processJobPosting(self,srv):
        rospy.loginfo(str(srv))
        for j in srv.posts:
            self.jobs.append(j)

        self.announce() 
        
        return AddJobsResponse(True)

    def announce(self):
        self.pub['job_announcement'].publish(self.jobs)
        
        
    def log(self,msg):
        rospy.loginfo(rospy.get_name() + ' : ' + str(msg))


