
#-*- coding: utf-8 -*-
from django.db.models import fields
from django.utils.translation import gettext_lazy as _
from django import forms


#PROTECTED REGION ID(phoneNumber) ENABLED START
class PhoneNumberField(fields.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 12
        super(PhoneNumberField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': forms.RegexField,
            'regex': '^\d{3}/\d{4}-\d{3}$',
            'max_length': self.max_length,
            'error_messages': {
                'invalid': _(u'Enter a valid phone number in the format xxx/xxxx-xxx.'),
            }
        }
        defaults.update(kwargs)
        return super(PhoneNumberField, self).formfield(**defaults)
#PROTECTED REGION END

	