import argparse

from app.core.app_config import AppConfig
from app.di.di import Di

import logging


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=5555)
    return parser.parse_args()

def setup_logger():
    logging.basicConfig(filename='sensor.log', 
                        encoding='utf-8', 
                        level=logging.CRITICAL,
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:S %p')

def main():
    setup_logger()
    try:
        args = parse_args()
        AppConfig.port = args.port
        di = Di()
        arduino_interactor = di.provide_arduino_interactor()
        arduino_interactor.start()
    except Exception as e:
        logging.critical(str(e))
    except KeyboardInterrupt as e:
        logging.critical("Stopped with keyboard interrupt")


if __name__ == '__main__':
    main()
