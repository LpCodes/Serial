# Check what serial ports are available on your machine


from serial.tools import list_ports
c = list_ports.comports()  # Outputs list of available serial ports

print(c)

