import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

import psutil

from user_friendly.output import *


class MemoryInfoError(Exception):
	def __init__(self, flag):
		self.message = f'Flag \'{flag}\' does not exist!'
		super().__init__(self.message)


class MemoryInfo():
	@staticmethod
	def get_mem_size(flag, format=True):
		svmem = psutil.virtual_memory()
		if flag == 'mem-size-total':
			if format:
				return convert_bytes(svmem.total)
			return svmem.total
		elif flag == 'mem-size-avialable':
			if format:
				return convert_bytes(svmem.avialable)
			return svmem.avialable
		elif flag == 'mem-size-used':
			if format:
				return convert_bytes(svmem.used)
			return svmem.used
		elif flag == 'mem-size-total-percentage':
			if format:
				return f'{convert_bytes(svmem.percent)}%'
			return svmem.percent
		raise MemoryInfoError(flag)

	@staticmethod
	def get_swap_mem_info(flag, format=True):
		swap = psutil.swap_memory()
		if flag == 'mem-size-total':
			if format:
				return convert_bytes(swap.total)
			return swap.total
		elif flag == 'mem-size-avialable':
			if format:
				return convert_bytes(swap.free)
			return swap.free
		elif flag == 'mem-size-used':
			if format:
				return convert_bytes(swap.used)
			return swap.used
		elif flag == 'mem-size-total-percentage':
			if format:
				return f'{convert_bytes(swap.percent)}%'
			return swap.percent
		raise MemoryInfoError(flag)