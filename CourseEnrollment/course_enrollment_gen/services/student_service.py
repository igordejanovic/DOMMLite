# coding: UTF-8
# WARRNING: This file is generated. DO NOT EDIT! 
# Service StudentService
# Generated on Mon Sep 28 16:46:47 CEST 2009 from Services templates

from dommlite import service_registry, Service

student_service_service = Service('course_enrollment','student_service','Student service')
 
	
def enrollStudent(student, course, dateOfEnrollment):
	raise NotImplementedError('Operation StudentService.enrollStudent has not been implemented yet.')
	



core_service.register_function(enrollStudent, 'enrollStudent', 'Enroll student to given course', None, '''''')
		

def getStudentsForCourse(course):
	raise NotImplementedError('Operation StudentService.getStudentsForCourse has not been implemented yet.')
	



core_service.register_function(getStudentsForCourse, 'getStudentsForCourse', 'Gets students enrolled to given course.', None, '''''')
		


service_registry.register_service('student_service', student_service_service)
	