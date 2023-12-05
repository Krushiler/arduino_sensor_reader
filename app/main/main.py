from app.di.di import Di

if __name__ == '__main__':
    di = Di()
    arduino_interactor = di.provide_arduino_interactor()
    arduino_interactor.start()
