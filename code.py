import board
import digitalio
import pwmio
from adafruit_motor import servo
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
from adafruit_bluefruit_connect.packet import Packet
from adafruit_bluefruit_connect.button_packet import ButtonPacket

ble = BLERadio()
uart_service = UARTService()
advertisement = ProvideServicesAdvertisement(uart_service)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

pwm1 = pwmio.PWMOut(board.GP16, duty_cycle=2 ** 15, frequency=50)
servo1 = servo.Servo(pwm1, min_pulse=500, max_pulse=2500)

pwm2 = pwmio.PWMOut(board.GP17, duty_cycle=2 ** 15, frequency=50)
servo2 = servo.Servo(pwm2, min_pulse=500, max_pulse=2500)

while True:
    ble.start_advertising(advertisement)

    while not ble.connected:
        pass

    while ble.connected:
        if uart_service.in_waiting:
            packet = Packet.from_stream(uart_service)
            if isinstance(packet, ButtonPacket):
                if packet.pressed:
                    if packet.button == ButtonPacket.UP:
                        led.value = True
                        servo1.angle = 90
                        servo2.angle = 90
                    elif packet.button == ButtonPacket.DOWN:
                        led.value = False
                        servo1.angle = 0
                        servo2.angle = 0
    # led.value = True
    # servo1.angle = 0
    # servo2.angle = 0
    # time.sleep(1.0)

    # led.value = False
    # servo1.angle = 180
    # servo2.angle = 180
    # time.sleep(1.0)

