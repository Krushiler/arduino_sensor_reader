from typing import Protocol


class NetworkRepository(Protocol):
    def send_event(self, event: str) -> None:
        pass
