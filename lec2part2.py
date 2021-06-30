#!/usr/bin/python2


##############################DATA TYPES OF PYTHON#################################


##Strings
##Numbers
##List
##Dictionaires
##Tuples
##Boolean

##############################String################################

#multiple ways to define a string


name = "method1"
print name
name ='method2'
print name

name = 'method1\nmethod2'
###raw string

print "Demo of a Raw string in python"
name = r"method1\nmethod2"
print name


##multiple lines defined via string 



name = """
This is a multiple line commment which covers 3 different line from now and you cansee the magic

1.\n
12.\n
123.\n
Enjoy you stay
"""
print name



###python also support uncode string

name = u'cars'
print name

##converting a  unicode string to a normal string 

str(name)
print "str(name)"
print name


###converting a a normal string to unicode

print """unicode("carswithanitro")"""

unicode("appleisfast")


###USED FOR WEB_APPLICATION


####STRING OPERATIONS

###IMMUTABLE OBJECTS


name = "vivek"

print name[0]

###GArabage collection is automatically freed up oonce the  variable is no longer required



###Repating a sequence


print """ "a"*20 """

print  "A"*20
