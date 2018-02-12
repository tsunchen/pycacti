#! /usr/bin/env python
# coding=utf-8
# get image manjisweet()

import time,datetime,socket,urllib,urllib2,cookielib
import pycactisetting

from   pycacti_b4948 import *

#import numpy as np
#import cv2, matplotlib.pyplot as plt

#threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days = 10)) 
#print datetime.datetime.now()
#print datetime.timedelta(days = 10)

#
# designed on 2018-02-09
#
def range_date_from_minute():
        global dbegin
        global dend
        #oneDayAgo = (datetime.datetime.now() - datetime.timedelta(days = 1, hours = -8))
        oneDayAgo = (datetime.datetime.now() - datetime.timedelta(days = 1))
        print oneDayAgo

        oneDayAgootherStyleTime = oneDayAgo.strftime("%Y-%m-%d %H:%M:%S") 
        print oneDayAgootherStyleTime

        format_otherStyleTime = "%s 00:00:00" % oneDayAgootherStyleTime.split()[0]
        ##print format_otherStyleTime

        ##print oneDayAgootherStyleTime.split()[1]
        ##print oneDayAgootherStyleTime.split()[1].split(':')[0]
        ##print oneDayAgootherStyleTime.split()[1].split(':')[1]

        format_otherStyleTime2 = "%s %s:%s:00" % (oneDayAgootherStyleTime.split()[0], oneDayAgootherStyleTime.split()[1].split(':')[0], oneDayAgootherStyleTime.split()[1].split(':')[1])
        ##print format_otherStyleTime2
        #dbegin=time.mktime(time.strptime(format_otherStyleTime,'%Y-%m-%d %H:%M:%S')) - 28800
        dbegin=time.mktime(time.strptime(format_otherStyleTime2,'%Y-%m-%d %H:%M:%S'))
        ##print dbegin


        #zeroDayAgo = (datetime.datetime.now() - datetime.timedelta(hours = -8))
        zeroDayAgo = (datetime.datetime.now() - datetime.timedelta(days = 0))
        zeroDayAgootherStyleTime = zeroDayAgo.strftime("%Y-%m-%d %H:%M:%S")
        ##print zeroDayAgootherStyleTime

        ##print zeroDayAgootherStyleTime.split()[1]
        ##print zeroDayAgootherStyleTime.split()[1].split(':')[0]
        ##print zeroDayAgootherStyleTime.split()[1].split(':')[1]

        format_otherStyleTime3 = "%s %s:%s:00" % (zeroDayAgootherStyleTime.split()[0], zeroDayAgootherStyleTime.split()[1].split(':')[0], zeroDayAgootherStyleTime.split()[1].split(':')[1])
        ##print format_otherStyleTime3

        #result = "%s 00:00:00" % zeroDayAgootherStyleTime.split()[0]
        #print result
        #dend=time.mktime(time.strptime(result,'%Y-%m-%d %H:%M:%S')) - 28800
        dend=time.mktime(time.strptime(format_otherStyleTime3,'%Y-%m-%d %H:%M:%S'))
        ##print dend


def range_date():
        global dbegin
        global dend
        #oneDayAgo = (datetime.datetime.now() - datetime.timedelta(days = 1, hours = -8))
        oneDayAgo = (datetime.datetime.now() - datetime.timedelta(days = 1))
        print oneDayAgo

        oneDayAgootherStyleTime = oneDayAgo.strftime("%Y-%m-%d %H:%M:%S") 
        print oneDayAgootherStyleTime

        format_otherStyleTime = "%s 00:00:00" % oneDayAgootherStyleTime.split()[0]
        print format_otherStyleTime

        #print oneDayAgootherStyleTime.split()[1]
        #print oneDayAgootherStyleTime.split()[1].split(':')[0]
        #print oneDayAgootherStyleTime.split()[1].split(':')[1]

        #format_otherStyleTime2 = "%s %s:%s:00" % (oneDayAgootherStyleTime.split()[0], oneDayAgootherStyleTime.split()[1].split(':')[0], oneDayAgootherStyleTime.split()[1].split(':')[1])
        #print format_otherStyleTime2
        #dbegin=time.mktime(time.strptime(format_otherStyleTime,'%Y-%m-%d %H:%M:%S')) - 28800
        dbegin=time.mktime(time.strptime(format_otherStyleTime,'%Y-%m-%d %H:%M:%S'))
        print dbegin


        #zeroDayAgo = (datetime.datetime.now() - datetime.timedelta(hours = -8))
        zeroDayAgo = (datetime.datetime.now() - datetime.timedelta(days = 0))
        zeroDayAgootherStyleTime = zeroDayAgo.strftime("%Y-%m-%d %H:%M:%S")
        print zeroDayAgootherStyleTime
        result = "%s 00:00:00" % zeroDayAgootherStyleTime.split()[0]
        print result
        #dend=time.mktime(time.strptime(result,'%Y-%m-%d %H:%M:%S')) - 28800
        dend=time.mktime(time.strptime(result,'%Y-%m-%d %H:%M:%S'))
        print dend



