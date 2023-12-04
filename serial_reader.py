import time

import serial


def find_serial_port():
    ser = None
    serial_ports = serial.tools.list_ports.comports()
    for serial_port in serial_ports:
        try:
            ser = serial.Serial(serial_port, 9600)
            ser.write(b"Clown")
        except serial.SerialException:
            continue
    return ser


def create_serial_port():
    try:
        return serial.Serial('COM11', 9600)
    except serial.SerialException:
        return None


def consume_output(ser: serial.Serial):
    if ser is None:
        raise serial.SerialException("No serial port")
    print(ser.readline())


ser = None

while True:
    try:
        consume_output(ser)
    except serial.SerialException:
        ser = create_serial_port()
        print("Reopening")
        time.sleep(0.1)
