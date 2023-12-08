import zmq

context = zmq.Context()

client = context.socket(zmq.SUB)
client.connect("tcp://127.0.0.1:5555")
client.subscribe('')

while True:
    message = client.recv_string()
    print(f"Received event: {message}")
