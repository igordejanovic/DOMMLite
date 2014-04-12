# -*- coding: utf-8 -*-
# WARNING: This file is generated. DO NOT EDIT! 
# Generated on Mon Sep 28 16:46:47 CEST 2009 from ModelsGen templates

from django import forms
from datetime import date
from django.forms.util import ValidationError
from django.conf.urls.defaults import patterns
from django.db import models
from django.contrib import admin
from course_enrollment.models import Country,Student,Course
from course_enrollment.validators import *


class CountryAdminForm(forms.ModelForm):
	class Meta:
		model = Country

class CountryAdmin(admin.ModelAdmin):
	form = CountryAdminForm
	
	pass

class StudentAdminForm(forms.ModelForm):
	class Meta:
		model = Student
	
	def clean_lastName(self):
		lastName = self.cleaned_data['lastName']
		isOnlyLetters(lastName)		
		return lastName
	
	def clean_SUI(self):
		SUI = self.cleaned_data['SUI']
		isOnlyDigits(SUI)		
		mod(SUI,10)		
		return SUI
	
	def clean_email(self):
		email = self.cleaned_data['email']
		isValidEmail(email)		
		return email
	
	def clean_firstName(self):
		firstName = self.cleaned_data['firstName']
		isOnlyLetters(firstName)		
		return firstName
	
	def clean_discipline(self):
		discipline = self.cleaned_data['discipline']
		isOnlyLetters(discipline)		
		return discipline

class StudentAdmin(admin.ModelAdmin):
	form = StudentAdminForm
	fieldsets = (
        (None, {
        	
            'fields': ('SUI','firstName','lastName','admissionDate',)
        }),
      	
        ('Contact Information', {
            'classes': 'wide',
            'fields' : ('phone','email','postalAddress',)
        }),

        ('Prior education', {
        	'description' : u'Informations about student\'s prior education',            'classes': 'wide',
            'fields' : ('degree','discipline','institutionName','graduationDate',)
        })
        
    )
	radio_fields = {
				"degree" : admin.HORIZONTAL,
			
		
	}
	
	search_fields = ['lastName','SUI','email','postalAddress','firstName','institutionName','discipline']		
	pass

class CourseAdminForm(forms.ModelForm):
	class Meta:
		model = Course

class CourseAdmin(admin.ModelAdmin):
	form = CourseAdminForm
	
	pass

admin.site.register(Country, CountryAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)

