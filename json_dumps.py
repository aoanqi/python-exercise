# -*- coding: utf-8 -*-
import json

demoDictList = [{"yearMonth": {"month": {"string": "November", "value": "11"}, "year": {"string": "2012", "value": "2012"}}, "reservedMonthList": ["2", "3", "8", "9", "10", "11", "12", "13", "17", "18", "19", "20", "21", "22", "23"]}, {"yearMonth": {"month": {"string": "December", "value": "12"}, "year": {"string": "2012", "value": "2012"}}, "reservedMonthList": ["7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "21", "22", "23", "24", "25", "26", "27", "28", "30", "31"]}]

jsonDumpsIndentStr = json.dumps(demoDictList);
print "jsonDumpsIndentStr=",jsonDumpsIndentStr;