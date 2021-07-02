import colorama
from progress.bar import Bar


def convert_bytes(bytes, suffix='B'):
	factor = 1024
	for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi']:
		if bytes < factor:
			return f'{bytes:.2f}{unit}{suffix}'
		bytes /= factor
	del bytes
