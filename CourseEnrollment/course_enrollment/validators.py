# coding: UTF-8
# This file is generated only once. You shoud manualy define user validator implementations
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _

	
#PROTECTED REGION ID(isLessOrEquealThanRef) START
def isLessOrEquealThanRef(value, other_labels=None, other_fields=None):
	raise ValidationError(_(u'Validator "isLessOrEquealThanRef" is applied to this field but is not defined yet.'))
#PROTECTED REGION END

#PROTECTED REGION ID(isOnlyLetters) START
def isOnlyLetters(value, ):
	raise ValidationError(_(u'Validator "isOnlyLetters" is applied to this field but is not defined yet.'))
#PROTECTED REGION END

#PROTECTED REGION ID(isBetweenRefsInclusive) START
def isBetweenRefsInclusive(value, other_labels=None, other_fields=None):
	raise ValidationError(_(u'Validator "isBetweenRefsInclusive" is applied to this field but is not defined yet.'))
#PROTECTED REGION END

#PROTECTED REGION ID(isCommaSeparatedEmailList) START
def isCommaSeparatedEmailList(value, ):
	raise ValidationError(_(u'Validator "isCommaSeparatedEmailList" is applied to this field but is not defined yet.'))
#PROTECTED REGION END

#PROTECTED REGION ID(isWellFormedXml) START
def isWellFormedXml(value, ):
	raise ValidationError(_(u'Validator "isWellFormedXml" is applied to this field but is not defined yet.'))
#PROTECTED REGION END

#PROTECTED REGION ID(isValidEmail) START
def isValidEmail(value, ):
	raise ValidationError(_(u'Validator "isValidEmail" is applied to this field but is not defined yet.'))
#PROTECTED REGION END

#PROTECTED REGION ID(isValidURL) START
def isValidURL(value, ):
	raise ValidationError(_(u'Validator "isValidURL" is applied to this field but is not defined yet.'))
#PROTECTED REGION END

#PROTECTED REGION ID(isOnlyDigits) ENABLED START
def isOnlyDigits(value, ):
#	raise ValidationError('Validator "isOnlyDigits" is applied to this field but is not defined yet.')
    try:
    	int(value)
    except ValueError:
    	raise ValidationError(_(u'Only digits are allowed in this field.'))
#PROTECTED REGION END

#PROTECTED REGION ID(isExistingURL) START
def isExistingURL(value, ):
	raise ValidationError(_(u'Validator "isExistingURL" is applied to this field but is not defined yet.'))
#PROTECTED REGION END

#PROTECTED REGION ID(notEmptyIfRefsNotEmpty) START
def notEmptyIfRefsNotEmpty(value, other_labels=None, other_fields=None):
	raise ValidationError(_(u'Validator "notEmptyIfRefsNotEmpty" is applied to this field but is not defined yet.'))
#PROTECTED REGION END

#PROTECTED REGION ID(isValidImageURL) START
def isValidImageURL(value, ):
	raise ValidationError(_(u'Validator "isValidImageURL" is applied to this field but is not defined yet.'))
#PROTECTED REGION END

#PROTECTED REGION ID(matchesRegularExpression) START
def matchesRegularExpression(value, param0str):
	raise ValidationError(_(u'Validator "matchesRegularExpression" is applied to this field but is not defined yet.'))
#PROTECTED REGION END

#PROTECTED REGION ID(isGreaterThanRef) START
def isGreaterThanRef(value, other_labels=None, other_fields=None):
	raise ValidationError(_(u'Validator "isGreaterThanRef" is applied to this field but is not defined yet.'))
#PROTECTED REGION END

#PROTECTED REGION ID(isLowerCase) START
def isLowerCase(value, ):
	raise ValidationError(_(u'Validator "isLowerCase" is applied to this field but is not defined yet.'))
#PROTECTED REGION END

#PROTECTED REGION ID(emptyIfRefsEmpty) START
def emptyIfRefsEmpty(value, other_labels=None, other_fields=None):
	raise ValidationError(_(u'Validator "emptyIfRefsEmpty" is applied to this field but is not defined yet.'))
#PROTECTED REGION END

#PROTECTED REGION ID(isUpperCase) START
def isUpperCase(value, ):
	raise ValidationError(_(u'Validator "isUpperCase" is applied to this field but is not defined yet.'))
#PROTECTED REGION END

#PROTECTED REGION ID(isLessThanInt) START
def isLessThanInt(value, param0_int):
	raise ValidationError(_(u'Validator "isLessThanInt" is applied to this field but is not defined yet.'))
#PROTECTED REGION END

