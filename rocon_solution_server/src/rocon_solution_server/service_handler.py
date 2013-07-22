#! /usr/bin/env python
import rospy
import yaml
from rocon_solution_msgs.msg import *
from rocon_solution_msgs.srv import *

class ServiceHandler(object):

    pub = {}
    sub = {}
    srv = {}
    srv_proxy = {}
    rocon_service = []
    id_inc = 0

    def __init__(self):
        self.srv_proxy['post_jobs'] = rospy.ServiceProxy('post_jobs',AddJobs)
        self.srv['add_a_service'] = rospy.Service('add_a_service',AddService,self.processAddService)

    def processAddService(self,req):
        service = self.load_service_from_file(req.filename)


        self.rocon_service.append(service)
        self.post_jobs(service)

        return AddServiceResponse(True)

    def load_service_from_file(self,filename):
        with open(filename) as f: 
            yaml_data = yaml.load(f)

        return yaml_data

    def post_jobs(self,service):
        jp = AddJobsRequest()
        for r in service['roles']:
            condition = [str(n) + ' : ' + str(c) for n,c in r['condition'].items()]
            job_post = JobPost(service['name'],r['name'],condition,service['priority'],self.id_inc)
            self.id_inc = self.id_inc + 1
            jp.posts.append(job_post)
        self.srv_proxy['post_jobs'](jp)

    def log(self,msg):
        rospy.loginfo(rospy.get_name() + ' : ' + str(msg))
