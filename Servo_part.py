import machine
p4 = machine.Pin(14)
servo = machine.PWM(p4,freq=50)
# duty for servo is between 40 - 115
servo.duty(100)