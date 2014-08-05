#!/usr/bin/python

import urllib2
import json 
import sys 

sys.argv.pop(0)
inputs = sys.argv
first_res_list = [] 
for word in inputs :
    respons = urllib2.urlopen("http://www.google.com/inputtools/request?"+
            "text=" + word + 
            "&ime=transliteration_en_ar"+
            "&num=5"+
            "&cp=0"+
            "&cs=0"+
            "&ie=utf-8"+
            "&oe=utf-8"+
            "&app=jsapi"+
            "&uv").read()
    json_respons = json.loads(respons)
    possibilities = json_respons[1][0][1] # nested lists
    first_res_list.append(possibilities[0])
    print "results for the word \"" + word + "\" are :\n" 
    for result in possibilities :
        print result + "\n"

# print the most correct results 
print "the most correct result for transliteration is :\n"
for res in first_res_list :
    print res, 

