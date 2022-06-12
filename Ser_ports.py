# Initialize serial device
import serial

ser = serial.Serial()
# default
print(ser)
# can set value
ser.baudrate = 19200
print(ser)  # c difference in OP
ser.port = 'COM1'
print(ser)
print(ser.is_open)

try:
    ser.open()

except Exception as e:
    print("Unable to open port", e)
print(ser.is_open)

# Also supported with context manager:
with serial.Serial() as ser:
    try:
        ser.baudrate = 19200
        ser.port = 'COM1'
        ser.open()
        ser.write(b'hello')
    except Exception as e:
        print(e)

print(ser.isOpen())
