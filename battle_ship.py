import pygame, time

pygame.init()

screen = pygame.display.set_mode([720, 750])
image = pygame.image.load("196190_hav_None.png").convert()

class Ship:
    def __init__(self, image: str, length: int, screen: pygame.Surface, name: str="None",) -> None:
        self.image: pygame.Surface = pygame.image.load(image).convert_alpha()
        self.pos: int
        self.in_view: bool = False
        self.length: int = length
        self.name: str = name
        self.screen: pygame.Surface = screen
    def drawShip(self):
        if self.in_view:
            for i in range(0,self.screen.get_width()+72,72):
                for j in range(0,self.screen.get_height()-30,72):
                    if self.pos[0] < i and self.pos[1] < j:
                        self.screen.blit(self.image,(i-72,j-72))
                        break
                if self.pos[0] < i:
                    break

class Ship_button:
    def __init__(self,x: int, y: int, image: str, ship: Ship, size_mod: int=0.66, incr: int=10) -> None:
        self.x: int = x
        self.y: int = y
        self.image: pygame.Surface = pygame.image.load(image).convert_alpha()
        self.ship = ship
        self.image = pygame.transform.scale(self.image,(self.image.get_width()*size_mod,self.image.get_height()*size_mod))
        self.next_x: int = self.x + self.image.get_width() +incr
    def inside_button(self, click_pos: tuple) -> bool:
        #return click_pos[0] < self.x + self.image.get_width() and self.x < click_pos[0] and click_pos[1] < self.y + self.image.get_height() and self.y < click_pos[1]
        if click_pos[0] < self.x + self.image.get_width() and self.x < click_pos[0] and click_pos[1] < self.y + self.image.get_height() and self.y < click_pos[1]:
            global current_ship
            current_ship = self.ship

Blank = Ship("cube.png",1,"None")
current_ship = Blank

Saul = Ship("1x2_boat_better_call_saul.png", 2, screen, "Saul")
Saul_button = Ship_button(10, screen.get_height()-30, "Saul_knapp.png", Saul)

Walter = Ship("1x3_boat_walter_white_jesse_we_need_to_cook.png", 3, screen, "Walter")
Walter_button = Ship_button(Saul_button.next_x,screen.get_height()-30, "Walter_knapp.png", Walter)

Mike = Ship("1x4_mike_boat_ok_ok_cool_yesyes_balls.png", 4, screen, "Mike")
Mike_button  = Ship_button(Walter_button.next_x,screen.get_height()-30, "Mike_knapp.png", Mike)

Jesse = Ship("1x6_JESSE_WE_NEED_TO_COOK_JESSE.png", 6, screen, "Jesse")
Jesse_button = Ship_button(Mike_button.next_x, screen.get_height()-30,"Jesse_knapp.png", Jesse)


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
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            if pygame.mouse.get_pos()[1] > 720: 
                Saul_button.inside_button(pygame.mouse.get_pos())
                Walter_button.inside_button(pygame.mouse.get_pos())
                Mike_button.inside_button(pygame.mouse.get_pos())
                Jesse_button.inside_button(pygame.mouse.get_pos())
            elif current_ship.name != "None" and pygame.mouse.get_pos()[1] < screen.get_height()-30-(current_ship.length-1)*72:
                current_ship.pos = pygame.mouse.get_pos()
                current_ship.in_view = True
            elif current_ship.name != "None" and pygame.mouse.get_pos()[1] > screen.get_height()-30-(current_ship.length-1)*72:
                print("Fail")
                fail_time = time.time()
                failed = True
    
    #Code for drawing Saul ship
    Saul.drawShip()
    Walter.drawShip()
    Mike.drawShip()
    Jesse.drawShip()

    screen.blit(Saul_button.image, (Saul_button.x, Saul_button.y))
    screen.blit(Walter_button.image, (Walter_button.x, Walter_button.y))
    screen.blit(Mike_button.image, (Mike_button.x, Mike_button.y))
    screen.blit(Jesse_button.image, (Jesse_button.x, Jesse_button.y))

    if failed and time.time() - fail_time < 1.5:
        screen.blit(invalid_placement,(screen.get_width()/2-72,screen.get_height()/2-72))
    elif failed:
        failed = False
    pygame.display.update()
