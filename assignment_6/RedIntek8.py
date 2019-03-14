# The Example 00:
global data
data = {}

def put(key, value):
	data[key] = value
	return value


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
def delete(*keys):
	num = 0
	for key in keys:
		if key in data.keys():
			del(data[key])
			num += 1
	return num


# The Example 03:
def incr(key):
	if key not in data.keys():
		data[key] = 0 + 1
		return 1
	else:
		try:
			data[key] += 1
			return data[key]
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
def sadd(key, *values):
	set_value = []
	for value in values:
		set_value.append(value)
	set_value = set(set_value)
	if key in data.keys():
		if type(data[key]) != set:
			data[key] = set_value
		else:
			data[key].union(set_value)
	else:
		data[key] = set_value
	return len(set_value)


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
			return True
	return False


print(exists('singers'))
print(sadd('singers', 'Michael Jackson', 'Madonna', 'Elvis', 'Madonna'))
print(smembers('singers'))
