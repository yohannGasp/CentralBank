#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Task(object):
	"""struct for Task"""

	path_in     = ""
	maska       = ""
	archive     = ""
	target      = ""
	period      = 0 
	command_in  = []
	command_out = []

	def __init__(self, name, path_in, maska, archive, target, period, command_in, command_out, path_out):
		
		self.name        = name
		self.path_in     = path_in
		self.maska       = maska
		self.archive     = archive
		self.target      = target
		self.period      = period 
		self.command_in  = command_in
		self.command_out = command_out
		self.path_out    = path_out

	def toString(self):
		return self.path_in
				
		