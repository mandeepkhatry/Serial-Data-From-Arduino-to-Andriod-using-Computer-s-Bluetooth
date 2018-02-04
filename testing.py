import socket
import serial

ser = serial.Serial('COM3', 9600)  # Serial port and baud rate in arduino

while True:
	s = ser.readline().decode('utf-8')
	print(s)

ser.close()