import pygame

pygame.init()

MAIN_WINDOW = pygame.display.set_mode([720, 750])
sea_square = pygame.image.load("Pictures/196190_hav_None.png").convert()

class Ship:
    """
    Class representing the ships
    """
    def __init__(
            self, image: str, length: int, screen: pygame.Surface, #Nondefault params
            name: str="None") -> None:
        self.image: pygame.Surface = pygame.image.load(image).convert_alpha()
        self.pos: int
        self.in_view: bool = False
        self.length: int = length
        self.name: str = name
        self.screen: pygame.Surface = screen
    def draw_ship(self):
        """
        Draws ship if it is in view
        """
        if self.in_view:
            for x_coord in range(0,self.screen.get_width()+72,72):
                for y_coord in range(0,self.screen.get_height()-30,72):
                    if self.pos[0] < x_coord and self.pos[1] < y_coord:
                        self.screen.blit(self.image,(x_coord-72,y_coord-72))
                        break
                if self.pos[0] < x_coord:
                    break

class ShipButton:
    """
    Represents buttons for selecting ships
    """
    def __init__(
            self, x_coord: int, y_coord: int,image: str, ship: Ship, #Nondefault params
            size_mod: int=0.66, incr: int=10) -> None:
        self.x_coord: int = x_coord
        self.y_coord: int = y_coord
        self.image: pygame.Surface = pygame.image.load(image).convert_alpha()
        self.ship = ship
        self.image = pygame.transform.scale(
            self.image,
            (
                self.image.get_width()*size_mod,
                self.image.get_height()*size_mod
            )
        )
        self.next_x_coord: int = self.x_coord + self.image.get_width() +incr
    def mouse_pos_in_button(self, click_pos: tuple) -> bool:
        """
        Checks if mouse position is overlapping with a point in the button
        """
        if (click_pos[0] < self.x_coord + self.image.get_width()
                and self.x_coord < click_pos[0] 
                and click_pos[1] < self.y_coord + self.image.get_height()
                and self.y_coord < click_pos[1]):
            global current_ship
            current_ship = self.ship

Blank = Ship("cube.png",1,"None")
current_ship = Blank

Saul = Ship("Pictures/Boats/1x2_boat_better_call_saul.png", 2, MAIN_WINDOW, "Saul")
Saul_button = ShipButton(
    10,
    MAIN_WINDOW.get_height()-30,
    "Pictures/Buttons/Saul_knapp.png",
    Saul
)

Walter = Ship("Pictures/Boats/1x3_boat_walter_white_jesse_we_need_to_cook.png", 3, MAIN_WINDOW, "Walter")
Walter_button = ShipButton(
    Saul_button.next_x_coord,
    MAIN_WINDOW.get_height()-30,
    "Pictures/Buttons/Walter_knapp.png",
    Walter
)

Mike = Ship("Pictures/Boats/1x4_mike_boat_ok_ok_cool_yesyes_balls.png", 4, MAIN_WINDOW, "Mike")
Mike_button  = ShipButton(
    Walter_button.next_x_coord,
    MAIN_WINDOW.get_height()-30,
    "Pictures/Buttons/Mike_knapp.png",
    Mike
)

Jesse = Ship("Pictures/Boats/1x6_JESSE_WE_NEED_TO_COOK_JESSE.png", 6, MAIN_WINDOW, "Jesse")
Jesse_button = ShipButton(
    Mike_button.next_x_coord,
    MAIN_WINDOW.get_height()-30,
    "Pictures/Buttons/Jesse_knapp.png",
    Jesse
)

invalid_placement = pygame.image.load("Pictures/Ugyldig_plassering.png").convert_alpha()
fail_time: int
failed = False
while True:
    MAIN_WINDOW.fill((90,90,90))
    
    #Creates the grid
    for i in range(0,MAIN_WINDOW.get_width(),72):
        for j in range(0,MAIN_WINDOW.get_height()-30,72):
            MAIN_WINDOW.blit(sea_square,(i,j))
    #Get events
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            if pygame.mouse.get_pos()[1] > 720: 
                Saul_button.mouse_pos_in_button(pygame.mouse.get_pos())
                Walter_button.mouse_pos_in_button(pygame.mouse.get_pos())
                Mike_button.mouse_pos_in_button(pygame.mouse.get_pos())
                Jesse_button.mouse_pos_in_button(pygame.mouse.get_pos())
            elif (current_ship.name != "None"
                    and pygame.mouse.get_pos()[1] < MAIN_WINDOW.get_height()-30-(
                        current_ship.length-1
                        )*72):
                current_ship.pos = pygame.mouse.get_pos()
                current_ship.in_view = True
            elif (current_ship.name != "None"
                    and pygame.mouse.get_pos()[1] > MAIN_WINDOW.get_height()-30-(
                            current_ship.length-1
                        )*72):
                fail_time = pygame.time.get_ticks()
                failed = True

    #Code for drawing Saul ship
    Saul.draw_ship()
    Walter.draw_ship()
    Mike.draw_ship()
    Jesse.draw_ship()

    MAIN_WINDOW.blit(Saul_button.image, (Saul_button.x_coord, Saul_button.y_coord))
    MAIN_WINDOW.blit(Walter_button.image, (Walter_button.x_coord, Walter_button.y_coord))
    MAIN_WINDOW.blit(Mike_button.image, (Mike_button.x_coord, Mike_button.y_coord))
    MAIN_WINDOW.blit(Jesse_button.image, (Jesse_button.x_coord, Jesse_button.y_coord))

    if failed and pygame.time.get_ticks() - fail_time < 1000:
        MAIN_WINDOW.blit(
            invalid_placement,
            (MAIN_WINDOW.get_width()/2-72,MAIN_WINDOW.get_height()/2-72)
        )
    elif failed:
        failed = False
    pygame.display.update()
