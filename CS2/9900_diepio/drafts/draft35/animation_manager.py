import sparkle, random

class AnimationManager:
    def __init__(self):
        self.animations = []

    def update(self):
        for i in reversed(range(len(self.animations))):
            self.animations[i].update()
            if self.animations[i].hit_points <= 0:
                del self.animations[i]

    def draw(self, povx, povy, center_on_screen=False):
        for a in self.animations:
            a.draw(povx, povy, center_on_screen=False)

    def addSpark(self, screen, x, y):
        randcolor = random.randint(0,255),random.randint(0,255),random.randint(0,255)
        temp = sparkle.Sparkle(screen, x+random.randint(-100,100),
                    y+random.randint(-100,100), randcolor)
        self.animations.append(temp)
