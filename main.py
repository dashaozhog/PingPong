from models import *

background = transform.scale(image.load("background.png"), WIN_SETTING)
clock = time.Clock()


r1 = Player(paddle_IMG, 0,0, 10, "left")
r2 = Player(transform.flip(paddle_IMG, True, False), WIN_SETTING[0]-SPSIZE[0],0, 10, "right")
game = True
while game:
	window.blit(background, (0,0))
	r1.update_position()
	r2.update_position()
	for e in event.get():
		if e.type == QUIT:
			game = False
	clock.tick(FPS)
	display.update()