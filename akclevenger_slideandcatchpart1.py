import pygame, random, simpleGE


class Worm(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Worm.png")
        self.setSize(25, 25)
        self.reset()
        
    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(3, 8)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()

class Fish(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Fish.png")
        self.setSize(50, 50)
        self.position = (320, 400)
        self.moveSpeed = 5
    
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed        

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("Ocean.png")
        
        self.sndWorm = simpleGE.Sound("worm.png")
        
        self.fish = Fish(self)
        self.worm = Worm(self)
        
        self.sprites = [self.fish,
                        self.worm]
        
    def process(self):
        if self.fish.collidesWith(self.worm):
            self.sndWorm.play()
            self.worm.reset()
    
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()