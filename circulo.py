import pygame
pygame.init()
dimensiones=(400,500)
pantalla=pygame.display.set_mode(dimensiones)
BLANCO=[255,255,255]
NEGRO=[0,0,0]
hecho=False
reloj=pygame.time.Clock()
x_coord=10
y_coord=10
desplazamiento_en_x=0
desplazamiento_en_y=0
def elipse(pantalla,x,y):
    pygame.draw.ellipse(pantalla,NEGRO,[x,y,50,20],0)
while not hecho:
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            hecho=True
        elif evento.type==pygame.KEYDOWN:

            if evento.key==pygame.K_LEFT:
                desplazamiento_en_x=-3
            elif evento.key==pygame.K_RIGHT:
                desplazamiento_en_x=3
            elif evento.key==pygame.K_UP:
                desplazamiento_en_y=-3
            elif evento.key==pygame.K_DOWN:
                desplazamiento_en_y=3

        elif evento.type==pygame.KEYUP:
            if evento.key==pygame.K_LEFT:
                desplazamiento_en_x=0
            elif evento.key==pygame.K_RIGHT:
                desplazamiento_en_x=0
            elif evento.key==pygame.K_UP:
                desplazamiento_en_y=0
            elif evento.key==pygame.K_DOWN:
                desplazamiento_en_y=0

    
                
    x_coord+=desplazamiento_en_x
    y_coord+=desplazamiento_en_y
    pantalla.fill(BLANCO)
    elipse(pantalla,x_coord,y_coord)
    pygame.display.flip()
    reloj.tick(60)
pygame.quit()
