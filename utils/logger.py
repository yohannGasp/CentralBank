#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time

def logs(LOG, msg):
	"""function logs"""
	try:
		log = open(str(LOG),'a')
		log.write(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + ' ' + msg + '\n')
	finally:
		log.close()
