import car, math

class CarBallistic(car.Car):
    def __init__(self, screen, x, y, friction, acceleration):
        super().__init__(screen, x, y)
        self.dx = 0
        self.dy = 0
        self.friction = friction
        self.acceleration = acceleration

    def accelerate(self):
        self.dx += math.cos(self.angle)*self.acceleration
        self.dy += math.sin(self.angle)*self.acceleration

    def brake(self):
        self.dx = max(0,self.dx-math.cos(self.angle)*self.acceleration)
        self.dy = max(0,self.dy-math.sin(self.angle)*self.acceleration)

    def moveForward(self):
        self.x += self.dx
        self.y += self.dy
        self.dx = (1-self.friction)*self.dx
        self.dy = (1-self.friction)*self.dy
