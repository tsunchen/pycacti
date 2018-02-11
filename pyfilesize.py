#!/usr/bin/env python
#coding=utf8  

import time
import datetime

import os

import numpy

def get_FileSize(filePath):
	filePath = unicode(filePath,'utf8')
	fsize = os.path.getsize(filePath) - 30000
	#fsize = fsize/float(1024*1024)
	return round(fsize,2)

if __name__=='__main__':
	#print get_FileSize(r'E:/pycacti/20180209/b4948.png')
	#print get_FileSize(r'E:/pycacti/20180209/b4948_bj.png')
	#print get_FileSize(r'E:/pycacti/20180209/b4948_chj.png')
	nlist = []
	nlist.append(get_FileSize(r'E:/pycacti/20180209/b4948.png'))
	nlist.append(get_FileSize(r'E:/pycacti/20180209/b4948_bj.png'))
	nlist.append(get_FileSize(r'E:/pycacti/20180209/b4948_chj.png'))
	print nlist
	narray=numpy.array(nlist)
	sum1=narray.sum()
	narray2=narray*narray
	sum2=narray2.sum()
	N=len(nlist)
	mean=sum1/N
	print mean
	var=sum2/N-mean**2
	print var

	nlist = []
	nlist.append(get_FileSize(r'E:/pycacti/b4948.png'))
	nlist.append(get_FileSize(r'E:/pycacti/b4948_bj.png'))
	nlist.append(get_FileSize(r'E:/pycacti/b4948_chj.png'))
	print nlist
	narray=numpy.array(nlist)
	sum1=narray.sum()
	narray2=narray*narray
	sum2=narray2.sum()
	N=len(nlist)
	mean=sum1/N
	print mean
	var=sum2/N-mean**2
	print var


