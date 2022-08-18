import pygame, time

pygame.init()

screen = pygame.display.set_mode([720, 750])
image = pygame.image.load("196190_hav_None.png").convert()
ship_1x2 = pygame.image.load("1x2_boat_better_call_saul.png").convert_alpha()
ship_1x2_pos: int
ship_1x2_in_view = False

saul_knapp = pygame.image.load("Saul_knapp.png").convert()
print((saul_knapp.get_width(),saul_knapp.get_height()))
saul_knapp = pygame.transform.scale(saul_knapp,(saul_knapp.get_width()*0.66,saul_knapp.get_height()*0.66))
print((saul_knapp.get_width(),saul_knapp.get_height()))

current_ship = "None"
invalid_placement = pygame.image.load("Ugyldig_plassering.png").convert_alpha()
fail_time: float
failed = False
while True:
    screen.fill((90,90,90))
    
    #Creates the grid
    for i in range(0,screen.get_width(),72):
        for j in range(0,screen.get_height()-30,72):
            screen.blit(image,(i,j))
    #Get events
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            if pygame.mouse.get_pos()[1] > 648 and pygame.mouse.get_pos()[0] > 10 and pygame.mouse.get_pos()[0] < 10+saul_knapp.get_width():
                current_ship = "Saul"
            elif current_ship == "Saul" and pygame.mouse.get_pos()[1] < screen.get_height()-30:
                ship_1x2_pos = pygame.mouse.get_pos()
                ship_1x2_in_view = True
            elif current_ship == "Saul" and pygame.mouse.get_pos()[1] > screen.get_height()-30:
                fail_time = time.time()
                failed = True
    
    #Code for drawing Saul ship
    if ship_1x2_in_view:
        for i in range(0,screen.get_width()+72,72):
            for j in range(0,screen.get_height()-30,72):
                if ship_1x2_pos[0] < i and ship_1x2_pos[1] < j:
                    screen.blit(ship_1x2,(i-72,j-72))
                    break
            if ship_1x2_pos[0] < i:
                break
    screen.blit(saul_knapp,(10,screen.get_height()-saul_knapp.get_height()))

    if failed and time.time() - fail_time < 1.5:
        screen.blit(invalid_placement,(screen.get_width()/2-72,screen.get_height()/2-72))
    elif failed:
        failed = False
    pygame.display.update()
