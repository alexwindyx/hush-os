import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from user_friendly.output import *
import hushclock

from colorama import init
from colorama import Fore, Style


# Logging system by k1tsukendo #
class kitsulogger():
	@staticmethod
	def set_default_log_level(level):
		global loglvl
		loglvl = level

	@staticmethod
	def log(message, task='info'):
		if loglvl == 1:
			return f'[info : {task} : {hushclock.hushclock.get_local_time(True)}] : {message}'
		elif loglvl == 2:
			return f'[warning : {task} : {hushclock.hushclock.get_local_time(True)}] : {message}'
		elif loglvl == 3:
			return f'{Fore.LIGHTRED}[error : {task} : {hushclock.hushclock.get_local_time(True)}] : {message}{Style.RESET_ALL}'
		elif loglvl == 4:
			return f'{Fore.RED}[{Fore.YELLOW}CRITICAL{Fore.RED} : {task} : {hushclock.hushclock.get_local_time(True)}] : {message}{Style.RESET_ALL}'
		return
