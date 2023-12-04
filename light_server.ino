int photo_pin = A0;
int touch_pin = 2;
int magnet_pin = 3;

string welcome_message = "Clown";

void setup() {
  Serial.begin(9600);
  pinMode(photo_pin, INPUT);
  pinMode(touch_pin, INPUT);
  pinMode(magnet_pin, INPUT);
}

int photo_delay = 1000;
int prev_photo_time = 0;

int debounce_time = 500;
int prev_magnet_debounce_time = 0;
int prev_touch_data = 0;

int magnet_debounce_time = 500;
int prev_debounce_time = 0;
int prev_magnet_data = 0;

void loop() {
  int touch_data = digitalRead(touch_pin);
  int magnet_data = digitalRead(magnet_pin);

  int currentTime = millis();

  if (currentTime - prev_photo_time > photo_delay) {
    int photo_data = analogRead(photo_pin);
    prev_photo_time = currentTime;
    Serial.print("p ");
    Serial.println(photo_data);
  }

  if (touch_data > 0 && prev_touch_data == 0) {
    if (currentTime - prev_debounce_time > debounce_time) {
      prev_debounce_time = currentTime;
      Serial.println("t");
    } else {
      touch_data = 0;
    }
  }

  if (magnet_data > 0 && prev_magnet_data == 0) {
    if (currentTime - prev_magnet_debounce_time> magnet_debounce_time) {
      prev_magnet_debounce_time = currentTime;
      Serial.println("m");
    } else {
      magnet_data = 0;
    }
  }

  prev_touch_data = touch_data;
  prev_magnet_data = magnet_data;
}
