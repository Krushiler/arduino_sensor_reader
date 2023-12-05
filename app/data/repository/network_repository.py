class NetworkRepositoryImpl:
    def __init__(self):
        pass

    def send_event(self, event: str) -> None:
        print(f'Sending event: {event}')
