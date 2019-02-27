# def rgb(a, b, c):
# 	if(a < 0 or b < 0 or c < 0):
# 		return "Invalide argument"
# 	else:
# 		return("#" + format(a, '02x') + format(b, '02x') + format(c, '02x'))
# # reference from https://stackoverflow.com/questions/14678132/python-hexadecimal


def rgb(r, g, b):
	if r > 255 or r < 0 or g > 255 or g < 0 or b > 255 or b < 0:
		return('Invalid argument')
	else:
		return('#%02x%02x%02x' % (r, g, b))


print(rgb(255, 0, 0))