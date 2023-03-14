from models import *

background = transform.scale(image.load("background.png"), WIN_SETTING)
clock = time.Clock()

font.init()
fontlabel = font.SysFont("Terminal", 32)

RED = (255,0,0)
GREEN = (0,255,0) 

player1_win = fontlabel.render('Player 1 won!', True, RED)
player2_win = fontlabel.render('Player 2 won!', True, GREEN)

r1 = Player(paddle_IMG, 0,0, 15, "left")
r2 = Player(transform.flip(paddle_IMG, True, False), WIN_SETTING[0]-SPSIZE[0],0, 15, "right")
ball = Ball()
game = True
finish = False
while game:
	window.blit(background, (0,0))
	if not finish:
		r1.update_position()
		r2.update_position()
		ball.draw()
		ball.move(r1,r2)
		if ball.rect.x == 0 or ball.rect.x == WIN_SETTING[0]-ball.rect.width:
			finish = True
	for e in event.get():
		if e.type == QUIT:
			game = False
	clock.tick(FPS)
	display.update()