def login_pycacti_getimage(db, de, httpsrc, httppw):
        #values = {'action':'login', 'login_username':'tech_21vianet','login_password':'MitKghYe' }
        #values = {'action':'login', 'login_username':'admin','login_password':'eZeV2FE1*S' }
        values = {'action':'login', 'login_username':'admin','login_password': httppw }
        data = urllib.urlencode(values)
        ##print data

        idxh = 'http://' + httpsrc
        ##print idxh
        #request = urllib2.Request(idxh + '/index.php', data ,headers)
        request = urllib2.Request(idxh, data ,headers)
        res = urlOpener.open(request).read()
        print request
        #get image
        '''
        #request = urllib2.Request("http://211.152.48.100/graph_image.php?action=zoom&local_graph_id=9172&rra_id=0&view_type=&graph_start=%s&gra
ph_end=%s&graph_height=120&graph_width=600&title_font_size=10"%(int(db),int(de)), None ,headers)
        '''
        ###request = urllib2.Request(idxh + '/graph_image.php?action=zoom&local_graph_id=9172&rra_id=0&view_type=&graph_start=%s&graph_end=%s&graph_height=120&graph_width=600&title_font_size=10' % (int(db), int(de)), None ,headers)
        request = urllib2.Request(idxh + '/graph_image.php?action=zoom&local_graph_id=14987&rra_id=0&view_type=&graph_start=%s&graph_end=%s&graph_height=120&graph_width=600&title_font_size=10' % (int(db), int(de)), None ,headers)
        #request = urllib2.Request(idxh + '/graph.php?action=zoom&local_graph_id=14987&rra_id=0&view_type=tree&graph_start=%s&graph_end=%s' % (int(db), int(de)), None ,headers)
        #request = urllib2.Request(idxh + '/graph.php?action=zoom&local_graph_id=14987&rra_id=0&graph_start=%s&graph_end=%s' % (int(db), int(de)), None ,headers)
        #
        #http://110.173.1.249/graph.php?action=zoom&local_graph_id=9172&rra_id=0&graph_start=1518062268&graph_end=1518148668
        #http://203.166.160.152/graph.php?action=zoom&local_graph_id=14987&rra_id=0&graph_start=1518062446&graph_end=1518148846
        ##request = urllib2.Request(idxh + '/graph.php?action=zoom&local_graph_id=9172&rra_id=0&graph_start=%s&graph_end=%s&graph_height=120&graph_width=600&title_font_size=10' % (int(db), int(de)), None ,headers)
        #request = urllib2.Request("http://110.173.1.249/graph_image.php?action=zoom&local_graph_id=%s&rra_id=0&view_type=&graph_start=%s&graph_end=%s&graph_height=120&graph_width=600&title_font_size=0"%(int(gid),int(db),int(de)), None ,headers)
        res = urlOpener.open(request).read()
        #print res
        return res


if __name__=='__main__':

        #range_date()
        range_date_from_minute()



        socket.setdefaulttimeout(10)
        headers={}
        cookiejar = cookielib.CookieJar()
        urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))


        res = login_pycacti_getimage(dbegin, dend, pycactisetting.cacti_suser_wgq, pycactisetting.cacti_passw_wgq)
        #print res
        # save image to file
        #file_name = '/backups/localroot/pub/easybridge-BA/manjisweet/' + str(dbegin) + '.png'
        #file_name = '/backups/localroot/pub/easybridge-BA/manjisweet/' + str("manji") + '.png'
        #file_name = r'E:\backupswitch\localroot\pub\pycacti' + str("\manji") + '.png'
        file_name = r'E:\pycacti' + str("\\b4948") + '.png'
        print file_name
        file_object = open(file_name, 'wb')
        file_object.write(res)
        #print res
        file_object.close()
        print 'function done!'


        res2 = login_pycacti_getimage(dbegin, dend, pycactisetting.cacti_suser_chj, pycactisetting.cacti_passw_chj)
        #print res2
        #file_name2 = '/backups/localroot/pub/easybridge-BA/manjisweet/' + str("manji_chj") + '.png'
        file_name2 = r'E:\pycacti' + str("\\b4948_chj") + '.png'
        print file_name2
        file_object2 = open(file_name2, 'wb')
        file_object2.write(res2)
        file_object2.close()
        print 'function2 done!'


        res3 = login_pycacti_getimage(dbegin, dend, pycactisetting.cacti_suser_bj, pycactisetting.cacti_passw_bj)
        #print res2
        #file_name2 = '/backups/localroot/pub/easybridge-BA/manjisweet/' + str("manji_chj") + '.png'
        file_name3 = r'E:\pycacti' + str("\\b4948_bj") + '.png'
        print file_name3
        file_object2 = open(file_name3, 'wb')
        file_object2.write(res3)
        file_object2.close()
        print 'function3 done!'

        ###
        nlist = []
        nlist.append(get_FileSize(r'E:/pycacti/b4948.png'))
        nlist.append(get_FileSize(r'E:/pycacti/b4948_chj.png'))
        nlist.append(get_FileSize(r'E:/pycacti/b4948_bj.png'))
        for n in nlist:
            print n
        narray=numpy.array(nlist)
        sum1=narray.sum()
        narray2=narray*narray
        sum2=narray2.sum()
        N=len(nlist)
        mean=sum1/N
        print "mean: %s" % mean
        var=sum2/N-mean**2
        var = var / 10000
        if var < 10:
                print "expected var: %s" % var
        elif var < 20:
                print "warning var: %s" % var
        else:
                print "critical var: %s" % var
