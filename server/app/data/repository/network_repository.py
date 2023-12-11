import zmq

from app.core.app_config import AppConfig


class NetworkRepositoryImpl:
    def __init__(self):
        self._context = zmq.Context()
        self._socket = None

    def start(self) -> None:
        self._socket = self._context.socket(zmq.PUB)
        port = AppConfig.port
        self._socket.bind(f"tcp://*:{port}")

    def send_event(self, event: str) -> None:
        print(f"Sending event: {event}")
        self._socket.send_string(event)