#PROTECTED REGION ID(mod) ENABLED START
def mod(value, modulus):
#	raise ValidationError('Validator "mod" is applied to this field but is not defined yet.')
    _sum = 0
    alt = False
    for d in reversed(str(value)):
    	d = int(d)
        if alt:
            d *= 2
            if d > modulus-1:
                d -= modulus-1
        _sum += d
        alt = not alt
    if not (_sum % modulus) == 0:
    	raise ValidationError('Number does not pass mod(%d) test.' % modulus)
#PROTECTED REGION END

#PROTECTED REGION ID(isGreaterOrEqualThanInt) START
def isGreaterOrEqualThanInt(value, param0_int):
	raise ValidationError(_(u'Validator "isGreaterOrEqualThanInt" is applied to this field but is not defined yet.'))
#PROTECTED REGION END

#PROTECTED REGION ID(isGreaterThanInt) START
def isGreaterThanInt(value, param0_int):
	raise ValidationError(_(u'Validator "isGreaterThanInt" is applied to this field but is not defined yet.'))
#PROTECTED REGION END

#PROTECTED REGION ID(emptyIfRefsNotEmpty) START
def emptyIfRefsNotEmpty(value, other_labels=None, other_fields=None):
	raise ValidationError(_(u'Validator "emptyIfRefsNotEmpty" is applied to this field but is not defined yet.'))
#PROTECTED REGION END

#PROTECTED REGION ID(isLessOrEqualThanInt) START
def isLessOrEqualThanInt(value, param0_int):
	raise ValidationError(_(u'Validator "isLessOrEqualThanInt" is applied to this field but is not defined yet.'))
#PROTECTED REGION END

#PROTECTED REGION ID(isBetweenIntsExclusive) START
def isBetweenIntsExclusive(value, param0_int, param1_int):
	raise ValidationError(_(u'Validator "isBetweenIntsExclusive" is applied to this field but is not defined yet.'))
#PROTECTED REGION END

#PROTECTED REGION ID(isCommaSeparatedIntegerList) START
def isCommaSeparatedIntegerList(value, ):
	raise ValidationError(_(u'Validator "isCommaSeparatedIntegerList" is applied to this field but is not defined yet.'))
#PROTECTED REGION END

#PROTECTED REGION ID(isBetweenRefsExclusive) START
def isBetweenRefsExclusive(value, other_labels=None, other_fields=None):
	raise ValidationError(_(u'Validator "isBetweenRefsExclusive" is applied to this field but is not defined yet.'))
#PROTECTED REGION END

#PROTECTED REGION ID(isWellFormedXmlFragment) START
def isWellFormedXmlFragment(value, ):
	raise ValidationError(_(u'Validator "isWellFormedXmlFragment" is applied to this field but is not defined yet.'))
#PROTECTED REGION END

#PROTECTED REGION ID(isNotOnlyDigits) START
def isNotOnlyDigits(value, ):
	raise ValidationError(_(u'Validator "isNotOnlyDigits" is applied to this field but is not defined yet.'))
#PROTECTED REGION END

#PROTECTED REGION ID(notEmptyIfRefsEmpty) START
def notEmptyIfRefsEmpty(value, other_labels=None, other_fields=None):
	raise ValidationError(_(u'Validator "notEmptyIfRefsEmpty" is applied to this field but is not defined yet.'))
#PROTECTED REGION END

#PROTECTED REGION ID(isAlphaNumeric) START
def isAlphaNumeric(value, ):
	raise ValidationError(_(u'Validator "isAlphaNumeric" is applied to this field but is not defined yet.'))
#PROTECTED REGION END

#PROTECTED REGION ID(isLessThanRef) START
def isLessThanRef(value, other_labels=None, other_fields=None):
	raise ValidationError(_(u'Validator "isLessThanRef" is applied to this field but is not defined yet.'))
#PROTECTED REGION END

#PROTECTED REGION ID(isValidImage) START
def isValidImage(value, ):
	raise ValidationError(_(u'Validator "isValidImage" is applied to this field but is not defined yet.'))
#PROTECTED REGION END

#PROTECTED REGION ID(isValidHTML) START
def isValidHTML(value, ):
	raise ValidationError(_(u'Validator "isValidHTML" is applied to this field but is not defined yet.'))
#PROTECTED REGION END

#PROTECTED REGION ID(isGreaterOrEqualThanRef) START
def isGreaterOrEqualThanRef(value, other_labels=None, other_fields=None):
	raise ValidationError(_(u'Validator "isGreaterOrEqualThanRef" is applied to this field but is not defined yet.'))
#PROTECTED REGION END

#PROTECTED REGION ID(isBetweenIntsInclusive) START
def isBetweenIntsInclusive(value, param0_int, param1_int):
	raise ValidationError(_(u'Validator "isBetweenIntsInclusive" is applied to this field but is not defined yet.'))
#PROTECTED REGION END

	