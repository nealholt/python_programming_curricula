class Sprite:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

