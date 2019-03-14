# The Example 00:
global data
data = {}

def put(key, value):
	data[key] = value


def get(key):
	if key in data.keys():
		return data[key]
	else:
		return None


# The Example 01:
def exists(key):
	if key in data.keys():
		return True
	else:
		return False


# The Example 02:
def delete(key):
	if key in data.keys():
		del(data[key])
	else:
		print('The key doesnt exist.')


# The Example 03:
def incr(key):
	if key not in data.keys():
		data[key] = 0 + 1
	else:
		try:
			data[key] += 1
		except TypeError:
			raise ValueError("Incorrect value")


def incrby(key, delta):
	if key not in data.keys():
		data[key] = 0 + delta
	else:
		try:
			data[key] += delta
		except TypeError:
			raise ValueError("Incorrect value")


# The Example 04:
def sadd(key, value):
	if key in data.keys():
		if type(data[key]) != set:
			data[key] = {value}
		else:
			data[key].add(value)
	else:
		data[key] = {value}


def smembers(key):
	if key not in data.keys():
		return None
	else:
		if data[key] == {}:
			return {}
		elif type(data[key]) != set:
			return None
		else:
			return data[key]


# The Example 05:
def sunion(key1, key2):
	if key1 not in data.keys() and key2 in data.keys():
		return data[key2]
	elif key1 in data.keys() and key2 not in data.keys():
		return data[key1]
	elif key1 not in data.keys() and key2 not in data.keys():
		return {}
	else:
		return data[key1].union(data[key2])


def sinter(key1, key2):
	if key1 in data.keys() and key2 in data.keys():
		return data[key1].intersection(data[key2])
	else:
		return {}


# The Example 06:
def srem(key, value):
	if key in data.keys():
		if type(data[key]) == set and value in data[key]:
			data[key].remove(value)
			if len(data[key]) == 0:
				data[key] = {}

