#!/usr/bin/python3
# -*- coding: utf-8 -*-
# 
# Process obr file Central Bank
# 
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

import time
import json
import os
import sys
import shutil
import glob
import threading
import sqlite3
import task
from tkinter import *
from utils import logger
from command.commandIn import ProcessObr

procList = []

def donothing():
	pass

def main():
	"""  main """

	try:

		def stop():
			""" stop """
			for pr in procList:
				pr.flag = 'stop'
				logger.logs(LOG, "stop proc task id:" + str(id(pr.task)))
				print("stop proc task id:" + str(id(pr.task)))

		def out():
			pass

		"""
		settings.json parse

		"""
		conf = open('settings.json','r')
		param = conf.read()
		js_param = json.loads(param)

		LOG      = js_param['log']
		SETT     = js_param['settings']

		logger.logs(LOG, "start programm")

		global procList

		"""
		tkinter

		"""
		root = Tk()
		menubar = Menu(root)
		filemenu = Menu(menubar, tearoff = 0)
		filemenu.add_command(label = "Выход", command = stop)
		menubar.add_cascade(label = "Файл", menu = filemenu)

		editmenu = Menu(menubar, tearoff=0)
		editmenu.add_separator()
		menubar.add_cascade(label = "Отправка", menu = editmenu)
		
		servicemenu = Menu(menubar, tearoff=0)
		servicemenu.add_command(label = "Проверить ключи", command = donothing)
		servicemenu.add_command(label = "asrkeyw", command = donothing)
		servicemenu.add_command(label = "Остановить обработку", command = stop)
		menubar.add_cascade(label = "Сервис", menu = servicemenu)

		helpmenu = Menu(menubar, tearoff=0)
		helpmenu.add_command(label = "О программе", command = donothing)
		menubar.add_cascade(label = "Справка", menu = helpmenu)


		for element in SETT:

			sheduleTask = task.Task(element['name'], element['path_in'], element['maska'], element['archive'], element['target'], element['period'], element['command_in'], element['command_out'], element['path_out'])

			if not os.path.exists(sheduleTask.path_in):
				os.makedirs(sheduleTask.path_in)

			if not os.path.exists(os.path.join(sheduleTask.archive,'in')):
				os.makedirs(os.path.join(sheduleTask.archive,'in'))

			if not os.path.exists(os.path.join(sheduleTask.archive,'out')):
				os.makedirs(os.path.join(sheduleTask.archive,'out'))

			if not os.path.exists(sheduleTask.target):
				os.makedirs(sheduleTask.target)

			if not os.path.exists(sheduleTask.path_out):
				os.makedirs(sheduleTask.path_out)

			editmenu.add_command(label = sheduleTask.name, command = donothing)  #add menu
			editmenu.add_separator()

			proc = ProcessObr(sheduleTask, LOG)
			procList.append(proc)

			thread = threading.Thread(target=proc.inner)
			thread.start()
			
		root.title("Обработка отчетности")
		root.config(menu = menubar)
		root.geometry('1121x443')
		root.resizable(False, False)
		root.mainloop()

	except Exception as e:
		logger.logs(LOG, "error: {0}".format(e))
	
if __name__ == "__main__":
	main()