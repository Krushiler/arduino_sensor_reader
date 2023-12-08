from app.domain.repository.arduino_repository import ArduinoRepository
from app.domain.repository.network_repository import NetworkRepository


class ArduinoInteractor:
    def __init__(self, arduino_repository: ArduinoRepository, network_repository: NetworkRepository):
        self._arduino_repository = arduino_repository
        self._network_repository = network_repository

    def start(self) -> None:
        self._arduino_repository.start()
        self._network_repository.start()
        self._arduino_repository.values().subscribe(lambda x: self._network_repository.send_event(x))
