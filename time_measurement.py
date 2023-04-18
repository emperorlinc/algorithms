import time
from functools import wraps

def time_measurement(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		time_start = time.time()
		fn(*args, **kwargs)
		time_end = time.time()
		print("Total Execution Time: %d" % round((time_end - time_start), 3))
		return fn(*args, **kwargs)
	return wrapper

