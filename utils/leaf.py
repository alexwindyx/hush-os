import pathlib

import os
import sys
import inspect
import time

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from user_friendly.output import *
from colorama import Fore, Style
from utils import kitsu

class leaf():
	@staticmethod
	def list_files(directory, hidden=False):
		_current_dir = pathlib.Path(directory)
		for file in _current_dir.iterdir():
			if os.path.isdir(file):
				if not hidden and str(file).replace(directory, '').startswith('.'):
					continue
				print(f'{Fore.BLUE}{str(file).replace(directory, "")} {Style.RESET_ALL}', end='')
			else:
				if not hidden and str(file).replace(directory, '').startswith('.'):
					continue
				print(str(file).replace(directory, '') + ' ', end='')
		del _current_dir

	@staticmethod
	def create_directory(path):
		try: 
			os.mkdir(path)
			print('Leaf: Created directory at {path}')
		except: pass

	@staticmethod
	def get_file_size(path, format=True):
		if format:
			return convert_bytes(pathlib.Path(path).stat().st_size)
		return pathlib.Path(path).stat().st_size

	@staticmethod
	def say_hello_to_shouka():
		print(f'{Fore.YELLOW}Shalom, Shouka!{Style.RESET_ALL}')
		kitsu.kitsulogger.set_default_log_level(4)
		time.sleep(6)
		while True:
			print(kitsu.kitsulogger.log('SHOUKA IS PYTHON SENIOR PROGRAMMER'))


print(leaf.get_file_size('/home/kitsugi/apps/gzdoom/gzdoom'))
leaf.say_hello_to_shouka()
