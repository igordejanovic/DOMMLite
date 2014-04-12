# coding: UTF-8
# This file is generated only once. Here you should define your service methods manualy.
# Service StudentService
# Generated on Fri Sep 25 16:39:14 CEST 2009 from ServicesSrc templates
# ------------------- Service  StudentService  ---------------------------

from course_enrollment_gen.services import student_service
from dommlite import service_registry

student_service_service = service_registry.get_service('student_service')

	

def enrollStudent(student, course, dateOfEnrollment):
	raise NotImplementedError('Operation StudentService.enrollStudent has not been implemented yet.')
	



core_service.get_function('enrollStudent')['function'] = enrollStudent
		


def getStudentsForCourse(course):
	raise NotImplementedError('Operation StudentService.getStudentsForCourse has not been implemented yet.')
	



core_service.get_function('getStudentsForCourse')['function'] = getStudentsForCourse
		
	