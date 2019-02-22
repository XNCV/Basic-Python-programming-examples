import os


def env_hello():
	# After the 5th character of the string,
	# the type of the encryption was showed
	# and we dont need use this element.
	if os.environ["LANG"][0:5] == "fr_FR":
		return 'Bonjour!'
	else:
		return 'Hello!'


print(env_hello())
