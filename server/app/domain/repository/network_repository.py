from typing import Protocol


class NetworkRepository(Protocol):
    def start(self) -> None:
        pass

    def send_event(self, event: str) -> None:
        pass
