import sys
import os
import pygame as pg

os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"

planetname = 'Mizumi'
planetNewsFile = planetname +'News.txt'
planetBackgroundFile = 'SystemAtopie.png'


pg.init()
screen = pg.display.set_mode((1600, 900), pg.NOFRAME)
pg.display.set_caption(planetname)
screen_rect = screen.get_rect()
clock = pg.time.Clock()

background = pg.image.load(planetBackgroundFile).convert()


news = ''
with open(planetNewsFile) as inputfile:
	for line in inputfile:
		news+= '   +++   '+line.strip('\n')
		
font = pg.font.Font(None, 48)
rendered_text = font.render(news, True, pg.Color("white"))
text_rect = rendered_text.get_rect(midleft=(900, screen_rect.bottom-40))  
textwidth = text_rect.width 

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    
    if text_rect.midright > screen_rect.midleft:
        #print(text_rect.centerx)
        text_rect.move_ip(-5, 0)  
    else: 
        text_rect.move_ip(text_rect.width + screen_rect.width, 0)
    screen.blit(background, (0,0))
    #screen.fill(pg.Color("gray5"))
    screen.blit(rendered_text, text_rect)

    pg.display.update()
    clock.tick(60)

pg.quit()
sys.exit()