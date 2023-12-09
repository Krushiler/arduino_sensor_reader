int photo_pin = A0;
int touch_pin = 2;
int magnet_pin = 3;

class Timer {
  private:
    int _delay;
    int _time;
  public:
    Timer(int delay) {
      _delay = delay;
      _time = 0;
    }

    bool tick() {
      int currentTime = millis();
      if (currentTime - _time >= _delay) {
        _time = currentTime;
        return true;
      }
      return false;
    }
};

void setup() {
  Serial.begin(9600);
  pinMode(photo_pin, INPUT);
  pinMode(touch_pin, INPUT);
  pinMode(magnet_pin, INPUT);
}

Timer photo_timer(1000);
Timer touch_timer(500);
Timer magnet_timer(500);

int prev_touch_data = 0;
int prev_magnet_data = 0;

String welcome_message = "w3lc0m3blya";

void listen_welcome() {
  if (Serial.available() > 0) {
    String message = Serial.readString();
    Serial.println(welcome_message);
    if (message == welcome_message) {
    }
  }
}

void loop() {
  listen_welcome();

  int touch_data = digitalRead(touch_pin);
  int magnet_data = digitalRead(magnet_pin);

  if (photo_timer.tick()) {
    int photo_data = analogRead(photo_pin);
    Serial.print("p ");
    Serial.println(photo_data);
  }

  if (touch_data > 0 && prev_touch_data == 0) {
    if (touch_timer.tick()) {
      Serial.println("t");
    } else {
      touch_data = 0;
    }
  }

  if (magnet_data > 0 && prev_magnet_data == 0) {
    if (magnet_timer.tick()) {
      Serial.println("m");
    } else {
      magnet_data = 0;
    }
  }

  prev_touch_data = touch_data;
  prev_magnet_data = magnet_data;
}
