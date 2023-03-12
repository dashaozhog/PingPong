from pygame import *

WIN_SETTING = (1800,1000)
FPS = 60
window = display.set_mode(WIN_SETTING)
SPSIZE = (100, 300)
paddle_IMG = transform.scale(image.load("paddle.png"), SPSIZE)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, typee):
        super().__init__()
        self.image = player_image
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.typee = typee
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_position(self):
        keys = key.get_pressed()
        if self.typee == "left":
            if keys[K_w]:
                self.rect.y -= self.speed
            if keys[K_s]:
                self.rect.y += self.speed
        if self.typee == "right":
            if keys[K_UP] :
                self.rect.y -= self.speed
            if keys[K_DOWN]:

                self.rect.y += self.speed

        self.reset()