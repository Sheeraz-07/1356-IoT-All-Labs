import network
import time
import BlynkLib
import dht
from machine import Pin, I2C
import ssd1306
import neopixel

# ---- USER SETTINGS ----
#WIFI_SSID = "Acccio Internet"
#WIFI_PASS = "P@SSSWORD"
WIFI_SSID = "sherry"
WIFI_PASS = "connectedd"
BLYNK_AUTH = "ZFnH1GoseLH-JlrJW1Ce2KaxSOHcDwhG"

# ---- CONNECT TO WIFI ----
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("🔄 Connecting to WiFi...")
        wlan.connect(WIFI_SSID, WIFI_PASS)
        while not wlan.isconnected():
            pass
    print("✅ Connected to WiFi:", wlan.ifconfig())

connect_wifi()

# ---- INITIALIZE BLYNK ----
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# ---- INITIALIZE DHT SENSOR ----
dht_sensor = dht.DHT11(Pin(4))

# ---- INITIALIZE OLED DISPLAY ----
i2c = I2C(0, scl=Pin(9), sda=Pin(8))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)

# ---- INITIALIZE NeoPixel LED ----
NUM_PIXELS = 1  
neo_pin = Pin(48, Pin.OUT)
np = neopixel.NeoPixel(neo_pin, NUM_PIXELS)

# ---- INITIAL RGB VALUES ----
red_value, green_value, blue_value = 0, 0, 0
rgb_enabled = True

# ---- FUNCTION TO UPDATE NeoPixel COLOR ----
def update_rgb():
    if rgb_enabled:
        np[0] = (red_value, green_value, blue_value)
    else:
        np[0] = (0, 0, 0)  # Turn off LED
    np.write()
    print(f"NeoPixel Updated -> R:{red_value}, G:{green_value}, B:{blue_value}, Status:{'ON' if rgb_enabled else 'OFF'}")

# ---- BLYNK HANDLERS ----
@blynk.on("V2")  # Red Slider
def red_handler(value):
    global red_value
    red_value = int(value[0])
    update_rgb()

@blynk.on("V3")  # Green Slider
def green_handler(value):
    global green_value
    green_value = int(value[0])
    update_rgb()

@blynk.on("V4")  # Blue Slider
def blue_handler(value):
    global blue_value
    blue_value = int(value[0])
    update_rgb()

@blynk.on("V5")  # Button for ON/OFF
def led_handler(value):
    global rgb_enabled
    rgb_enabled = bool(int(value[0]))  # 1 = ON, 0 = OFF
    update_rgb()

# ---- FUNCTION TO SEND SENSOR DATA ----
def send_sensor_data():
    try:
        dht_sensor.measure()
        time.sleep(1)
        temp = dht_sensor.temperature()
        humid = dht_sensor.humidity()
        print(f"🌡 Temp: {temp:.2f}°C | 💧 Humidity: {humid:.2f}%")
        oled.fill(0)
        oled.text(f"Temp: {temp} C", 10, 16)
        oled.text(f"Humidity: {humid} %", 10, 32)
        oled.show()
        blynk.virtual_write(0, round(temp, 2))
        blynk.virtual_write(1, round(humid, 2))
    except OSError as e:
        print(f"⚠ Sensor Error: {e}")

# ---- MAIN LOOP ----
while True:
    blynk.run()
    send_sensor_data()
    time.sleep(5)
