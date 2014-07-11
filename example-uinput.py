import serial
import uinput
import sys
import time

uinput.BTN_UP = (1, 264)
uinput.BTN_DOWN = (1, 265)
uinput.BTN_LEFT = (1, 266)
uinput.BTN_RIGHT = (1, 267)

events = (
        uinput.BTN_0,
        uinput.BTN_1,
        uinput.BTN_2,
        uinput.BTN_3,
        uinput.BTN_4,
        uinput.BTN_5,
        uinput.BTN_6,
        uinput.BTN_7,
        uinput.BTN_UP,
		uinput.BTN_DOWN,
		uinput.BTN_LEFT,
		uinput.BTN_RIGHT,
        uinput.ABS_X + (0, 255, 0, 0),
        uinput.ABS_Y + (0, 255, 0, 0),
        )

device = uinput.Device(events) 

buttons = {1:uinput.BTN_0, 2:uinput.BTN_1, 3:uinput.BTN_6, 4:uinput.BTN_7, 5:uinput.BTN_UP, 6:uinput.BTN_DOWN, 7:uinput.BTN_LEFT, 8:uinput.BTN_RIGHT, 9:uinput.BTN_2, 10:uinput.BTN_3, 11:uinput.BTN_4, 12:uinput.BTN_5}

ser = serial.Serial('/dev/ttyACM0', 9600)

sc = []
c = ''

while 1:
	c = ser.read()
	
	if c != '#':
		try:
			sc.append(int(c))
		except:
			pass
	else:
		while len(sc) < 12:
			sc.insert(0,0)
		
		for k, i in enumerate(reversed(sc)):
			
			print k+1,i
			
			device.emit(buttons[k+1], i)
		print "\n"*3
		sc = []
	time.sleep(0.0001)

if(ser.isOpen()):
	print "Serial connection is still open."

ser.close()
