#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import json
import urllib2

data = {"plateno":"苏A7NJ88","vehicleid":"a4aefb2e-e02d-4ca2-8691-c35f44af5b81","devicetype":0,"ntspheader":{"apikey":"bda11d91-7ade-4da1-855d-24adfe39d174","corpid":"1001","errcode":0,"mdinfo":"null|samsung SM-G9006V|Android6.0.1","productid":"1002","sessionid":"5e93e55d-b4dc-4f4a-9fe7-b890984764c1","version":"5.7.7","zjid":"30166513"},"endtime":"2017-04-17 23:59","starttime":"2017-04-16 00:00"}
url = 'http://appapi.yesway.cn:9955/dx/trip/gettrackbyduration'

request = urllib2.Request(url)
request.add_header('Content-Type', 'application/json; charset=utf-8')

response = urllib2.urlopen(request, json.dumps(data))

result = json.loads(response.read().decode('utf-8'))

from pprint import pprint
track = result['track']['track']
sp = track.split("|")
length = len(sp)
for i in xrange(0,length/2):
    print sp[i*2] + " "+sp[i*2+1]