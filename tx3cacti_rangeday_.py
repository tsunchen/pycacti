#!/usr/bin/env python
#coding=utf-8
#get image manjisweet()

import time,datetime,socket,urllib
import http.cookiejar
import TSunxCactisetting as pycactisetting


#import numpy as np
#import cv2, matplotlib.pyplot as plt

#threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days = 10)) 
#print datetime.datetime.now()
#print datetime.timedelta(days = 10)

import argparse



#
def main_easelay(args):
    print("")
    print("--cactigid {0}".format(args.cactigid))
    print("--drange {0}".format(args.drange))
    #print("--dfc {0}".format(args.dfc))
    #print("--dorg {0}".format(args.dorg))
    #print("--dpst {0}".format(args.dgpst))
    #args.dgname, args.dgdesc, args.dgorg, args.dgpst
    #print("--wanport {0}".format(args.wanport))   	    #port的类型为int类型，如果命令行中没有输入该选项则报错
    #print("--wanaddress {0}".format(args.code_address))    #args.address会报错，因为指定了dest的值
    #print("--wangateway {0}".format(args.wangateway))      #args.gateway会报错，因为指定了dest的值
    #print("--templatename {0}".format(args.templatename))                   #args.templatename会报错，因为指定了dest的值
    #print("--save {0}".format(args.save))                   #args.save会报错，因为指定了dest的值
    #print("--flag {0}".format(args.flag))   		    #如果命令行中该参数输入的值不在choices列表中，则报错
    #print("-l {0}".format(args.log))  			    #如果命令行中输入该参数，则该值为True。因为为短格式"-l"指定了别名"--log"，所以程序中用args.log来访问



def range_date(day):
	global dbegin
	global dend
	oneDayAgo = (datetime.datetime.now() - datetime.timedelta(days = int(day)))
	print (oneDayAgo)

	oneDayAgootherStyleTime = oneDayAgo.strftime("%Y-%m-%d %H:%M:%S") 
	print (oneDayAgootherStyleTime)

	format_otherStyleTime = "%s 00:00:00" % oneDayAgootherStyleTime.split()[0]
	print (format_otherStyleTime)
	dbegin=time.mktime(time.strptime(format_otherStyleTime,'%Y-%m-%d %H:%M:%S')) #  - 28800
	print (dbegin)

	zeroDayAgo = (datetime.datetime.now() - datetime.timedelta(days = 0))
	zeroDayAgootherStyleTime = zeroDayAgo.strftime("%Y-%m-%d %H:%M:%S")
	print (zeroDayAgootherStyleTime)
	result = "%s 00:00:00" % zeroDayAgootherStyleTime.split()[0]
	print (result)
	dend=time.mktime(time.strptime(result,'%Y-%m-%d %H:%M:%S')) # - 28800
	print (dend)
	return oneDayAgootherStyleTime.split()[0], zeroDayAgootherStyleTime.split()[0]



def login_pycacti_getimage(db, de, httpsrc, httppw, gid):
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
	request = urllib.request.Request(idxh + '/graph_image.php?action=zoom&local_graph_id=' + gid + '&rra_id=0&view_type=&graph_start=%s&graph_end=%s&graph_height=120&graph_width=600&title_font_size=10' % (int(db), int(de)), None ,headers)
	res = urlOpener.open(request).read()
	#print res
	return (res)



if __name__=='__main__':
    parser = argparse.ArgumentParser(usage="TSunx Cacti, it's usage on easylay on the Cacti in range.", description="help info.")
    parser.add_argument("-g", "--cactigid", default="9172", help="cacti graph id with string: _ device cacti display graph _")
    parser.add_argument("-d", "--drange", default="1", help="range with string: _device cacti display in range of days_")
    args = parser.parse_args()
    main_easelay(args)
    drangefrom, drangeto = range_date(args.drange)
    socket.setdefaulttimeout(10)
    headers={}
    cookiejar = http.cookiejar.CookieJar()
    urlOpener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookiejar))
    res = login_pycacti_getimage(dbegin, dend, pycactisetting.cacti_suser_wgq, pycactisetting.cacti_passw_wgq, args.cactigid)
    # print res
    #  save image to file
    # #file_name = '/backups/localroot/pub/easybridge-BA/manjisweet/' + str(dbegin) + '.png'
    # file_name = './/BA-manjisweet//' + str("manji") + '.png'
    file_name = './/tx3cacti_png//' + args.cactigid + '//' + str("tx3cacti_") + args.cactigid + '_' + str(drangefrom) + '_' + str(drangeto) + '.png'
    print (file_name)
    file_object = open(file_name, 'wb') 
    file_object.write(res)
    #print res
    file_object.close()
    print ('function done!')
    res2 = login_pycacti_getimage(dbegin, dend, pycactisetting.cacti_suser_chj, pycactisetting.cacti_passw_chj, args.cactigid)
    #print res2
    file_name2 = './/tx3cacti_png//' + args.cactigid + '//' + str("tx3cacti_chj_") + args.cactigid + '_' + str(drangefrom) + '_' + str(drangeto) + '.png'
    print (file_name2)
    file_object2 = open(file_name2, 'wb')
    file_object2.write(res2)
    file_object2.close()
    print ('function2 done!')
