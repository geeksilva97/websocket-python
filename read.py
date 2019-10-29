import serial

ser = serial.Serial('/dev/ttyUSB0', 2400, timeout=1, parity=serial.PARITY_NONE)

print("connected to: " + ser.portstr)


# jogando po magico
values = bytearray([5,13])
ser.write(values)

print('recebido')
peso = ser.readline()
peso = peso[1:len(peso)-1]

print(peso.decode())

#print(ser.read())

ser.close()
