import time
import RPi.GPIO as GPIO


### function to operate servo by specifying an angle
def setservo(angle):
    angle = (0.5 + (1.9 / 180) * angle) / 20 * 100
    servo.ChangeDutyCycle(angle)
    time.sleep(1)

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)

### case : user input data
print("speciflying the angle")
angle = input()

for i in range(3):
    servo.ChangeDutyCycle(2.5)
    time.sleep(1)
    setservo(angle)

GPIO.cleanup()
