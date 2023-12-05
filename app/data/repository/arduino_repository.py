import threading

from app.data.arduino.serial_reader import SerialReader
import reactivex as rx


class ArduinoRepositoryImpl:
    def __init__(self, serial_reader: SerialReader):
        self._serial_reader = serial_reader
        self._serial_thread = None

    def start(self) -> None:
        self._serial_thread = threading.Thread(target=self._serial_reader.start)
        self._serial_thread.start()

    def values(self) -> rx.abc.ObservableBase:
        return self._serial_reader.values()
