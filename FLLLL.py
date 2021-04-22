import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
red_pwm = GPIO.PWM(11, 100)
blu_pwm = GPIO.PWM(13, 100)

red_pwm.start(50)
blu_pwm.start(50)