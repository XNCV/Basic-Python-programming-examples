import sys

# To read the argument in command line, you need use sys.argv
file  = open(sys.argv[1], 'r')
# The function print includes '\n' to the end of the string
print(file.read(), end='')
file.close()
