import argparse

from app.core.app_config import AppConfig
from app.di.di import Di


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=5555)
    return parser.parse_args()


def main():
    args = parse_args()
    AppConfig.port = args.port
    di = Di()
    arduino_interactor = di.provide_arduino_interactor()
    arduino_interactor.start()


if __name__ == '__main__':
    main()
