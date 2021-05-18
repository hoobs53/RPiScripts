#!/usr/bin/python3
import sys
import getopt
from sense_emu import SenseHat
xvalue = ''
yvalue = ''
rvalue = ''
gvalue = ''
bvalue = ''
sysarg = sys.argv[1:]
sense = SenseHat()
try:
	opts, args = getopt.getopt(sysarg, 'x:y:r:g:b:')
except getopt.GetoptError as err:
	print(err)
	sys.exit(1)

for opt, arg in opts:
	if opt in '-x':
		xvalue = arg
	elif opt in '-y':
		yvalue = arg
	elif opt in '-r':
		rvalue = arg
	elif opt in '-g':
        	gvalue = arg
	elif opt in '-b':
        	bvalue = arg

args_given = xvalue and yvalue and rvalue and gvalue and bvalue
if not args_given:
	print("arguments not given")
	sys.exit(2)
    
x = int(xvalue)
y = int(yvalue)
r = int(rvalue)
g = int(gvalue)
b = int(bvalue)
cords_valid = x >= 0 and x <= 7 and y>= 0 and y <= 7
rgb_valid = r>=0 and r<=255 and g>=0 and g<=255 and b>=0 and b<=255
if cords_valid and rgb_valid:
	sense.set_pixel(x, y, r, g, b)
    
else:
	print("Wrong args given")
	sys.exit(3)

for arg in opts:
	sysarg.remove(arg[0])
	if arg[1]:
		sysarg.remove(arg[1])

index = 1
for arg in sysarg:
	index = index + 1
