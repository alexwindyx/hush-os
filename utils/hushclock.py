import ntplib
from time import ctime

import datetime


class hushclock():
	@staticmethod
	def get_net_time(server='europe.pool.ntp.org', version=3):
		c = ntplib.NTPClient()
		response = c.request(server, version=version)
		return ctime(response.tx_time)

	@staticmethod
	def get_local_time(format):
		now = datetime.datetime.now()
		if format:
			return '{}.{}.{} {}:{}'.format(now.day, now.month, now.year, now.hour, now.minute)
		return now.day, now.month, now.year, now.hour, now.minute
