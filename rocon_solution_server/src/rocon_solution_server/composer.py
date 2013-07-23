#! /usr/bin/env python
import rospy
import threading
import std_srvs.srv

from rocon_solution_msgs.msg import *
from rocon_solution_msgs.srv import *

class Composer(object):

    srv = {}
    srv_proxy = {}

    def __init__(self,cc):
        self.careercenter = cc

        self.srv['review_applications'] = rospy.Service('review_applications',std_srvs.srv.Empty,self.process_review)

    def process_review(self,req):
        
        self.log("Starting the application review process")
        jobs, applications = self.careercenter.get_job_applications()
        
        self.log("This is mockup. So assumes that orchestreation has been solved. Do hard coded job offer")
        self.log("CameraManager - camera")
        self.log("Cleaner       - kobuki")
        self.log("OrderReceiver - hydro")
        self.log("Database      - turtle")
        self.log(str(jobs))

        combination = {}
        combination['camera'] = 'CameraManager'
        combination['kobuki'] = 'Cleaner'
        combination['hydro']  = 'OrderReceiver'
        combination['turtle'] = 'Database'

        for agent, job_name in combination.items():
            srv_proxy = rospy.ServiceProxy(agent + "/job_offer",JobOffer)    

            job = [j for j in jobs if j.job_name == job_name]
            
            offer = JobOfferRequest(job[0])
            result = srv_proxy(offer)
            self.log(str(agent) + " has accepted Job")

        return std_srvs.srv.EmptyResponse()

    def log(self,msg):
        rospy.loginfo(rospy.get_name() + " : " + str(msg))
