#/usr/bin/python
import cgi
import cgitb;
import json
from sense_emu import SenseHat
print("Content-Type: text/html")
print()
sense = SenseHat()
cgitb.enable()
form = cgi.FieldStorage()
data_filled = "x" in form and "y" in form and "r" in form and "g" in form and "b" in form
if data_filled:
    x = int(form['x'].value)
    y = int(form['y'].value)
    r = int(form['r'].value)
    g = int(form['g'].value)
    b = int(form['b'].value)
    sense.set_pixel(x, y, r, g, b)
    print("Pixel on " + str(x) + " " + str(y) + " has been set (" + str(r) + ", " + str(g) + ", " + str(b) + ")")
else:
    print("Error")
