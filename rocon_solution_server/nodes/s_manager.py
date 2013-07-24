#! /usr/bin/env python

import rospy 
import std_srvs.srv
from rocon_solution_server import ServiceRecruiter
from rocon_solution_server import brain
from rocon_solution_msgs.srv import *

def process_review(careercenter,req):
    
    log("Starting the application review process")
    jobs, applications = careercenter.get_job_applications()
    
    reviewer = rospy.get_param("~reviewer")
    review = getattr(brain,reviewer)
    
    combination = review(jobs,applications)
    log(combination)
                                                                                                        
    for agent, job_name in combination.items():
        srv_proxy = rospy.ServiceProxy(agent + "/job_offer",JobOffer)    
                                                                                                        
        job = [j for j in jobs if j.job_name == job_name]
        
        offer = JobOfferRequest(job[0])
        result = srv_proxy(offer)
        r = "accepted" if result else "declined"
        log(str(agent) + " has " + str(r))
                                                                                                        

def log(msg):

    rospy.loginfo(rospy.get_name() + " : " + str(msg))

if __name__ == '__main__':

    rospy.init_node('service_recruiter')
    
    filename = rospy.get_param('~service')
    mockup = ServiceRecruiter(filename,process_review)
    rospy.loginfo('Initialized')
    mockup.spin()
    rospy.loginfo('Bye Bye')
