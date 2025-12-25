import board
import time
import digitalio
import pwmio
from adafruit_motor import servo

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

pwm = pwmio.PWMOut(board.GP16, duty_cycle=2 ** 15, frequency=50)
moje_servo = servo.Servo(pwm)

while True:
    led.value = True
    moje_servo.angle = 0
    print("Kąt: 0")
    time.sleep(1.0)

    led.value = False
    moje_servo.angle = 180
    print("Kąt: 180")
    time.sleep(1.0)

