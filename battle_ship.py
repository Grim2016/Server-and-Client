import pygame

pygame.init()

MAIN_WINDOW = pygame.display.set_mode([720, 750])
sea_square = pygame.image.load("Pictures/196190_hav_None.png").convert()
POSSIBLE_POSITIONS = [pos for pos in range(0,MAIN_WINDOW.get_width()+72,72)]
class Ship:
    """
    Class representing the ships
    """
    def __init__(
            self, image: str, length: int, screen: pygame.Surface, #Nondefault params
            name: str="None") -> None:
        self._base_image: pygame.Surface = pygame.image.load(image).convert_alpha()
        self.in_view: bool = False
        self.length: int = length
        self.name: str = name
        self.screen: pygame.Surface = screen
        self.temp_pos: list = [0,0]
        self.pos: list = [0,0]
        self.pointing: str = "up"
        self.possible_x: list = POSSIBLE_POSITIONS
        self.possible_y: list = POSSIBLE_POSITIONS[:-self.length+1]
        self.angle: int = 0
    def draw_ship(self):
        """
        Draws ship if it is in view
        """
        if self.in_view:
            self.screen.blit(pygame.transform.rotate(self._base_image, self.angle),(self.pos[0]*72,self.pos[1]*72))
    def __str__(self) -> str:
        return f"{self.name}: {self.pos[0]},{self.pos[1]}, Supposed to be displayed: {self.in_view}"
    
    def change_possible_pos(self, direction):
        print(direction)
        self.pointing = direction
        if (self.pointing == "up" or "down") and self.pos[1] > 10-self.length:
            self.pos[1] = 10-self.length
        elif (self.pointing == "left" or "right") and self.pos[0] > 10-self.length:
            self.pos[0] = 10-self.length
        
        if self.pointing == "left":
            print("E")
            self.possible_x = POSSIBLE_POSITIONS[:-self.length+1]
            self.possible_y = POSSIBLE_POSITIONS
            self.angle = 90
        elif self.pointing == "right":
            self.possible_x = POSSIBLE_POSITIONS[:-self.length+1]
            self.possible_y = POSSIBLE_POSITIONS
            self.angle = 270
        elif  self.pointing == "up":
            self.possible_x = POSSIBLE_POSITIONS
            self.possible_y = POSSIBLE_POSITIONS[:-self.length+1]
            self.angle = 0
        elif self.pointing == "down":
            self.possible_x = POSSIBLE_POSITIONS
            self.possible_y = POSSIBLE_POSITIONS[:-self.length+1]
            self.angle = 180

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
    for i in range(0,MAIN_WINDOW.get_width(),72): #Creates the grid
        for j in range(0,MAIN_WINDOW.get_height()-30,72):
            MAIN_WINDOW.blit(sea_square,(i,j))
    #Get events
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                current_ship.change_possible_pos("right")
            if event.key == pygame.K_LEFT:
                current_ship.change_possible_pos("left")
            if event.key == pygame.K_UP:
                current_ship.change_possible_pos("up")
            if event.key == pygame.K_DOWN:
                current_ship.change_possible_pos("down")
        if event.type == pygame.MOUSEBUTTONUP:
            if pygame.mouse.get_pos()[1] > 720: #Check if buttons are pressed
                Saul_button.mouse_pos_in_button(pygame.mouse.get_pos())
                Walter_button.mouse_pos_in_button(pygame.mouse.get_pos())
                Mike_button.mouse_pos_in_button(pygame.mouse.get_pos())
                Jesse_button.mouse_pos_in_button(pygame.mouse.get_pos())
            elif (current_ship.name != "None"
                    and pygame.mouse.get_pos()[1] < MAIN_WINDOW.get_height()-30):
                mouse_pos = pygame.mouse.get_pos()
                for i in current_ship.possible_y:
                    if mouse_pos[1] <=i:
                        current_ship.temp_pos[1] = i/72-1
                        x_failed = False
                        break
                    else:
                        x_failed = True
                
                for i in current_ship.possible_x:
                    if mouse_pos[0] <= i:
                        current_ship.temp_pos[0] = i/72-1
                        y_failed = False
                        break
                    else:
                        y_failed = True
                
                if x_failed or y_failed:
                    failed = True
                    fail_time = pygame.time.get_ticks()
                    current_ship.temp_pos = current_ship.pos
                    x_failed, y_failed = False, False
                else:
                    print("Didn't fail")
                    current_ship.pos = current_ship.temp_pos
                    current_ship.in_view = True
                    print(current_ship)
                    
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
