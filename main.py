import pyb



class Motor:
    pin = None
    timer = None
    channel = None

    pins = ((pyb.Pin.board.X1, 5, 1),
            (pyb.Pin.board.X2, 5, 2),
            (pyb.Pin.board.X3, 9, 1),
            (pyb.Pin.board.X4, 9, 2),
            (pyb.Pin.board.X6, 2, 1),
            (pyb.Pin.board.X7, 13, 1),
            (pyb.Pin.board.X8, 14, 1),
            (pyb.Pin.board.Y9, 2, 3),
            (pyb.Pin.board.Y10, 2, 4),
            (pyb.Pin.board.X10, 4, 2))

    def __init__(self, i):
        self.pin = self.pins[i][0]
        self.timer = pyb.Timer(self.pins[i][1], freq=50)
        self.channel = self.timer.channel(self.pins[i][2], pyb.Timer.PWM, pin=self.pin, pulse_width=0)
        self.motor_on_percent(self.freq_to_percent(1500))

    def motor_on_percent(self, percent):
        self.channel.pulse_width_percent(percent)

    def freq_to_percent(self, frequency):
        return frequency * 7.5 / 1500

    def percent_to_percent(self, percent):
        frequency = 1500 + (500 * percent / 100)
        return self.freq_to_percent(frequency)

    def motor_on_frequency(self, frequency):
        self.channel.pulse_width_percent(self.freq_to_percent(frequency))


led1 = pyb.LED(1)
led2 = pyb.LED(2)
led3 = pyb.LED(3)

led1.on()

motors = []
for i in range(10):
    led2.toggle()
    motors.append(Motor(i))
pyb.delay(7000)

led1.off()
while True:
    motors[0].motor_on_percent(8.5)
    led3.toggle()
