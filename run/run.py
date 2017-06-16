#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Copyright 2017 by BaikalInvestBank. All Rights Reserved.
#
# Permission to use, copy, modify, and distribute this software and its
# documentation for any purpose and without fee is hereby granted,
# provided that the above copyright notice appear in all copies and that
# both that copyright notice and this permission notice appear in
# supporting documentation, and that the name of Vinay Sajip
# not be used in advertising or publicity pertaining to distribution
# of the software without specific, written prior permission.
# VINAY SAJIP DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING
# ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL
# VINAY SAJIP BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR
# ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER
# IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT
# OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

"""
Interpretator package for Python. 

Copyright (C) 2017 BaikalInvestBank. All Rights Reserved.

"""

import subprocess
import os
import shutil
from utils import logger


def wrapperVerba(param):
	pass
	# proc = subprocess.Popen("wrapperVerba.exe", shell=True, stdout=subprocess.PIPE)
	# return proc.stdout.readlines()

def ShellExecute(name, param):
	proc = subprocess.Popen(name, shell=True, stdout=subprocess.PIPE)
	return proc.stdout.readlines()

def run(file, task, log, direction):
	""" run method interpretator """
	
	if direction == 'in':
		line = task.command_in
	elif direction == 'out':
		line = task.command_out
	
	lineList = line.split(';')
	for command in lineList:

		#
		# verba
		# 
		
		if command == 'LOADKEY_1':
			wrapperVerba('LOADKEY_1')
		elif command == 'LOADKEY_2':
			wrapperVerba('LOADKEY_2')
		elif command == 'SIGN_1':
			wrapperVerba('file,NUM_KEY1,SERIA1') # !!!
		elif command == 'SIGN_2':
			wrapperVerba('')
		elif command == 'DELSIGN':
			wrapperVerba('DELSIGN')
		elif command == 'RESETKEY_1':
			wrapperVerba('RESETKEY_1 NUM_KEY1 + SERIA1')  # !!!
		elif command == 'RESETKEY_2':
			wrapperVerba('RESETKEY_2 NUM_KEY2 + SERIA2') # !!!
		elif command == 'CRYPT_1(KLIKO)':
			wrapperVerba('CRYPT_1(KLIKO) file NUM_KEY1,SERIA1,kliko') # !!!
		elif command == 'CRYPT_2(FTS)':
			wrapperVerba('CRYPT_2(FTS) file, NUM_KEY2,SERIA2,fts') # !!!
		elif command == 'DECRYPT':
			wrapperVerba('DECRYPT fl,NUM_KEY2)')
		elif command == 'DECRYPT1':
			wrapperVerba('DECRYPT1 fl,NUM_KEY1)')

		#	
		# os
		# 

		elif not command.find('MOVE_IN', 0) == -1:

			shutil.move(file, task.target)
			logger.logs(log, "MOVE_IN: " + file + " " + task.target)

		elif not command.find('MOVE_OUT', 0) == -1:

			shutil.move(file, task.path_out)
			logger.logs(log, "MOVE_OUT: " + file + " " + task.path_out)

		elif not command.find('ARCHIVE_IN', 0) == -1:

			shutil.copy(file, os.path.join(task.archive,'in'))
			logger.logs(log, "ARCHIVE_IN: " + file + " " + os.path.join(task.archive,'in'))

		elif not command.find('ARCHIVE_OUT', 0) == -1:			

			shutil.copy(file, os.path.join(task.archive,'out'))
			logger.logs(log, "ARCHIVE_OUT: " + file + " " + os.path.join(task.archive,'out'))



		elif not command.find('SCRIPT', 0) == -1:
			pass

			# ShellExecute(script_name)