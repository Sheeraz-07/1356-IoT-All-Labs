import BlynkLib as blynklib
import network
import utime as time
from machine import Pin
from neopixel import NeoPixel

# WiFi and Blynk Credentials
WIFI_SSID = "sherry"
WIFI_PASS = "connectedd"
BLYNK_AUTH = "gF_JPBxIqa6byyEHVFbAFYSlrptwj906"

# Connect to WiFi
print(f"Connecting to WiFi network '{WIFI_SSID}'...")
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASS)
while not wifi.isconnected():
    time.sleep(1)
    print('WiFi connect retry ...')
print('WiFi IP:', wifi.ifconfig()[0])

# Connect to Blynk
print("Connecting to Blynk server...")
blynk = blynklib.Blynk(BLYNK_AUTH)

# Initialize NeoPixel LED
pin = Pin(48, Pin.OUT)
np = NeoPixel(pin, 1)

# Function to set NeoPixel color
def set_color(r, g, b):
    np[0] = (r, g, b)
    np.write()
    print(f"✅ NeoPixel Updated -> R: {r}, G: {g}, B: {b}")

# Handle zeRGBa (Advanced Mode - V4)
@blynk.on("V4")
def v4_write_handler(value):
    print(f"📩 Received from zeRGBa: {value}")
    
    try:
        r, g, b = map(int, value[0].split(","))  # Convert "R,G,B" to integers
        set_color(r, g, b)
    except Exception as e:
        print(f"⚠ Error parsing zeRGBa data: {e}")

# Blynk Handlers
@blynk.on("connected")
def blynk_connected():
    print("✅ Blynk Connected!")
    blynk.sync_virtual(4)  # Sync zeRGBa data

@blynk.on("disconnected")
def blynk_disconnected():
    print("❌ Blynk Disconnected!")

# Main Loop
while True:
    blynk.run()
