#!/usr/bin/python2
#Varibles,Object,References


name = "vivek" # we dont need to define the type of variable to name(such as int name)

print name
print "the value of name is:" + name

loca=str (hex(id(name)))

print "The location of name = vivek is :" + loca
#print hex(id(name))

print "USing variable.__repr__"
print name.__repr__

###########################################################################################
print "\n\n\n\n"
name = 100
name = str(name)
print "The location of name = 100 is :" 
print hex(id(name))
print "the value of name is:" + name
print "using the variable.__repr__"
print name.__repr__

# summary
#name is the variable and 100 is the object so the object is assigned a type and not the name
#this will print vivek once and 100 on the second line
#To find the exact memory location where the  object is stored
#use hex(id(var)) or var.repr aslo id(name)



