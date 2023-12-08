import re
import time

import reactivex as rx
import serial
from serial.tools import list_ports


class SerialReader:
    def __init__(self):
        self._ser = None
        self._values = rx.subject.Subject()

    def values(self) -> rx.abc.ObservableBase:
        return self._values

    def start(self):
        while True:
            self._find_serial_port_infinite()
            self._listen_output()

    def _listen_output(self):
        print("Listening for output")
        while self._ser is not None:
            try:
                self._consume_output()
            except serial.SerialException:
                self._ser = None

    def _consume_output(self):
        line = self._ser.readline().decode("utf-8")
        line = re.sub("\r\n", "", line)
        self._values.on_next(line)

    def _find_serial_port_infinite(self):
        while self._ser is None:
            print("Searching for arduino port")
            self._find_serial_port()
            time.sleep(0.1)

    def _find_serial_port(self):
        self._ser = None
        serial_ports = list_ports.comports()
        for serial_port in serial_ports:
            try:
                print(serial_port.name)
                self._ser = serial.Serial(serial_port.name, 9600)
                self._ser.write(b"wlc")
                time.sleep(1)
                line = self._ser.read_all().decode("utf-8")
                if "wlc" not in line:
                    print("Port found")
                    return
                else:
                    self._ser = None
            except serial.SerialException:
                continue
            except ValueError:
                continue
