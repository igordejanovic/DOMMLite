# coding: UTF-8
# WARRNING: This file is generated. DO NOT EDIT! 
# Generated on Mon Sep 28 16:46:47 CEST 2009 from ModelsGenBase templates

from django.db import models
from course_enrollment import custom_fields
	
	
DEGREE_CHOICE = (
	('N','None'),
	('B','Bachelor'),
	('M','Master'),
	('P','PhD'),
)

	
class Student(models.Model):
	# ----------------------------------- Identifier -----------------------------------
	SUI = models.CharField(verbose_name=u"Student ID", unique=True,max_length=11)
	# ----------------------------------------------------------------------------------
	
	firstName = models.CharField(verbose_name=u"First Name", blank=True,max_length=20)
	lastName = models.CharField(verbose_name=u"Last Name", blank=True,max_length=30)
	admissionDate = models.DateField(verbose_name=u"Date of admission", null=True, blank=True)
	
	# -----------------------------------    Compartment priorEducation    -----------------------------------
	degree = models.CharField(verbose_name=u"Degree level",
            max_length=1, 
            choices=DEGREE_CHOICE,
            db_index=True,
            default=DEGREE_CHOICE[0][0], null=True, blank=True
	)
	discipline = models.CharField(verbose_name=u"Discipline", blank=True,max_length=30)
	institutionName = models.CharField(verbose_name=u"Name of the institution", blank=True,max_length=50)
	graduationDate = models.DateField(verbose_name=u"Graduation date", null=True, blank=True)

	# -----------------------------------    Compartment contactInfo    -----------------------------------
	phone = custom_fields.PhoneNumberField(verbose_name=u"Phone number", null=True, blank=True)
	email = models.CharField(verbose_name=u"E-mail", blank=True,max_length=30)
	postalAddress = models.CharField(verbose_name=u"Postal address", blank=True,max_length=50)
	
	def __unicode__(self):
		return u"%s %s" % (self.firstName,self.lastName,)
    
	class Meta:
		verbose_name=u"Student"


class Country(models.Model):
	# ----------------------------------- Identifier -----------------------------------
	code = models.IntegerField(verbose_name=u"Country code", unique=True)
	# ----------------------------------------------------------------------------------
	
	
    
	class Meta:
		verbose_name=u"Country"


class Course(models.Model):
	# ----------------------------------- Identifier -----------------------------------
	code = models.IntegerField(verbose_name=u"Course code", unique=True)
	# ----------------------------------------------------------------------------------
	
	
    
	class Meta:
		verbose_name=u"Course"


	
	
	
	
	
	
	
	
	

	
	

	