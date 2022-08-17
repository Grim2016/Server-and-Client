import pygame

pygame.init()

screen = pygame.display.set_mode([720, 750])
image = pygame.image.load("196190_hav_None.png").convert()
ship_1x2 = pygame.image.load("1x2_boat_better_call_saul.png").convert_alpha()
ship_1x2_pos: int
ship_1x2_in_view = False
possible_possitions = []
current_ship = "Saul"
while True:
    screen.fill((90,90,90))
    
    #Creates the grid
    for i in range(0,screen.get_width(),72):
        for j in range(0,screen.get_height()-30,72):
            screen.blit(image,(i,j))
    #Get events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            if current_ship == "Saul":
                ship_1x2_pos = pygame.mouse.get_pos()
                ship_1x2_in_view = True
    
    #Code for drawing Saul ship
    if ship_1x2_in_view:
        for i in range(0,screen.get_width()+72,72):
            for j in range(0,screen.get_height()-30,72):
                if ship_1x2_pos[0] < i and ship_1x2_pos[1] < j:
                    screen.blit(ship_1x2,(i-72,j-72))
                    break
            if ship_1x2_pos[0] < i:
                break
    pygame.display.update()
