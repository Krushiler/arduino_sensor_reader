import threading
import time

import reactivex as rx


class ArduinoMockRepositoryImpl:
    def __init__(self):
        self._serial_thread = None
        self._values = rx.subject.Subject()

    def _emit_values(self):
        while True:
            self._values.on_next("p 100")
            time.sleep(1)

    def start(self) -> None:
        self._serial_thread = threading.Thread(target=self._emit_values)
        self._serial_thread.start()

    def values(self) -> rx.abc.ObservableBase:
        return self._values
