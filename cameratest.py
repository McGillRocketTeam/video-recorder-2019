import picamera
import time
import board
import busio
import adafruit_bmp280

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
bmp280.sea_level_pressure = 1013.25

# Camera
camera = picamera.PiCamera()
camera.resolution = (1640, 922)
camera.framerate = 24
camera.start_preview()
camera.annotate_background = False

camera.start_recording('testing_BMP_1.h264')

while True:
    string = 'T:' + str(round(bmp280.temperature, 1)) + ' P:' + str(round(bmp280.pressure, 1)) + ' A:' + str(round(bmp280.altitude, 1))
    camera.annotate_text = string
    camera.wait_recording(3)
#camera.wait_recording(10)
camera.stop_recording()
