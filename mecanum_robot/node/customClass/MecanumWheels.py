from gpiozero import Motor

class MecanumWheels():

    def __init__(self, wheel_pins):
        print("Mecanum Wheel constructed")
        self.rf = Motor(wheel_pins[0][0], wheel_pins[0][1])
        self.rb = Motor(wheel_pins[1][0], wheel_pins[1][1])
        self.lf = Motor(wheel_pins[2][0], wheel_pins[2][1])
        self.lb = Motor(wheel_pins[3][0], wheel_pins[3][1])
    
    def _calcParam(self, direction, pwm):
        a = 0
        b = 0
        d = direction * 4
        if direction > -0.5 and direction <= 0: # Right Forward
            a = d + 1
            b = 1
        elif direction > -1 and direction <= -0.5: # Right Backward
            a = -1
            b = d + 3
        elif direction > 0 and direction <= 0.5: # Left Forward
            a = 1
            b = -d + 1
        elif direction > 0.5 and direction <= 1: # Left Backward
            a = -d + 3
            b = -1
        else:
            print('direction value range must be (-1, 1]')

        a = a * pwm
        b = b * pwm
        return a, b

    def _motorMove(self, motor, param):
        if param >= 0:
            motor.forward(param)
        else:
            motor.backward(-param)
    
    def normalMove(self, direciton=0, pwm=1):
        a, b = self._calcParam(direciton, pwm)
        self._motorMove(self.rf, a)
        self._motorMove(self.rb, a)
        self._motorMove(self.lf, b)
        self._motorMove(self.lb, b)

    def parallelMove(self, direciton=0, pwm=1):
        a, b = self._calcParam(direciton, pwm)
        self._motorMove(self.rf, a)
        self._motorMove(self.rb, b)
        self._motorMove(self.lf, b)
        self._motorMove(self.lb, a)

    def stop(self):
        self.rf.stop()
        self.rb.stop()
        self.lf.stop()
        self.lb.stop()

    def forward(self, pwm=1):
        self.rf.forward(pwm)
        self.rb.forward(pwm)
        self.lf.forward(pwm)
        self.lb.forward(pwm)

    def backward(self, pwm=1):
        self.rf.backward(pwm)
        self.rb.backward(pwm)
        self.lf.backward(pwm)
        self.lb.backward(pwm)

    def rotateRight(self, pwm=1):
        self.rf.backward(pwm)
        self.rb.backward(pwm)
        self.lf.forward(pwm)
        self.lb.forward(pwm)

    def rotateLeft(self, pwm=1):
        self.rf.forward(pwm)
        self.rb.forward(pwm)
        self.lf.backward(pwm)
        self.lb.backward(pwm)

    def parallelRight(self, pwm=1):
        self.rf.backward(pwm)
        self.rb.forward(pwm)
        self.lf.forward(pwm)
        self.lb.backward(pwm)
    
    def parallelLeft(self, pwm=1):
        self.rf.forward(pwm)
        self.rb.backward(pwm)
        self.lf.backward(pwm)
        self.lb.forward(pwm)

    def parallelForwardRight(self, pwm=1):
        self.rf.forward(pwm)
        self.rb.stop()
        self.lf.stop()
        self.lb.forward(pwm)

    def parallelBackwardRight(self, pwm=1):
        self.rf.backward(pwm)
        self.rb.stop()
        self.lf.stop()
        self.lb.backward(pwm)

    def parallelForwardLeft(self, pwm=1):
        self.rf.stop()
        self.rb.backward(pwm)
        self.lf.backward(pwm)
        self.lb.stop()

    def parallelBackwardLeft(self, pwm=1):
        self.rf.stop()
        self.rb.backward(pwm)
        self.lf.backward(pwm)
        self.lb.stop()


    
