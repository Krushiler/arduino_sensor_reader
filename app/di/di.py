from app.data.arduino.serial_reader import SerialReader
from app.data.repository.arduino_repository import ArduinoRepositoryImpl
from app.data.repository.mock.arduino_mock_repository import ArduinoMockRepositoryImpl
from app.data.repository.network_repository import NetworkRepositoryImpl
from app.di.di_utils import lazy_singleton, provides
from app.domain.interactor.arduino_interactor import ArduinoInteractor
from app.domain.repository.arduino_repository import ArduinoRepository
from app.domain.repository.network_repository import NetworkRepository


class Di:
    @lazy_singleton
    def provide_serial_reader(self) -> SerialReader:
        return SerialReader()

    @lazy_singleton
    def provide_arduino_repository(self) -> ArduinoRepository:
        return ArduinoRepositoryImpl(self.provide_serial_reader())

    @lazy_singleton
    def provide_arduino_mock_repository(self) -> ArduinoRepository:
        return ArduinoMockRepositoryImpl()

    @lazy_singleton
    def provide_network_repository(self) -> NetworkRepository:
        return NetworkRepositoryImpl()

    @provides
    def provide_arduino_interactor(self) -> ArduinoInteractor:
        return ArduinoInteractor(self.provide_arduino_repository(), self.provide_network_repository())
