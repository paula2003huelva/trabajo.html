import pygame

pygame.init()

#Establecemos unas constantes para los colores(RGB)

ROJO=[255, 0, 0]
AZUL=[0,0,255]
VERDE=[0,255,0]
NEGRO = (0, 0 ,0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VIOLETA = (98, 0, 255)
  

dimensiones=[500,500]

#Creamos el espacio donde visualizar.
pantalla=pygame.display.set_mode(dimensiones)

#Le damos un título a la ventana
pygame.display.set_caption('Rebotamos')

hecho = False
 
# Se usa para establecer cuan rápido se actualiza la pantalla
 
reloj = pygame.time.Clock()
rectx=25
recty=10
rectcambiox=3
rectcambioy=2


while not hecho:
    # --- Bucle principal de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
    for evento in pygame.event.get():
         if evento.type == pygame.QUIT: 
            hecho = True
    # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ
  
    # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ
     
    # Primero, limpia la pantalla con blanco. No vayas a poner otros comandos de dibujo encima 
    # de esto, de otra forma serán borrados por este comando:
    pantalla.fill(NEGRO)
    pygame.draw.rect(pantalla, BLANCO, [rectx,recty,50,50])
    rectx+=rectcambiox
    recty+=rectcambioy
    pygame.draw.rect(pantalla, VIOLETA, [rectx,recty,50,50])
    rectx +=rectcambiox
    recty +=rectcambioy
   
   
    if rectx>450 or rectx<0:
        rectcambiox=rectcambiox*-1
    if recty>450 or recty<0:
        rectcambioy=rectcambioy*-1
     
    # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
    pygame.display.flip()
    
    # --- Limitamos a 60 fotogramas por segundo (frames per second)
    reloj.tick(60)
     
# Cerramos la ventana y salimos.
# Si te olvidas de esta última línea, el programa se 'colgará'
# al salir si lo hemos estado ejecutando desde el IDLE.
pygame.quit()



