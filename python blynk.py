import BlynkLib
import requests
from time import sleep, time
from sense_hat import SenseHat

BLYNK_AUTH = "vIe-sHHAze7o63Ijx6SyosR1HirGA8HZ"
THINGSPEAK_API_KEY = "J32W2TA52LC113HE"

TEMP_THRESHOLD = 30
HUMIDITY_THRESHOLD = 50

sense = SenseHat()
sense.clear()

blynk = BlynkLib.Blynk(BLYNK_AUTH)

@blynk.on("V1")
def handle_v1_write(value):
    button_value = value[0]
    print(f"Button: {button_value}")

    if button_value == "1":
        sense.clear(255, 255, 255)
    else:
        sense.clear()

if __name__ == "__main__":
    print("Blynk started...")

try:
        while True:
            blynk.run()

            temp = round(sense.get_temperature(), 2)
            humidity = round(sense.get_humidity(), 2)

            blynk.virtual_write(0, temp)
            blynk.virtual_write(2, humidity)

            print(f"Temp: {temp} C | Humidity: {humidity}%")

            url = f"https://api.thingspeak.com/update?api_key={THINGSPEAK_API_KEY}&field1={temp}&field2={humidity}"
            requests.get(url)


            if temp > TEMP_THRESHOLD:
                print("High temp detected!")
                blynk.log_event("HighTemp")

                for _ in range(3):
                    sense.clear(255, 0, 0)  # red
                    sleep(0.3)
                    sense.clear()
                    sleep(0.3)

            if humidity > HUMIDITY_THRESHOLD:
                print("High humidity detected!")
                blynk.log_event("HighHumidity")

                for _ in range(3):
                    sense.clear(0, 0, 255)  # blue
                    sleep(0.3)
                    sense.clear()
                    sleep(0.3)

            if temp <= TEMP_THRESHOLD and humidity <= HUMIDITY_THRESHOLD:
                sense.clear()


            sleep(15)

    except KeyboardInterrupt:
        print("Stopped")
        sense.clear()