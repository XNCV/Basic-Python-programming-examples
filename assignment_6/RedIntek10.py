# The idea to solve the example 10 is that you dont need
# save the the values with its expired time. When we call the
# function get or exists, if it is expired we need delete it
# The functions were changed in this code are put, sadd, hset,
# get, exists, hget.
# https://instructobit.com/tutorial/108/How-to-share-global-variables-between-files-in-Python
import time

# All data was stored in the variable 'data'
global data
data = {}

# Delete specified keys in the dictionary 'data'
def delete(*keys):
	num = 0
	for key in keys:
		if key in data.keys():
			del(data[key])
			num += 1
	return num


# Add new key with value and its expired time
def put(key, value, expires_in=float("inf")):
	# Save the expired time in a list with the value input
	expired_time = time.time() + expires_in
	new_value = []
	new_value.append(value)
	new_value.append(expired_time)
	data[key] = new_value
	return value


# Get the value of specified key
def get(key):
	current_time = time.time()
	if key in data.keys():
		if data[key][1] < current_time:
			delete(key)
			return None
		else:
			return data[key][0]
	else:
		return None


# Is a key exist?
def exists(key):
	current_time = time.time()
	if key in data.keys():
		if data[key][1] < current_time:
			delete(key)
			return False
		else:
			return True
	else:
		return False


# Create a key with a value to equal to 1, if it doesnt exist
# Add 1 to the value of the key, if it exists
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


# Create a key with a value to equal to 'delta', if it doesnt exist
# Add 'delta' to the value of the key, if it exists
def incrby(key, delta):
	if key not in data.keys():
		data[key] = 0 + delta
	else:
		try:
			data[key] += delta
		except TypeError:
			raise ValueError("Incorrect value")


# Add values to the set associated to 'key'
def sadd(key, *values, expires_in=float("inf")):
	expired_time = time.time() + expires_in
	list_value = []
	for value in values:
		list_value.append(value)
	set_value = set(list_value)
	if key in data.keys():
		if type(data[key]) != list:
			data[key] = [set_value, expired_time]
		else:
			if data[key][1] == float("inf"):
				data[key] = [set_value, expired_time]
			else:
				data[key] = [data[key][0].union(set_value), expired_time]
	else:
		data[key] = [set_value, expired_time]
	return len(set_value)


# Return the set values associated to 'key'
def smembers(key):
	current_time = time.time()
	if key not in data.keys():
		return None
	else:
		if data[key][1] < current_time:
			delete(key)
			return None
		else:
			if data[key][0] == {}:
				return {}
			elif type(data[key][0]) != set:
				return None
			else:
				return data[key][0]


# Return all elements appeared in set values of 'key1' and 'key2'
def sunion(key1, key2):
	if key1 not in data.keys() and key2 in data.keys():
		return data[key2]
	elif key1 in data.keys() and key2 not in data.keys():
		return data[key1]
	elif key1 not in data.keys() and key2 not in data.keys():
		return {}
	else:
		return data[key1].union(data[key2])


# Return the common elements of two different sets in 'key1' and 'key2'
def sinter(key1, key2):
	if key1 in data.keys() and key2 in data.keys():
		return data[key1].intersection(data[key2])
	else:
		return {}


# Remove 'value' in the set associated to 'key'
def srem(key, value):
	if key in data.keys():
		if type(data[key]) == set and value in data[key]:
			data[key].remove(value)
			if len(data[key]) == 0:
				data[key] = {}
			return True
	return False


# Add a dictionary {hash_key: hash_value} to 'key'
def hset(key, hash_key, hash_value, expires_in=float("inf")):
	expired_time = time.time() + expires_in
	dic_hash = {}
	dic_hash[hash_key] = hash_value
	if key in data.keys():
		data[key][0].update(dic_hash)
		data[key][1] = expired_time
	else:
		data[key] = [dic_hash, expired_time]
	return dic_hash


# Get the value of 'hash_key' in the hash associated to 'key'
def hget(key, hash_key):
	current_time = time.time()
	if key in data.keys():
		if data[key][1] < current_time:
			delete(key)
			return None
		else:
			if hash_key in data[key][0].keys():
				return data[key][0][hash_key]
			else:
				return None
	else:
		return None


# Get all dictionaries '{hash_key: hash_value,...}' in 
# the hash associated to 'key'
def hgetall(key):
	if key in data.keys():
		return data[key]
	else:
		return None


put("toto", "tata", expires_in=3)
sadd("countries", "Viet Nam", expires_in=3)
print(data)
print(get("toto"))
time.sleep(4)
print(get("toto"))
print(exists("countries"))