import psutil


class CPUinfoException(Exception):
	def __init__(self, flag):
		self.message = f'Flag \'{flag}\' does not exist.'
		super().__init__(self.message)


class CPUinfo():
	@staticmethod
	def get_cpu_cores(flag=None):
		return psutil.cpu_count(logical=False) if flag == 'cpu-cores-physical' else return psutil.cpu_count()

	@staticmethod
	def get_cpu_frequencies(flag=None, format=False):
		cpufreq = psutil.cpu_freq()
		if flag == 'cpu-freq-current':
			if format:
				return f'{cpufreq.current:.2f}Mhz'
			return cpufreq.current
		elif flag == 'cpu-freq-min': 
			if format:
				return f'{cpufreq.min:.2f}Mhz'
			return cpufreq.min
		elif flag == 'cpu-freq-max':
			if format:
				return f'{cpufreq.max:.2f}Mhz'
			return cpufreq.max
		raise CPUinfoException(flag)


	@staticmethod
	def get_cpu_usage(flag=None, format=False):
		if flag == 'cpu-usage-percore':
			for core, precentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
				if format:
					return f'{core} : {precentage}%'
				return core, precentage
		if format:
			return f'{psutil.cpu_percent()}%'
		return psutil.cpu_percent()
