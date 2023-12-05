from arduino.serial_reader import SerialReader
import threading

if __name__ == '__main__':
    serial_reader = SerialReader()
    serial_reader.values().subscribe(lambda x: print(x))
    serial_thread = threading.Thread(target=serial_reader.start)
    serial_thread.start()
