print("Amanda Clevenger")
print("11/01/2024")
print("Slide and Catch game part 1")

import pygame, simpleGE, random

class Worm(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Worm.png")
        self.setSize(30, 30)
        self.minSpeed = 3
        self.maxSpeed = 8
        self.reset()
        
    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(self.minSpeed, self.maxSpeed)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()


class Fish(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Fish.png")
        self.setSize(90, 110)
        self.position = (320, 400)
        self.moveSpeed = 5
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -=self.moveSpeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x +=self.moveSpeed
        
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("Ocean.png")
        self.sndWorm = simpleGE.Sound("Bubble.mp3")
        self.fish = Fish(self)
        self.numWorms = 10
        self.worms = []
        for i in range(self.numWorms):
            self.worms.append(Worm(self))
            
        self.sprites = [self.fish,
                        self.worms]
        
    def process(self):
        for worm in self.worms:
            if worm.collidesWith(self.fish):
                self.sndWorm.play()
                worm.reset()
        
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()