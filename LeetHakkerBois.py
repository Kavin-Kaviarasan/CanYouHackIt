#LEET BOIS k

import serial
arduino = serial.Serial('COM3', 115200, timeout=.1)
check = 1;
while check:
	print("Reached here")
	check = 0
print("Reached end")
