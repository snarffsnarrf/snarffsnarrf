import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
red_pwm = GPIO.PWM(11, 50)
blu_pwm = GPIO.PWM(13, 50)
command = ""
started = False

while True:
    command = input(">>> ").lower()
    if command == "low":
        red_pwm.start(2)
        blu_pwm.start(2)
    if command == "high":
        red_pwm.start(100)
        blu_pwm.start(100)
    if command == "left":
        red_pwm.start(0)
        blu_pwm.start(100)
    if command == "right":
        red_pwm.start(100)
        blu_pwm.start(0)
    if command == "cop":
        i = 1
        d = 5
        while i <= 50/d: # i <= 5 is 1 second
            red_pwm.start(0)
            blu_pwm.start(100)
            time.sleep(.1)
            red_pwm.start(100)
            blu_pwm.start(0)
            time.sleep(.1)
            i = i + 1
        red_pwm.start(2)
        blu_pwm.start(2)
    elif command == "quit":
        red_pwm.start(0)
        blu_pwm.start(0)
        break

GPIO.cleanup()
