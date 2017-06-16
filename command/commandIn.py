#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import task
import os
import glob
import time
from utils import logger
from run.run import run

class ProcessObr(object):
	"""docstring for ProcessObr"""

	def __init__(self, task, log):
		self.task = task
		self.log = log
		self.flag = 'start'
		print("create proc task id:" + str(id(self.task)))
		logger.logs(self.log, "create proc task id:" + str(id(self.task)))

	def inner(self):
		""" inner catalog """

		while True:

			if self.flag == 'stop':
				logger.logs(self.log, "break task")
				break

			names = glob.glob(self.task.path_in + self.task.maska)
			for file in names:
				if os.path.isfile(file):
					logger.logs(self.log, "name: " + self.task.name + " file: " + file)
					run(file, self.task, self.log, 'in') # to command
			
			logger.logs(self.log, "finish task")
			time.sleep(int(self.task.period))
