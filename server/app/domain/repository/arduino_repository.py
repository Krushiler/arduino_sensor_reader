from typing import Protocol

import reactivex as rx


class ArduinoRepository(Protocol):
    def start(self) -> None:
        pass

    def values(self) -> rx.abc.ObservableBase:
        pass
