# -*- coding: utf-8 -*-
import json

my_name = 'MadCarmelo'
my_age = 24
my_height = 174 #CM
my_weight = 68 #kg
my_eyes = 'dark'
my_teeth = 'white'
my_hair = 'dark'

print "Let's talk about %s." %my_name
print "He's %d cm tall." %my_height
print "He's %d kg heavy." %my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." %my_teeth

#this line is tricky, try to get it exactly right.
print "If I add %d, %d, and %d I get %d." %(my_age, my_height, my_weight, my_age + my_height + my_weight)

demoDictList = [{"yearMonth": {"month": {"string": "November", "value": "11"}, "year": {"string": "2012", "value": "2012"}}, "reservedMonthList": ["2", "3", "8", "9", "10", "11", "12", "13", "17", "18", "19", "20", "21", "22", "23"]}, {"yearMonth": {"month": {"string": "December", "value": "12"}, "year": {"string": "2012", "value": "2012"}}, "reservedMonthList": ["7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "21", "22", "23", "24", "25", "26", "27", "28", "30", "31"]}]
jsonDumpsIndentStr = json.dumps(demoDictList, indent = 1)
print "jsonDumpsIndentStr=", jsonDumpsIndentStr