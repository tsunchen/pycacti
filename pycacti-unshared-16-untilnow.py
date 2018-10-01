#! /usr/bin/env python
# coding=utf-8
# get image manjisweet()

import time,datetime,socket,urllib
import http.cookiejar
import pycactisetting, pycactisetting_unshared


#import numpy as np
#import cv2, matplotlib.pyplot as plt

#threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days = 10)) 
#print datetime.datetime.now()
#print datetime.timedelta(days = 10)




def range_date():
	global dbegin
	global dend
	oneDayAgo = (datetime.datetime.now() - datetime.timedelta(days = 1))
	print (oneDayAgo)

	oneDayAgootherStyleTime = oneDayAgo.strftime("%Y-%m-%d %H:%M:%S") 
	print (oneDayAgootherStyleTime)

	format_otherStyleTime = "%s 00:00:00" % oneDayAgootherStyleTime.split()[0]
	print (format_otherStyleTime)
	dbegin=time.mktime(time.strptime(format_otherStyleTime,'%Y-%m-%d %H:%M:%S')) # - 28800

	format_otherStyleTime2 = "%s %s:%s:00" % (
	oneDayAgootherStyleTime.split()[0], oneDayAgootherStyleTime.split()[1].split(':')[0],
	oneDayAgootherStyleTime.split()[1].split(':')[1])
	dbegin = time.mktime(time.strptime(format_otherStyleTime2, '%Y-%m-%d %H:%M:%S'))
	print (dbegin)

	zeroDayAgo = (datetime.datetime.now() - datetime.timedelta(days = 0))
	zeroDayAgootherStyleTime = zeroDayAgo.strftime("%Y-%m-%d %H:%M:%S")
	print (zeroDayAgootherStyleTime)
	result = "%s 00:00:00" % zeroDayAgootherStyleTime.split()[0]
	print (result)
	#dend=time.mktime(time.strptime(result,'%Y-%m-%d %H:%M:%S')) # - 28800

	format_otherStyleTime3 = "%s %s:%s:00" % (
	zeroDayAgootherStyleTime.split()[0], zeroDayAgootherStyleTime.split()[1].split(':')[0],
	zeroDayAgootherStyleTime.split()[1].split(':')[1])

	dend = time.mktime(time.strptime(format_otherStyleTime3, '%Y-%m-%d %H:%M:%S'))
	print (dend)



def login_pycacti_getimage(db, de, httpsrc, httppw, graphid):
	#values = {'action':'login', 'login_username':'tech_21vianet','login_password':'MitKghYe' }
	#values = {'action':'login', 'login_username':'admin','login_password':'eZeV2FE1*S' }
	values = {'action':'login', 'login_username':'admin','login_password': httppw }
	data = urllib.parse.urlencode(values).encode(encoding='UTF8')
	print (data)
	idxh = 'http://' + httpsrc
	print (idxh)
	#request = urllib2.Request(idxh + '/index.php', data ,headers)
	request = urllib.request.Request(idxh, data ,headers)
	res = urlOpener.open(request).read()
	print (request)
	#get image
	#request = urllib2.Request("http://211.152.48.100/graph_image.php?action=zoom&local_graph_id=9172&rra_id=0&view_type=&graph_start=%s&graph_end=%s&graph_height=120&graph_width=600&title_font_size=10"%(int(db),int(de)), None ,headers)
	request = urllib.request.Request(idxh + '/graph_image.php?action=zoom&local_graph_id=%s&rra_id=0&view_type=&graph_start=%s&graph_end=%s&graph_height=120&graph_width=600&title_font_size=10' % (int(graphid), int(db), int(de)), None ,headers)
	res = urlOpener.open(request).read()
	print (request)
	return (res)


if __name__=='__main__':
	range_date()
	socket.setdefaulttimeout(10)
	headers={}
	cookiejar = http.cookiejar.CookieJar()
	urlOpener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookiejar))
	for key, value in pycactisetting_unshared.unsharedbands.items():
		print(key + ':' + value)
		res = login_pycacti_getimage(dbegin, dend, pycactisetting.cacti_suser_wgq, pycactisetting.cacti_passw_wgq, value)
		#   #print res
	    #   #save image to file
	    #   #file_name = '/backups/localroot/pub/easybridge-BA/manjisweet/' + str(dbegin) + '.png'
		file_name = './/BA-unshared//' + key + '.png'
		print (file_name)
		file_object = open(file_name, 'wb')
		file_object.write(res)
		#print res
		file_object.close()
	print ('function done!')


	for key, value in pycactisetting_unshared.unsharedbands.items():
		print(key + ':' + value)
		res2 = login_pycacti_getimage(dbegin, dend, pycactisetting.cacti_suser_chj, pycactisetting.cacti_passw_chj, value)
		#print res2
		file_name2 = './/BA-unshared-chj//' + key + str("_CHJ") + '.png'
		print (file_name2)
		file_object2 = open(file_name2, 'wb')
		file_object2.write(res2)
		file_object2.close()
	print ('function2 done!')


